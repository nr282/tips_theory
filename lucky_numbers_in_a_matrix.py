"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


"""

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:


        if not (type(matrix) == list and type(matrix[0]) == list):
            raise ValueError("Input must be a list of lists")

        m, n = len(matrix), len(matrix[0])
        col_to_max = dict()
        row_to_min = dict()
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                col_max = col_to_max.get(j)
                row_min = row_to_min.get(i)
                if col_max is None or col_max < val:
                    col_max[j] = val
                if row_min is None or row_min > val:
                    row_min[i] = val

        lucky_number = 0
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                col_max = col_to_max[j]
                row_min = row_to_min[i]
                if val == row_min and val == col_max:
                    lucky_number += 1

        return lucky_number


