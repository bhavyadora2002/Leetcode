from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        li = []
        c = []
        ans = []
        words = sorted(words)
        for i in words:
            if i not in li:
                li.append(i)
                c.append(words.count(i))
            else:
                continue
        i=k
        while i!=0:
            m=max(c)
            idx=c.index(m)
            ans.append(li[idx])
            c[idx]=0
            i=i-1
        return ans