import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while n>=2**i:
            if n==2**i:
                return True
            i=i+1
        return False
        '''x=math.log(n,2)
        print(x)
        #return isinstance(x,float)
        a=round(x,0)
        if x-a==0:
            return True
        return False'''            
            