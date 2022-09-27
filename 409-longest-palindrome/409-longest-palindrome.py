class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=0
        f=0
        e=0
        l=[]
        '''if len(set(s))==1:
            return len(s)'''
        for i in s:
            if s.count(i)%2==0 and i not in l:
                c+=s.count(i)
                l.append(i)
            elif s.count(i)%2==1 and i not in l:
                e=e+s.count(i)-1
                f=1
                l.append(i)
        if f==1:
            return c+e+1
        return c
        