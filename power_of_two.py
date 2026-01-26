"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.

"""


from typing import Optional
def isPowerOfTwo(n: int) -> bool:
    nx = n
    while nx > 1:
        m = nx % 2
        nx = nx // 2
        if m != 0:
            return False
    return True


if __name__ == '__main__':

    pass





