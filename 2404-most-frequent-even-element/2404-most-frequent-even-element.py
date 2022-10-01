class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        l=sorted(nums)
        d={}
        for i in l:
            if i&1!=1:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        key = list(d.keys())
        c=0
        ans=-1
        for i in key:
            if d[i]>c:
                ans=i
                c=d[i]
            elif d[i]==c and i<ans:
                ans=i
        return ans
                
        