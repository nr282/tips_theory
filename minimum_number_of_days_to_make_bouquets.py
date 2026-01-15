"""
You are given an integer array bloomDay, an integer m, and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then
can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
If it is impossible to make m bouquets return -1.

Analysis:
----------------------------------------------


bloomDay = [4,2,8,10,6,9]
m = 1 #Number of bouquets to make
k = 4 #Adjacent flowers to use in a bouquet
n = len(bloomDay)


Structure:
    1. Search space is the number of days.
    2. On each day, a certain set of flowers bloom.
    3. We need to determine if we can make m bouquets.


The time taken for implementation is 16 minutes.

The implementation of bouquetPossible is a greedy algorithm.

It takes the following form

Suppose that hte diagram of flowers in the bouquet is:

o ---> blooming
x ---> not blooming

As we move from left to right, we try to create as many bouquets as possible.
What we can see is that greedy stays ahead.

Hence, we only need to consider the left-most starting point, and if we can form a buoquest with
the adjacent flowers, then the adjacent flowers will not partcipate in a maximizing buouquet.

Our method will stay ahead in the number of created bouquets.


    --------->
------------->
o   o   o   x   x   x   o   o   o   o



"""


from typing import List


def bouquestPossible(bloomDay, day, k):

    num_bouquets = 0
    i = 0
    n = len(bloomDay)
    curr_b = 0
    while i < n:
        if bloomDay[i] <= day:
            curr_b += 1

            if curr_b == k:
                num_bouquets += 1
                curr_b = 0
        else:
            curr_b = 0
        i += 1

    return num_bouquets


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        l = 0
        r = max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if bouquestPossible(bloomDay, mid, k):
                r = mid
            else:
                l = mid + 1

        if l == max(bloomDay):
            return -1
        else:
            return l
