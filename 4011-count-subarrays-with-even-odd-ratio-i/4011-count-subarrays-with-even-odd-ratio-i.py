from bisect import bisect_left

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        pre = 0
        for x in nums:
            pre.append(pre[-1] + (b if x % 2 == 1 else -a))

        last = [-1] * (n + 1)
        p = -1
        for i, x in enumerate(nums):
            if x & 1:
                p = i
            last[i + 1] = p

        vals = sorted(set(pre))
        bit = [0] * (len(vals) + 2)

        def add(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def qry(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        ans = ins = 0
        m = len(vals)

        for r in range(n + 1):
            while ins <= last[r]:
                add(bisect_left(vals, pre[ins]) + 1)
                ins += 1
            idx = bisect_left(vals, pre[r]) + 1
            ans += qry(m) - qry(idx - 1)

        return ans