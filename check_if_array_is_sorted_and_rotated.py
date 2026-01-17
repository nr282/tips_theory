"""
Given an array nums, return true if the array was originally sorted in non-decreasing order,
then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such
that B[i] == A[(i+x) % A.length] for every valid index i.

Analysis.
-------------------------------------------------------------------------------------------

A base array could be:
[1,1,4,5,7,10,24,56] -----> True

Suppose that the array is rotated:
[10,24,56,1,1,4,5,7]

"""

from typing import List

def check_non_decreasing(arr, i, j):
    is_non_decreasing = True
    while i < j - 1:
        if arr[i] <= arr[i+1]:
            is_non_decreasing = True
        else:
            is_non_decreasing = False
    return is_non_decreasing


def check_non_increasing(arr, i, j):
    is_non_increasing = True
    while i < j - 1:
        if arr[i] >= arr[i+1]:
            is_non_increasing = True
        else:
            is_non_increasing = False
    return is_non_increasing


class Solution:
    def check(self, nums: List[int]) -> bool:

        n = len(nums)
        if n <= 2:
            return True

        i = 0
        index = None
        while i < n - 1:
            first = nums[i]
            second = nums[i+1]
            if first >= second:
                index = i
                break
            i += 1

        if index is None:
            all_non_increasing = check_non_increasing(nums, 0, n-1)
            all_non_decreasing = check_non_decreasing(nums, 0, n-1)
            return all_non_increasing or all_non_decreasing
        else:
            kinked_properly = check_non_decreasing(nums, 0, index) and check_non_increasing(nums, index + 1, n - 1)
            return kinked_properly
