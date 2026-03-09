"""
https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return True if any value appears at least twice in the array,
and return False if every element is distinct.

In other words, determine whether the array contains any duplicate element.

Example 1:
Input: nums = [1,2,3,1]
Output: True

Example 2:
Input: nums = [1,2,3,4]
Output: False

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True

Constraints:
1 <= len(nums) <= 10^5
-10^9 <= nums[i] <= 10^9
"""

'''
Time Complexity: O(n) -> because of the set function
Space Complexity: O(n) -> we create a set to store the elements of the array
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for cur in nums:
            if cur in my_set:
                return True
            else:
                my_set.add(cur)
        return False
    def containsDuplicateFast(self, nums: List[int]) -> bool:
        my_set = set(nums)
        return len(my_set) != len(nums)