class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = 0
        largest = float('-inf')
        for i, num in enumerate(nums):
            sums += num
            if i >= k:
                sums -= nums[i - k]
            if i >= k - 1:
                largest = max(sums, largest)
        return largest / float(k)
