class Solution:
    def frequencySort(self, s: str) -> str:
        d,ans = {},''
        for i in s:
            if i in d.keys():
                d[i] = d[i]+1
            else:
                d[i] = 1
        d = sorted(d.items(),key = lambda x:x[1],reverse = True)
        for k,v in d:
            ans += k*v
        return ans
        