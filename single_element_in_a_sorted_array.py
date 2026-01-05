"""
Leetcode problem is provided here:
https://leetcode.com/problems/single-element-in-a-sorted-array/

Problem Statement:
------------------

You are given a sorted array consisting of only integers where every element appears exactly twice, except
for one element which appears exactly once.

Return the single element that appears only once.

Notes
------------------
    1.

Step 1: Create some examples. The examples are provided below:

    #Index:
    #0,1,2,3,4,5,6,7,8,9,10,11,12
    [1,1,2,2,3,3,4,4,8,9,9,10,10] --->
    #0,1,2,3,4,5,6,7,8
    [1,1,2,3,3,4,4,8,8] ----> 2
    [1, 1] -----> None
    [1,1,5] ----> Verified Manually.
    #0,1,2 -->
    [2,3,3] ---> 2. Verified Manually
    [1,7,7,8,8] -----> 1
    [] ---> None

These test cases seem representative to me.

As I analyze the above problem, what do I see:
    1. The single occurence has neighbors that different from it
    unless the target index is at the boundaries of the array.


Review:
Completed in half an hour.
Look at multiple approaches

"""

def singleNonDuplicate(nums: list[int]) -> int:

    #Define the search space
    n = len(nums)
    l = 0
    r = n - 1

    while l < r:
        mid = l + (r - l) // 2
        if ((mid % 2 == 0 and
             mid != (n - 1) and
             nums[mid] != nums[mid + 1])
            or (mid % 2 == 1
                and nums[mid] == nums[mid + 1])
        ):

            r = mid
        else:
            l = mid + 1

    #POSTCONDITION: Smallest index such that the condition holds.
    #This is a very complex condition.

    return nums[l]





