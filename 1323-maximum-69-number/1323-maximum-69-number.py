class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == '6':
                c = i
                break
        return int(s[0:i]+'9'+s[i+1:])