"""
Need prefix sum theory.

Prefix Sum theory will be critical for a variety of problems.

The core problems for prefix-sum were problems involving
    1. number of ones and zeros in a binary array.
        - we calculate the running sum of 1's and 0's,
        and we search via a dictionary for the current running sum
        or a matching sum from earlier in the array.
    2. We first started with:
        1. keeping around a running sum of ones and zeros in their individual array.
        2. and then we cleaned this up by looking only at the running differences.
        3. Since it was this quantity that better expressed what we were looking for

    3. There were other patterns where a:
        1. prefix-sum was paired up with a dictionary that keeps track
        of elements earlier in the array.



"""