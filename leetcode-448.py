class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        else:
            m = max(nums)
            l = len(nums)
            b = [i for i in range(1,max([m,l])+1)]
            c = list(set(b).difference(set(nums)))
            return c
            
===========================================================
 class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:   
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [idx + 1 for idx, num in enumerate(nums) if num > 0]

