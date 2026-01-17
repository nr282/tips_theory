"""
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using
k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.


Review of the material
------------------------------------------------------------------------------------------------------------------------

sweetness = [1, 2, | 3, 4, | 3, 2, | 1]
k = 3


The key idea here is that this is an adhoc binary search problem, where we see there is a construction/cutting
that has a particular minimum segment.

"""

from typing import List


def canBeCut(sweetness, k, min_size):

    cuts = 0
    n = len(sweetness)
    i = 0
    curr_cut = 0
    num_elements_in_cut = 0
    while i < n:
        if curr_cut < min_size:
            curr_cut += sweetness[i]
            num_elements_in_cut += 1
            i += 1
        else:
            cuts += 1
            curr_cut = 0
            num_elements_in_cut = 0

    return cuts >= k


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        l = 0
        r = sum(sweetness)

        while l < r:
            mid = l + (r - l) // 2
            if canBeCut(sweetness, k, mid):
                l = mid + 1
            else:
                r = mid

        return l



