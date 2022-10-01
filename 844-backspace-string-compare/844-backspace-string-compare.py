class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l = []
        li = []
        for i in s:
            if i != '#':
                l.append(i)
            elif len(l)>0:
                l.pop()
        for i in t:
            if i != '#':
                li.append(i)
            elif len(li)>0:
                li.pop()
        return l==li