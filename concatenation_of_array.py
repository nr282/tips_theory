"""
Given an integer array nums of length n, you want to create an array ans
of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i]
for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.


"""

from typing import List

def getConcatenation(nums: List[int]) -> List[int]:

    res = []
    n=len(nums)
    for i in range(2*n):
        res.append(nums[i%n])
    return res

if __name__ == "__main__":

    nums = [1,2,1]
    res = getConcatenation(nums)
    print(res)

    nums = []
    res = getConcatenation(nums)
    print(res)

    nums = [1]
    res = getConcatenation(nums)
    print(res)
