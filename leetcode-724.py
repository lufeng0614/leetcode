class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return -1
        for i in range(nums_len):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            else:
                if i+1 == nums_len:
                    return -1
                continue


