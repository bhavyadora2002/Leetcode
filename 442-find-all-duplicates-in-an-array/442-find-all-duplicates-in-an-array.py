class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        c = 0
        ans = []
        n = len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                ans.append(nums[i])
        return ans