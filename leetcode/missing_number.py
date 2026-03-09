"""
https://leetcode.com/problems/missing-number/
Given an array nums containing n distinct numbers taken from the range [0, n],
return the one number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number because it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number because it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number because it does not appear in nums.

Constraints:
n == len(nums)
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
"""

class Solution:
    # Using sorted list and set difference
    '''
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    '''
    def missingNumberSlowest(self, nums: List[int]) -> int:
        my_sorted_list = sorted(nums)
        n = len(nums)
        my_range = range(n + 1)
        my_set = set()
        
        if my_sorted_list == my_range:
            return n + 1
        else:
            for cur in my_range:
                if cur not in nums:
                    return cur

    # Using for loop
    '''
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    def missingNumberSlow(self, nums: List[int]) -> int:
        n = len(nums)
        for cur in range(n + 1):
            if cur not in nums:
                return cur
        return n + 1
    # Using set difference
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (set(range(n + 1)) - set(nums)).pop()