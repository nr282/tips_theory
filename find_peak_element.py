"""
This code is much simpler than my approach for find-peak-element.



"""


from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """


              / - \
             /     \
            /      \
           /       \
          /         \

        """




        # Step 1: Define search space.
        #The index has to be in the array, so the search space is defined
        #to be within the array.

        #We use l and r to represent left and right. the pointers that
        #are used in the search space.
        l = 0
        r = len(nums) - 1

        #We use l < r for consistency. We will exit when l==r.
        #This will be the standard procedure.
        while l < r:

            #We use the representation below because we may encounter overflow
            #otherwise.

            mid = l + (r - l) // 2

            #This is the condition that we will rely on when making the calculations.
            #When looking at the condition provided below, we know that if the mid is larger
            #in value than its right neighbor, then the peak must either be at mid or to
            #the left of mid.

            #Likewise, a key observation in the problem is that the peak element is the first
            #element that is not less than its right neighbor.

            #Hence the condition provided below, provides the correct setup.
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        #         #POSTCONDITION:
        #         #l is the minimum index such that the condition holds
        #         #condition is nums[mid] > nums[mid + 1]
        #         #substituting l in, nums[l] > nums[l + 1].
        return l




if __name__ == "__main__":
    obj = Solution()
    l = obj.findPeakElement([1,2,3,1])