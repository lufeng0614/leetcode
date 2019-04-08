

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

====================================================================================
我的 超出时间限制
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        init = nums[0]
        len_nums = len(nums)
        for x in range(len_nums):
            for j in range(x+1, len_nums+1):
                temp = (sum(nums[x:j]))
                if temp > init:
                    init = temp

        return init
            
==================================================================================


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for x in range(1, len(nums)):
            nums[x] = nums[x] + max(nums[x-1], 0) # =============================

        return max(nums)
 # 理解为思想是动态规划，nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和。
# 如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和
