"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.


["a", "e", "i", "y"]



"""

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)
        num_swaps = n // 2
        for i in range(num_swaps):
            l = s[i]
            r = s[n - i - 1]
            s[i] = r
            s[n - i - 1] = l
