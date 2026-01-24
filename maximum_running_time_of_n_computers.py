"""
You have n computers. You are given the integer n and a 0-indexed integer array batteries
where the ith battery can run a computer for batteries[i] minutes.

You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment,
you can remove a battery from a computer and insert another battery any number of times.

The inserted battery can be a totally new battery or a battery from another computer.
You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.


Analysis:

Example 1
--------------------------------------------------------------
n = 2, batteries = [5,4,9]
computer 1 -----> 5 units
computer 2 -----> 4 units --> 9 units
max time is 5 units in a poor setup
---------------------------------------------------------------
n = 2, batteries = [5,4,9]
computer 1 ----> 9 units
computer 2 -----> 4 units -----> 5 units
max run time is 9. this is the theoretical maximum.

What is the maximum amount of time that can be run.
It is the sum of all batteries divided by the number of computers, n.


n = 2, batteries = [5,4,5]
computer 1 ----> 9 units
computer 2 -----> 4 units -----> 5 units
max run time is 9. this is the theoretical maximum.

n = 2, batteries = [1,1,1,1,1,1,1,1,1,1]
computer 1 ----> 5 units
computer 2 ----> 5 units
max run time is 5. this is the theoretical maximum.

In order to achieve the maximum, does it make sense to schedule the biggest batteries
first or at the end.

This is a good question.

Suppose that you knew how long was the maximum or how long it would take.
How would you schedule optimally.
This sets me up for an ad-hoc binary search.

There must be a greedy algorithm that exists in solving this problem, otherwise
it would not be solvable.

You can swap the battery out. This likely makes a big difference.

Take the example of:

batteries = [7,5,6,3,9]

computer 1 ----> 9   ------> 5
computer 2 ----> 7   ------> 6 --> 3

I am thinking that is it most optimal to use the larger batteries first, and then
smaller batteries last.


n = 3
batteries = [7,5,6,3,9,10]

computer 1 ---> 10,3 ---> 13
computer 2 ---> 9,5  ---> 14
computer 3 ---> 7,6 ----> 13



"""

from collections import deque
from heapq import heappush, heappop, heapify


def isRunnable(n, batteries, mid):

    h = [0 for _ in range(n)]
    heapify(h)
    batteries = sorted(batteries, reverse=True)

    for battery in batteries:
        time = heappop(h)
        time += battery
        heappush(h, time)

    isRunnable = True
    while h:
        time = heappop(h)
        if time < mid:
            isRunnable = False
            return isRunnable


    return isRunnable

from typing import List
def maxRunTime(n: int, batteries: List[int]) -> int:

    #Define search space.
    l = 0
    r = sum(batteries) / n

    while l < r:
        mid = l + (r-l) // 2
        if not isRunnable(n, batteries, mid):
            r = mid
        else:
            l = mid + 1

    return l


if __name__ == "__main__":

    n = 2
    batteries = [7, 5, 6, 3, 9]

    result = maxRunTime(n, batteries)

    print("Result is provided by: ")
    print(result)

    batteries = [5, 4, 5]
    n = 2

    result = maxRunTime(n, batteries)

    print("Result is provided by: ")
    print(result)

    batteries = [5, 4, 9]
    n = 2

    result = maxRunTime(n, batteries)

    print("Result is provided by: ")
    print(result)

    batteries = [5, 3, 9]
    n = 2

    result = maxRunTime(n, batteries)

    print("Result is provided by: ")
    print(result)

    n = 2
    batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    result = maxRunTime(n, batteries)

    print("Result is provided by: ")
    print(result)

    n = 3
    batteries = [7, 5, 6, 3, 9, 10]

    result = maxRunTime(n, batteries)

    print("Result is provided by: ")
    print(result)