class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        l=[]
        l2=[]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if i/j not in l2:
                    l2.append(i/j)
                    l.append(str(i)+'/'+str(j))
        return l
