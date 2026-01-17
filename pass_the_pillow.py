"""

There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially.

Every second, the person holding the pillow passes it to the next person standing in the line.

Once the pillow reaches the end of the line, the direction changes,
and people continue passing the pillow in the opposite direction.


For example, once the pillow reaches the nth person they pass it to the n - 1th person,
then to the n - 2th person and so on. Given the two positive integers n and time,
return the index of the person holding the pillow after time seconds.

Analysis
--------------------------------------------------------------------------------------------

1   2   3   4   5   6   7   8


Solution time is 6 minutes.


"""


from typing import List, Optional

class Solution:
    def passThePillow(self, n: int, time: int) -> int:


        t = 0
        direction = "right"
        person = 1
        while t < time:
            if direction == "right":
                if person == n:
                    direction = "left"
                    person -= 1
                else:
                    person += 1
            else:
                if person == 1:
                    direction = "right"
                    person += 1
                else:
                    person -= 1

            t += 1

        return person





