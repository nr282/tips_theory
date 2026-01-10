"""
Given a sorted array arr, two integers k and x, return the k closest integers to x in the array.

The result should be sorted in ascending order.

An integer a is closer than the integer b if:
    1. |a-x| < |b-x|, or
    2. |a-x| == |b-x| and a < b

-----------------------------

In this solution, I will first create some examples:
    1. arr = [1,2,3,4,5] and k = 4 and x = 3

In the problem, we can see that if we create a window designated
by left (l) and right (r) pointers, we can successively increase.

In order to find the location of x in the array, we may first need to do binary search.

1. First, do binary search to find x in the array.
2. Second, apply increasing window dynamics to find the k closest elements.
3. I figured out that I had to first do a binary search to find the correct index.


Review:

1. Implementation took me around 24 minutes.
2. My implementation handles from my perspective the critical cases.
3. The problem was an unseen medium-level problem.
4. I kept the window starting around the middle value and only after significant
    index checking would increase said-value.

Areas to increase accuracy.
    - To make the code cleaner, I could break the binary search into its own function.
    - To make the code cleaner, one may be able not to have copy and paste so much code
    but instead break the function into helper functions.





"""

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        #Step 1: Develop binary search to find the index of x.
        l = 0
        n = len(arr)
        r = n - 1

        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1

        # Step 2: Create a window around the found index and incrementally increase
        l_w = l
        r_w = l
        closest = []
        num_closest = 0
        while num_closest < k:

            l_val, r_val = None, None
            if l_w >= 1:
                l_val = arr[l_w - 1]
            if r_w < n - 1:
                r_val = arr[r_w + 1]

            if l_val is not None and r_val is not None:
                l_diff = abs(l_val - x)
                r_diff = abs(r_val - x)
                if l_diff == r_diff:
                    closest.append(l_val)
                    num_closest += 1
                    l_w -= 1
                else:
                    if l_diff < r_diff:
                        closest.append(l_val)
                        num_closest += 1
                        l_w -= 1
                    else:
                        closest.append(r_val)
                        num_closest += 1
                        r_w += 1
            elif l_val is None and r_val is None:
                break
            else:
                if l_val is not None:
                    closest.append(l_val)
                    num_closest += 1
                    l_w -= 1
                else:
                    closest.append(r_val)
                    num_closest += 1
                    r_w -= 1

        return closest

#Refactored version.
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Step 1: Develop binary search to find the index of x.
        def binary_search(arr, x):
            l = 0
            n = len(arr)
            r = n - 1
            while l < r:
                mid = l + (r - l) // 2
                if arr[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1
            return l



        def find_k_closest(arr, l, k):
            l_w = l
            r_w = l
            closest = []
            num_closest = 0
            while num_closest < k:

                l_val, r_val = None, None
                if l_w >= 1:
                    l_val = arr[l_w - 1]
                if r_w < n - 1:
                    r_val = arr[r_w + 1]

                if l_val is not None and r_val is not None:
                    l_diff = abs(l_val - x)
                    r_diff = abs(r_val - x)
                    if l_diff == r_diff: #TODO: These three lines could be refactored into helper function
                        closest.append(l_val)
                        num_closest += 1
                        l_w -= 1
                    else:
                        if l_diff < r_diff:
                            closest.append(l_val)
                            num_closest += 1
                            l_w -= 1
                        else:
                            closest.append(r_val)
                            num_closest += 1
                            r_w += 1
                elif l_val is None and r_val is None:
                    break
                else:
                    if l_val is not None:
                        closest.append(l_val)
                        num_closest += 1
                        l_w -= 1
                    else:
                        closest.append(r_val)
                        num_closest += 1
                        r_w -= 1

            return closest


        n = len(arr)
        l = binary_search(arr, x)
        closest = find_k_closest(arr, l, k)
        return closest







