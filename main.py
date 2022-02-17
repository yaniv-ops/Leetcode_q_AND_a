
"""///

1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


///"""


class Solution:
    def twoSum(self, nums, target):
        list = nums
        list_to_return = []
        result = 1000
        for item in range(len(list)):
            for bacon in range(item+1, len(list)):
                calculate = abs(target - (list[item] + list[bacon]))
                if calculate <= result:
                    result = calculate
                    list_to_return = [item, bacon]
        return list_to_return


a = Solution()

b = a.twoSum(nums = [2,7,11,15], target=40)

print(b)
