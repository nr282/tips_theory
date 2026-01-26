"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:
    s = "leeEetcode"
    s = "leetcode"

Example 2:
    s = "leeEEtcode"
    s = "leetcode"

Example 3
    s = "abcCBA"
    s = ""
"""

from collections import deque
def makeGood(s: str) -> str:

    n = len(s)
    stack = deque([])
    for i in range(n):

        if i == 0:
            stack.append(s[i])
        else:
            if (s[i] != stack[-1]) and (s[i].upper() == stack[-1].upper()):
                stack.pop()
            else:
                stack.append(s[i])

    stack_n = len(stack)
    res = [None for i in range(stack_n)]
    for i in range(stack_n):
        res[stack_n - i - 1] = stack.pop()

    return "".join(res)


def tests():

    s = "abcCBA"
    res = makeGood(s)
    assert(res=="")

    s = "leeEEtcode"
    res = makeGood(s)
    assert(res == "ltcode")


if __name__ == "__main__":

    tests()