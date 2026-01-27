"""
Array partition.
----------------

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.



n = 4
arr = [1,2,5,6,9,10,2,8]


First, we propose sorting the array. And then pair min and max values.

sorted_arr = [1,2,2,5,6,8,9,10]

min(1,2) = 1
min(2,5) = 2
min(6,8) = 6
min(9,10) = 9

= 1 + 2 + 6 + 9 = 18


min(1,10) = 1
min(2,9) = 2
min(2,8) = 2
min(5,6) = 5

= 1 + 2 + 2 + 5 = 10



Key Test Cases:
    1. Zero element
    2.

"""



from typing import List
def arrayPairSum(nums: List[int]) -> int:
    s = 0
    nums_sorted = sorted(nums)
    n = len(nums_sorted) // 2
    for i in range(n):
        s += min(nums_sorted[2*i], nums_sorted[2*i+1])
    return s


if __name__ == "__main__":

    sorted_arr = [1, 2, 2, 5, 6, 8, 9, 10]
    val = arrayPairSum(sorted_arr)
    assert(val == 18)

    sorted_arr = []
    val = arrayPairSum(sorted_arr)
    assert (val == 0)

    sorted_arr = [2,2]
    val = arrayPairSum(sorted_arr)
    assert (val == 2)


