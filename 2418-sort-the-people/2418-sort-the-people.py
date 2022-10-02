class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        des = sorted(heights,reverse = True)
        l = []
        for i in des:
            l.append(names[heights.index(i)])
        return l
        