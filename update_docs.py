import subprocess
from pathlib import Path

import requests
import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
folders = ["easy", "medium", "hard"]
language_map = {
    "py": "Python",
}
summary = {}
all_files = []

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
    prompt = f"📖 Refreshing {folder.capitalize()}"
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
    text = """
<figure markdown>
![Logo](https://assets.leetcode.com/static_assets/public/webpack_bundles/images/logo-dark.e99485d9b.svg){ width="128" }
</figure>

# LeetCode

## Summary by Difficulty
""".lstrip()

    for folder, total in summary.items():
        text += f"""
- [{folder.capitalize()} ^{total}^]({folder}.md)
"""
    f.write(text)
