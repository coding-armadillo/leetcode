from typing import List


class Solution:
    def getKth(self, nums1: List[int], nums2: List[int], k: int) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.getKth(nums2, nums1, k)
        if len1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k // 2, len1)
        pb = k - pa
        if nums1[pa - 1] <= nums2[pb - 1]:
            return self.getKth(nums1[pa:], nums2, pb)
        else:
            return self.getKth(nums1, nums2[pb:], pa)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2) // 2 + 1)
        else:
            return (
                self.getKth(nums1, nums2, (len1 + len2) // 2)
                + self.getKth(nums1, nums2, (len1 + len2) // 2 + 1)
            ) * 0.5
