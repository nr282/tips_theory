"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown.



Test out for n = 3


i = 1, row = [1]
i = 2, row = [1, 1]
i = 3, row = [1, 2, 1]

The time it took me to solve this problem was 8 minutes.

I initially was going to write some very if-else type code, but then
decided that a two for loop approach would be more efficient.



"""


from typing import List

class Solution:
    def generate(self, numRows: int) -> List[   List[int]]:

        res = []
        for i in range(1, numRows + 1):
            row = []
            for j in range(1, i+1):
                if j == 1 or j == i:
                    row.append(1)
                else:
                    index = j-1
                    row.append(res[-1][index-1] + res[-1][index])
            res.append(row)

        return res