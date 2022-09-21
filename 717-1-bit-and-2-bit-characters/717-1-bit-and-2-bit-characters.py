class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        flag=0
        while i<len(bits):
            if bits[i]==1:
                i=i+2
                flag=0
            else:
                i=i+1
                flag=1
        return flag==1