"""
A conveyor belt has packages that must be shipped from one port to another within D days.

The ith-package on the conveyor belt has a weight of weights[i].

Each day, we load the ship with packages on the conveyor belt in the order
given by weights.

We may not load more capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages
on the conveyor belt being shipped within D days.

-----------------------------------------------------------------------------------------------------------------------




weights = [5, 9, 4, 2, 1, 10]
days = 3

Find the minimum weight of the ship.
1. A maximum is the sum of all the weights. With this value one can ship all in one day. --> Return True
2. A minimum can be found when setting the weight of the ship is 0. Return False.

How do we check that we can ship all the packages within D days with a certain amount of weight?
    1. The chosen weight has to be greater than the: sum(weights) / D.




weights = [5, 9, 4, 2, 1, 10]
days = 3


Took 3 extra minutes to fix issues.

Completed in 20 minutes.
Finished solution.


"""

from typing import List
import math


def can_ship(weights, days, ship_weight):

    n = len(weights)
    if n == 1:
        return weights[0] <= ship_weight

    d = 0
    i = -1

    curr_w = 0
    while i < n-1:
        if (i + 1 < n) and (weights[i + 1] + curr_w <= ship_weight):
            curr_w += weights[i + 1]
            i += 1
        else:
            d += 1
            curr_w = 0

    return d <= days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights) #Ship everything in one day

        while l < r:
            mid = l + (r - l) // 2
            if can_ship(weights, days, mid):
                r = mid
            else:
                l = mid + 1

        return l














