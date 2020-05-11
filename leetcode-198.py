class Solution(object):
    def rob(self, nums):
        """
        :param nums:
        :return:
        """
        # 运用动态规划求解
        if len(nums) == 0:
            return 0
        # 子问题：
        # f(k) = 偷[0..k)房间中的最大金额

        # f(0) = 0
        # f(1) = nums[0]
        # f(k) = max{f(k-1),nums[k-1]+rob(k-2)}

        N = len(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N+1):
            dp[k] = max(dp[k - 1], nums[k - 1] + dp[k - 2])
        return dp[N]

========================================================================
方法二：

def rob(self, nums: List[int]) -> int:
    prev = 0
    curr = 0
    
    # 每次循环，计算“偷到当前房子为止的最大金额”
    for i in nums:
        # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
        # dp[k] = max{ dp[k-1], dp[k-2] + i }
        prev, curr = curr, max(curr, prev + i)
        # 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]

    return curr





if __name__ == '__main__':
    print("leet code 198 ")
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
