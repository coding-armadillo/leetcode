import pickle
import subprocess
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path

import requests
import urllib3
import seaborn as sns
from bs4 import BeautifulSoup
from tqdm import tqdm

parser = ArgumentParser(
    prog="UpdateDocs",
    description="A helper script to update docs",
)
parser.add_argument("-f", "--force", action="store_true")
args, _ = parser.parse_known_args()
force = args.force

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
folders = ["easy", "medium", "hard"]
language_map = {
    "py": "Python",
}
summary = {}
all_files = []

try:
    with open("docs/.cache", "rb") as f:
        cache = pickle.load(f)
except:
    cache = {}

for folder in folders:
    uri = f"src/{folder}"
    if not Path(uri).exists():
        Path(uri).mkdir(exist_ok=True)

    files = list(Path(uri).glob("*"))
    solutions = {}

    for file in files:
        if file.stem not in solutions:
            solutions[file.stem] = [file.name]
        else:
            solutions[file.stem].append(file.name)
        all_files.append(file.name)

    total = len(solutions)
    summary[folder] = total

    if not force and set(solutions.keys()) < set(cache.keys()):
        print(f"⛔ Skipped {uri}: no update needed")
        print()
        continue

    try:
        subprocess.call(
            [
                "black",
                uri,
            ]
        )
    except:
        pass

    text = """---
hide:
  - toc
---
"""
    text += f"""
# Difficulty - {folder.capitalize()}
"""
    prompt = "📖 Refreshing Docs"
    for solution, languages in tqdm(sorted(solutions.items()), desc=prompt):
        url = f"https://leetcode.com/problems/{solution}/"
        if solution in cache:
            name = cache[solution]
        else:
            html = requests.get(url, verify=False).text
            soup = BeautifulSoup(html, "html.parser")
            name = soup.find("title").text.split(" - ")[0]
            cache[solution] = name
        if len(languages) > 1:
            suffix = f"s in {len(languages)} languages"
        else:
            ext = languages[0].split(".")[-1]
            suffix = f" in {language_map[ext]}"
        card = f"""
## [{name}]({url})

??? success "Solution{suffix}"
"""
        for language in sorted(languages):
            ext = language.split(".")[-1]
            card += f"""
    === "{language_map[ext]}"

        ```{ext} linenums="1"
        --8<-- "{uri}/{language}"
        ```
"""
        text += card

    print()

    with open(f"docs/{folder}.md", "w", encoding="utf-8") as f:
        f.write(text)

with open("docs/index.md", "w") as f:
    text = """# LeetCode

## Summary by Difficulty
"""

    for folder, total in summary.items():
        text += f"""
- [{folder.capitalize()} ^{total}^]({folder}.md)
"""
    text += f"""
## Summary by First Character

![summary-by-first-char](summary-by-first-char.png)
"""
    f.write(text)

with open("docs/.cache", "wb") as f:
    pickle.dump(cache, f)

s = Counter([k[0] for k in cache.values()])
ax = sns.barplot(x=list(s.keys()), y=list(s.values()))
ax.get_figure().savefig("docs/summary-by-first-char.png", bbox_inches="tight")
