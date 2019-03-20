题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

==================================================================================================

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}  # 关键
        for x, num in enumerate(nums):
            result = target - num
            # hashmap[num] = x 如果在这个位置会导致重复利用相同元素
            if result in hashmap:
                return [hashmap[result], x]
            hashmap[num] = x  # 关键  
            
# 以下代码运算超时        
#         for x, num in enumerate(nums): 
#             for y, other in enumerate(nums[(x+1):]):
#                 if ((num + other) == target):
#                         return [x, x+1+y]

        
