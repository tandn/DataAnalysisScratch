'''
source: https://www.geeksforgeeks.org/maximum-absolute-difference-between-sum-of-two-contiguous-sub-arrays/
Given an array of integers, find two non-overlapping contiguous sub-arrays
such that the absolute difference between the sum of two sub-arrays is maximum.

Input: [-2, -3, 4, -1, -2, 1, 5, -3]
Output: 12
Two subarrays are [-2, -3] and [4, -1, -2, 1, 5]


[1,9,5,1,4,9]
'''

def max_sum_difference(arr):
    n=len(arr)
    if n == 1:
        return 0
    if n==2:
        return abs(arr[0]-arr[1])
    dp=[0] * n
    for i in range(1,n-1): #arr[:i] arr[i+1:]
