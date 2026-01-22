"""
An ugly number is a positive integer that is divisible by either: a, b or c.

Given four integers n, a, b and c, return the nth ugly number.


nthUglyNumber(2, 2, 3, 5) -> 3

n = 2
a = 2
b = 3
c = 5

result = 3


n = 4
a = 2
b = 3
c = 5

1,2,3,4,5,6,7,8,9,10
  x,x,x,x,x

result = 5

really, depends on what the bounds are?


The idea that I have here is that if we consider m = a * b * c.

m mod a = 0
m mod b = 0
m mod c = 0

Hence, we just need to look to consider the number of ugly numbers between:
    (0, m] inclusive is:
    m/a + m/b + m/c

m/a
m/b
m/c

We can also consider then the tuples:

m/(a*b),
m/(b*c),
m/(c*a)

m/(a*b*c) = 1


number of ugly numbers in (0, m]:


is m/a + m/b + m/c - m/(a*b) - m/(b*c) - m/(c*a) - 1

Take the case where a=2,b=3,c=4.

The multiplication is: 2 * 3 * 4 = 24

24/2 + 24/3 + 24/4 - 24/(2*3) - 24/(3*4) - 24/(4*2) - 1 = 12
12 + 8 + 6 - 4 - 2 - 3 - 1 = 16

  1,2,3,o,4,o,5,6,7,o, ,8, o, 9, 10,11,o, 12,o, 13,14,15,o, 16
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24




"""

def kthUglyNumber(a: int, b: int, c: int, target: int) -> int:

    return  target // a + target // b + target // c - target // (a * b) - target // (b * c) - target // (c * a) - target // (a * b * c)

def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:


    l = 0
    r = a * b * c
    while l < r:
        mid = l + (r - l) // 2
        if kthUglyNumber(a, b, c, mid) >= n:
            r = mid
        else:
            l = mid + 1

    return l


