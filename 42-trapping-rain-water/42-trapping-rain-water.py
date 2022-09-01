class Solution:
    def trap(self, height: List[int]) -> int:
        s=0
        n=len(height)
        a=[0]*n
        b=[0]*n
        a[0]=height[0]
        b[n-1]=height[n-1]
        for i in range(1,n):
            a[i]=(max(a[i-1],height[i]))
        for i in range(n-2,-1,-1):
            b[i]=(max(b[i+1],height[i]))
        for i in range(n):
            s=s+min(a[i],b[i])-height[i]
        return s
            