class Solution:
    def containsNearbyDuplicate(self, n: List[int], k: int) -> bool:
        '''i,j,l=0,1,len(n)
        while j<l:
            if(j-i<=k and n[i]==n[j]):
                return True
            if j-i<k:
                if j!=l:
                    j+=1
                else:
                    i=i+1
                    j=j+1
            else:
                i=i+1
                j=i+1
                
        return False
        if k==0:
            return False
        l=len(n)
        j=1
        for i in range(l):
            j=i+1
            while j<l:
                if(abs(j-i)<=k and n[i]==n[j]):
                    return True
                j=j+1
        return False'''
        l=len(n)
        d={}
        for i in range(l):
            if n[i] not in d:
                d[n[i]]=i
            else:
                if d[n[i]]!=i and abs(d[n[i]]-i)<=k:
                    return True
                else:
                    d[n[i]]=i
        return False
            