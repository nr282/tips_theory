"""
In this module, I examine the theory behind the binary search.

#Define the search space.
#Use the template.
#Analyze whether is a: lower or upper bound problem
#Upper bound versus lower bound is useful when we have duplicates in the array.
#Find greatest duplicate element in the array.
#Find smallest duplicate element in the array.



def function(nums, i, j):
    while i < j:
        if condition(i,j) is true:
            r = mid
        else:
            l = mid + 1
    
    return mid


The reason that (1) Upper Bound or Lower Bound matters is for when
there are duplicates in the target array that we are iterating over.


Write out the post conditions.

POST CONDITION: left is minimum such that target <= nums[left].
the exiting l==r, is the [x,y], x=l in the value here.



Information related to binary search.
    - Inherently, there is a question about when to use binary search
        - Whenever a certain evaluation, can quickly reduce part of the search
        space then, that will be very useful.
        -


"""