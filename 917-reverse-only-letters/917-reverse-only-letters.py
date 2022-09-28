class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while i<j and i<len(s) and j>0:
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i=i+1
                j=j-1
            elif s[i].isalpha() and not s[j].isalpha():
                j=j-1
            elif s[j].isalpha() and not s[i].isalpha():
                i=i+1
            else:
                i=i+1
                j=j-1
        return "".join(s)
                
            
        