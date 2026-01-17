"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in
nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array
sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.

To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p = m + n - 1
        s = m - 1
        t = n - 1

        while p >= 0:
            if s >= 0 and t >= 0:
                if nums1[s] > nums2[t]:
                    nums1[p] = nums1[s]
                    s -= 1
                    p -= 1
                else:
                    nums1[p] = nums2[t]
                    t -= 1
                    p -= 1
            elif s >= 0:
                nums1[p] = nums1[s]
                s -= 1
                p -= 1
            else:
                nums1[p] = nums2[t]
                t -= 1
                p -= 1




