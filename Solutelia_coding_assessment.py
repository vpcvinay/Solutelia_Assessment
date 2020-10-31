# -*- coding: utf-8 -*-

def maxSubArray(nums):
    n = len(nums)
    # If the given input is empty, returns zero.
    if(n<1):
        return 0
    # initiates the max value for the sum
    max_sum = nums[0]
    for ele in range(1,n):
        #if the previous sum of elements is greater than the zero, then add 
        # the next element to the sum
        #if the previous sum of elements is less than zero, then start
        # the next subarray from the present element.
        if(nums[ele-1]>0):
            nums[ele] += nums[ele-1]
        
        # find the maximum of the present sum and previous sum. 
        max_sum = max(nums[ele], max_sum)
        
    return max_sum