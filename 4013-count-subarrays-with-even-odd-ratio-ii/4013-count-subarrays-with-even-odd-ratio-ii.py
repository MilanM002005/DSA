class Solution:
    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        s = 0
        p = [0]
        for x in nums:
            s += b if x % 2 == 0 else -a
            p.append(s)
        sorted_p = sorted(set(p))
        v = {x: idx + 1 for idx, x in enumerate(sorted_p)}
        bit = [0] * (len(v) + 1)

        def add(idx):
            while idx < len(bit):
                bit[idx] += 1
                idx += idx & -idx
        def query(idx):
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res
        ans = 0
        inserted_up_to = 0
        total_inserted = 0

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                while inserted_up_to <= i:
                    add(v[p[inserted_up_to]])
                    total_inserted += 1
                    inserted_up_to += 1

            rank = v[p[i + 1]]
            ans += total_inserted - query(rank - 1)

        return ans