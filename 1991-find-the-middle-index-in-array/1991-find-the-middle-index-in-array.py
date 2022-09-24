class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        '''n=len(nums)
        if n==1:
            return 0
        p=[0]*(n+2)
        q=[0]*(n+2)
        for i in range(1,n):
            p[i]=p[i-2]+nums[i-1]
        for i in range(n-2,-1,-1):
            q[i]=q[i+1]+nums[i+1]
        for i in range(1,n-1):
            if p[i-1]==q[i+1]:
                return i+1
        return -1'''
        l=0
        r=sum(nums)
        for i in range(0,len(nums)):
            r=r-nums[i]
            if l==r:
                return i
            l=l+nums[i]
        return -1