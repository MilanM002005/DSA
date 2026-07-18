class Solution:
    def beautifulArray(self, N):
        
            if N == 1: 
                return [1]
            odd= self.beautifulArray((N+1)//2)
            even=self.beautifulArray(N//2)
            ans=[]
            for i in odd:
                ans.append(2*i-1)
            for i in even:
                ans.append(2*i)
            return ans
