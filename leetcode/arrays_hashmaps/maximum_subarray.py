"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the subarray with the largest sum, and return its sum.

A subarray is a contiguous non-empty sequence of elements within the array.

Example 1:
Input: nums = [-2,1,-3,4,-1,21,-5,4]
Output: 6
Explanation: The subarray [4,-1,21,-5,4] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= len(nums) <= 10^5
-10^4 <= nums[i] <= 10^4
"""


class Solution:

    '''
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    # Brute force approach
    def maxSubArraySlowest(self, nums: List[int]) -> int:
        max = nums[0]
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s = s + nums[j]
                if max < s:
                    max = s
        return max

    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    # Sliding window approach
    def maxSubArrayMedium(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for val in nums:
            curr_sum = max(0, curr_sum) + val
            max_sum = max(max_sum, curr_sum)
        return max_sum
    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    # Slighly faster than the medium solution
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for val in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += val
            if max_sum < curr_sum:
                max_sum = curr_sum
        return max_sum