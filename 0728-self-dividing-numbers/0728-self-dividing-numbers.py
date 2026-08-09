class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for n in range(left, right + 1):
            x = n
            while x:
                d = x % 10

                if d == 0 or n % d:
                    break

                x //= 10
            else:
                ans.append(n)
        return ans