"""
A row-sorted binary matrix means that all elements are 0 or 1 and each
row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed)
of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly.
You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).

BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements
[rows, cols], which means the matrix is rows x cols.


Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat.
You will not have access to the binary matrix directly.

-------------------------------------------------------------------------------------------
Analysis:

Example Matrix:
--------------

0, 0, 1, 1, 1
0, 0, 0, 1, 1
0, 1, 1, 1, 1
1, 1, 1, 1, 1


There is clearly structure within the row.
But there is no structure from one row to the next.
So we will have to touch every row.
We may not need to touch every column in each row, since we immediately
exclude a large number of rows.


"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


def find_index_of_first_one(binaryMatrix, r_i, i, j):

    l = i
    r = j + 1
    while l < r:
        mid = l + (r - l) // 2
        if binaryMatrix.get(r_i, mid) == 1:
            r = mid
        else:
            l = mid + 1

    if l == j + 1:
        return None
    else:
        return l


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        m, n = binaryMatrix.dimensions()
        min_c_i = None
        for i in range(m):
            if min_c_i is not None:
                c_i = find_index_of_first_one(binaryMatrix, i, 0, min_c_i)
            else:
                c_i = find_index_of_first_one(binaryMatrix, i, 0, n-1)
            if c_i is not None:
                if min_c_i is not None:
                    min_c_i = min(min_c_i, c_i)
                else:
                    min_c_i = c_i


        if min_c_i is None:
            return -1
        else:
            return min_c_i






