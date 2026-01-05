"""
You are given a 0-indexed integer array nums of positive integers, where w[i] describes the weight of index i.

You need to implement the function pickIndex(), which randomly picks and index in the range of
[0, w.length - 1] proportionally to its weight. The probability picks an index i is w[i] / sum(w).


------------------------------------------------------------------------------------------------------------
This problem is completed.

I drew the following example to help me to start off.

example = [1,10,3,4,5,6,1]
index =   [0,1,2,3,4,5,6]

I determined that the call to random I could make would be
u = random.uniform(0,1)

I decided to calculate the total sum.

s = sum(example)

I then calculated the prefix sum.
[1/s,11/s,14/s,18/s,23/s,29/s,30/s]
[0,1,  2, 3, 4, 5, 6]

I calculated the
target = u * s

I then recognized that the differences in the prefix sum
represented probabilities, and that one could select an element
from example by looking at which w[index], where a binary search for target
in the prefix sum array.





"""

from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.n =  len(w)
        self.w = w
        self.s = sum(w)
        r = 0
        p_sum = []
        for i in range(len(w)):
            r += w[i]
            p_sum.append(r/self.s)
        self.p_sum = p_sum

    def pickIndex(self) -> int:

        if self.n == 1:
            return self.w[0]

        u = random.uniform(0,1)
        target = u * self.s

        l = 0
        r = self.n - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.p_sum[mid] > target:
                r = mid
            else:
                l = mid + 1

        return self.w[l]











# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


if __name__ == "__main__":
    obj = Solution([1])
    print(obj.pickIndex())