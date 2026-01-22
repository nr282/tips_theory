"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Review:
-----------

We are provided with two sorted arrays: nums1 and nums2.

As an example:

nums1 = [1,2,7,8,9]
nums2 = [3,4,5,6]

Return the median of the two arrays.

I am thinking that this problem could be an adhoc binary search problem.

We can determine that it is a binary search problem by the fact that the running
time is in O(log(m+n)).


If we propose that the median is a certain number then we can in O(log(m+n)) time
determine if this number is the median.

How many runs will this take?
    1. This will take O(log(m+n)) runs.
    2.


Suppose that the median is: 5


nums1 = [1,2,7,8,9] in O(log(n)), we determine that 2 elements are below, 3 elements are equal or above.
nums2 = [3,4,5,6], we determine that 2 elements are below, 2 elements are equal or above.
This can be done in O(log(m)) time.

O(log(m+n) * log(m+n))

Maybe this will not work. Is there another way of seeing if the correct number can be found.

After some examination, I think this will work.

We can break this into two binary searches. One looks to calculate the number of:
elements strictly above the number.

The second looks to calculate the number of elements strictly below the number.

What is the median?
The median is the number of

median of [1,2]
median is 1.5

Median is the number of elements above is equal to the number of elements below.

In this example,

nums1 = [1,2,7,8,9]
nums2 = [3,4,5,6]

nums1 = [1,2,7,8,9]
nums2 = [3,4,5,6]

equivalent to:
nums = [1,2,3,4,5,6,7,8,9]

The median is: 5.

The number of elements strictly below is equal to the number of elements strictly above.

What about duplicates?


nums1 = [1,2,7,8,9]
nums2 = [3,4,5,5,6]
nums = [1,2,3,4,5,5,6,7,8,9]

The median is: 5. Number below is equal to number above.


nums1 = [1,2,7]
nums2 = [3,4,5,5,6]
nums = [1,2,3,4,5,5,6,7]

The median is: 4.5.


Consider the case nums1 = [6]
Consider the case nums2 = [9]
The median is: 7.5.

we can identify 7 and 8 be interesting numbers.
Take the average of these two numbers.

I have spent too much time on this problem.


TODO: This likely does not work.



"""

from typing import List


def binary_search_greater(nums1, target):
    """


    x = [1, 2, 6, 8]
    target = 9

    return 0


    x = [1, 2, 6, 8]
    target = 0
    return 4



    x = [1, 2, 6, 8]
    target = 1
    return 3

    :param nums1:
    :param target:
    :return:
    """

    n = len(nums1)
    l = 0
    r = n

    while l < r:
        mid = l + (r - l) // 2
        if nums1[mid] < target:
            r = mid
        else:
            l = mid + 1

    return n - l

def binary_search_lesser(nums1, target):
    """


        x = [1, 2, 6, 8]
        target = 9

        return 4

        x = [1, 2, 6, 8]
        target = 0
        return 0

        x = [1, 2, 2, 6, 8]
        target = 2
        return 1

        :param nums1:
        :param target:
        :return:
    """


    n = len(nums1)
    l = 0
    r = n

    while l < r:
        mid = l + (r - l) // 2
        if nums1[mid] <= target:
            r = mid
        else:
            l = mid + 1
    return l



def strictly_greater(nums1, nums2, target):

    s = len(nums1)
    t = len(nums2)
    x = binary_search_greater(nums1, target)
    y = binary_search_greater(nums2, target)
    z = float(s + t) / 2
    return x + y < z

def strictly_less(nums1, nums2, target):

    s = len(nums1)
    t = len(nums2)
    x = binary_search_lesser(nums1, target)
    y = binary_search_lesser(nums2, target)
    z = float(s + t) / 2
    return x + y < z

def find_upper_bound_for_median_range(nums1, nums2):
    """


    """

    min_val = max(nums1[0], nums2[0])
    max_val = min(nums2[-1], nums2[-1])

    l = min_val - 1
    r = max_val

    while l < r:
        mid = l + (r - l) // 2
        target_is_greater_than_median = strictly_greater(nums1, nums2, mid)
        if target_is_greater_than_median:
            l = mid + 1
        else:
            r = mid
    return l

def find_lower_bound_for_median_range(nums1, nums2):

    min_val = max(nums1[0], nums2[0])
    max_val = min(nums2[-1], nums2[-1])

    l = min_val - 1
    r = max_val

    while l < r:
        mid = l + (r - l) // 2
        target_is_less_than_median = strictly_less(nums1, nums2, mid)
        if target_is_less_than_median:
            l = mid + 1
        else:
            r = mid
    return l


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lower_bound = find_lower_bound_for_median_range(nums1, nums2)
        upper_bound = find_upper_bound_for_median_range(nums1, nums2)
        return (lower_bound + upper_bound // 2)











