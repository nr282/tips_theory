"""


1. Iterate over elements in our input == Expand window (left, right)
2. Meet the condition to stop expansion -- the most difficult part.
3. Remove elements from the window.
4. Process the current valid window.


nums = [1,0,1,1,0,1]

For sliding window, I believe that we should use
    1. a for-loop for the outer loop.
    2. a while-loop to enforce the interior condition.
    3. keep track of the ones and the zeros.
`   4.

"""

from typing import List

def findMaxConsecutiveOnesBad(nums: List[int]) -> int:

    #Take the example nums= [0]

     num0 = 0
     l = 0
     res = 0

     # 1. Iterate over elements in our input == Expand the window (left, right)
     for r in range(len(nums)):

        #2. Meet the condition to stop expansion - the most difficult part (chi xai while)
        while num0 == 1 and nums[r] == 0:
             # 2.1. Remove nums[left] from window
            if nums[l] == 0:
                num0 -= 1
             # 2.2. Contract the window
            l += 1

        if nums[r] == 0:
            num0 += 1

         # 3. Process the current valid window.
        res = max(res, r - l + 1)

     return res



def findMaxConsecutiveOnesGood(nums: List[int]) -> int:


    #l is None and r is None means there is no active window.
    #l is not None and r is not None means there is an active window
    #All active windows must be processed into result by the end of
    #the function.
    l = None
    r = None
    n = len(nums)
    i = 0
    if n == 0:
        return 0

    res = 0
    while i < n:
        if nums[i] == 1 and l is None and r is None:
            l = i
            r = i
        elif nums[i] == 1 and l is not None and r is not None:
            r += 1
        elif nums[i] == 0 and l is None and r is None:
            pass
        else:
            res = max(res, r - l + 1)
            l, r = None, None
        i += 1

    if l is not None and r is not None:
        res = max(res, r - l + 1)
        l, r = None, None


    assert (l is None and r is None)
    return res





if __name__ == "__main__":

    test1 = [0]
    test2 = [1]

    result1 = findMaxConsecutiveOnesGood(test1)
    result2 = findMaxConsecutiveOnesGood(test2)

    print("Result1: ")
    print(result1)
    print("Result2: ")
    print(result2)

