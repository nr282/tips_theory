"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.




Analysis
-----------------------------------------------------------------------------------------------------------------------

This is an example of the problem.

[1,   3,  5,  7,  7,  8]
[10, 11, 12, 15, 15, 16]
[18, 19, 20, 21, 22, 23]
[24, 25, 26, 27, 28, 29]
[40, 41, 42, 43, 44, 45]

target = 3


Solution time was 22 minutes.

"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        m, n = len(matrix), len(matrix[0])
        l = -1
        r = m

        while l < r:
            mid = l + (r - l) // 2
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                r = mid
            else:
                l = mid + 1

        if l == m or l == -1:
            return False

        l_r = -1
        r_r = n
        while l_r < r_r:
            mid = l_r + (r_r - l_r) // 2
            if matrix[l_r][mid] >= target:
                r_r = mid
            else:
                l_r = mid + 1

        if l_r == n or l_r == -1:
            return False
        else:
            return True





