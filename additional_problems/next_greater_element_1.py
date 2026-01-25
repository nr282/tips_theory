"""
Analysis of the problem.

Stack is used to keep track of the historical numbers in a good manner.
The num used in nums2 will be paired up with the historical numbers.
"""


def nextGreaterElement(nums1, nums2):
    stack = []
    hashmap = {}

    #Looks to correctly model the structure.
    #Look at the historical numbers via the stack.
    #Handles the last element elegantly.
    for num in nums2:
        while stack and num > stack[-1]:
            hashmap[stack.pop()] = num
        stack.append(num)

    return [hashmap.get(i, -1) for i in nums1]



