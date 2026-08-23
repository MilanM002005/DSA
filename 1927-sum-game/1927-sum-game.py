class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2

        nums = [
            9 if ch == '?' else 2 * int(ch)
            for ch in num
        ]

        return sum(nums[:n]) != sum(nums[n:])