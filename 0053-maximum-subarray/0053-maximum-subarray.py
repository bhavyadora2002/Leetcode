class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = csum = nums[0]
        n = len(nums)
        for i in range(1,n):
            # csum += nums[i]
            if csum<0:
                csum = 0
            csum += nums[i]
            ans = max(ans,csum)
        return ans