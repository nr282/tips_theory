"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.


Analysis
--------------------------


flowerbed = [1,0,0,1]
n = 1

flowerbed = [1,0,0,0,1]
n = 1

flowerbed = [1,0,0,0,0,1]
n = 2


flowerbed = [0,0,0,0,0,1]
n = 2


flowerbed = [1,0,1,0,0,1] ---
result = 2

"""

from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:

    num = 0
    size=len(flowerbed)
    for i in range(size):
        if i == 0 and i == size-1:
            if flowerbed[i] == 0:
                flowerbed[i] = 1
                num += 1
        elif i == 0:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                num += 1
        elif i == size-1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                num += 1
        else:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                num += 1

    return num >= n


if __name__ == "__main__":

    flowerbed = [0, 0, 0, 0, 0, 1]
    n = 3
    print(canPlaceFlowers(flowerbed, n))

    flowerbed = [1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))

    flowerbed = [1]
    n = 0
    print(canPlaceFlowers(flowerbed, n))