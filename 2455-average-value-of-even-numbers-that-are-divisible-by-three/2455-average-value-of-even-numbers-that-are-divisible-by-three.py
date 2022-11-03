class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res=0
        c=0
        for i in nums:
            if i%6==0:
                res += i
                c += 1
        return res//c if c !=0 else 0