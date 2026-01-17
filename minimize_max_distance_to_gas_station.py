"""
You are given an integer array stations that represents the positions of the
gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.



Analysis:
---------

positions of gas stations

gas_positions = [1, 2, 5, 10, 11, 5]





--------------------------------------------------------
                        x

    1, 2, x, x, 5, x,  x,  x,  x, 10, 11,

k = 10


Basically, we look to use binary search on the minimum and maximum.

What is the minimum?


#False, False, False, True, True, True



"""

from typing import List
import heapq


def placement_possible(k, max_heap, min_distance):


    num_placed = 0
    while num_placed < k:

        max_diff = -1 * heapq.heappop(max_heap)
        left_diff, right_diff = max_diff / 2.0
        heapq.heappush(max_heap, left_diff)
        heapq.heappush(max_heap, right_diff)

        num_placed += 1

    max_diff = -1 * heapq.heappop(max_heap)
    if max_diff <= min_distance:
        return True
    else:
        return False

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:


        #Do preprocessing on stations with integer k.
        stations_sorted = sorted(stations)
        diffs = []
        n = len(stations_sorted)
        for i in range(n-1):
            diffs.append(stations_sorted[i+1] - stations_sorted[i])

        #Create heapq
        max_heap = []
        #diff_heap = heapq.heapify(diffs)
        for diff in diffs:
            heapq.heappush(max_heap, -1 * diff)

        l = 0
        r = max(diffs)
        mid = l + (r - l) // 2
        while l < r and (mid - l) > 1e-7:
            mid = l + (r - l) // 2
            if not placement_possible(k, max_heap, mid):
                l = mid
            else:
                r = mid

        return l



