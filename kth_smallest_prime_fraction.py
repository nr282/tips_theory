"""
You are given a sorted integer array arr containing 1 and prime numbers,
where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length,
we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an
array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Analysis:
----------

Example 1:
----------

arr = [1,2,3,5], k = 3

1/5, 1/3, 2/5, 1/2, 3/5, 2/3
    1. Why are these numbers prime?

There is a numerator or denominator, namely i and j.

Suppose that the kth smallest fraction is arr[i-1]/arr[j-1]

then:
    1. arr[i]/arr[j-1]
    2. arr[i-1]/arr[j-2]

The issue with this approach is that this will take (10^3)^2 = 1 * 10^6.

Is there a much faster way to search the space?

arr = [1,2,3,5], k = 3

We can consider the following fractions:

    i

    1       2   3   5
    2       3   5
    3       5
    5       x

This seems to be the correct structure.



        end
start
        1       2           3   4    5           4
                2           3   4    5           3
                            3   4    5           2
                                4    5           1
                                     x


                            (1,5)               x=1
                        (2,5), (1,4)            x=2
                    (3,5), (2,4), (1,3)         x=3
                (4,5), (3,4), (2,3), (1,2)      x=4


(1,5) ---> (1,4) ---> (1,3) ----> (2,5) ----> (2,4) --->



Because of the primeness, there will not be duplicates.

Let us consider the ordering here:

(1,5) < (1,4) < (2,5) <

"""

from typing import List
def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:


    i = 0
    j = len(arr) - 1
    count = 0
    starting =
    while count < k:










if __name__ == "__main__":
    pass

