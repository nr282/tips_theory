"""
Design a time-based key-value data structure that can store multiple values for the
same key at different time stamps and retrieve the key's value at the time stamp.

Implement TimeMap class.

The functions for TimeMap are:
    1. set(key, value, timestamp).
    2. get(key, timestamp)

1. I was going to use a list that we keep sorted. However, I need constant-time insert.
2. If I need constant time insert, then a linked-list would be best.
3. For getting the value from a sorted-list we can just use the binary search.

The information in the prompt is very helpful. The calls to set have strictly increasing
timestamps. This will allow us to ensure that we have a sorted list.

This problem took me 22 minutes and 49 seconds to complete.
There was a core concern if _binary_search was implemented correctly.
After running through the lower-bound binary search precondition, I verified that it was.



"""

from typing import List
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def _binary_search(self, arr, target_timestamp):

        n = len(arr)
        l = -1
        r = n - 1

        while l < r:
            mid = l + (r - l) // 2
            if arr[mid][0] > target_timestamp:
                mid = mid - 1
            else:
                mid = mid + 1

        return arr[l][1] if l != -1 else ""

    def get(self, key: str, timestamp: int) -> str:

        vals = self.map[key]
        target_val = self._binary_search(vals, timestamp)
        return target_val





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)