class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        N = 1
        while N < n:
            N *= 2

        # left, right, prefix, suffix, best, length
        t = [("", "", 0, 0, 0, 0)] * (2 * N)

        for i, c in enumerate(s):
            t[N+i] = (c, c, 1, 1, 1, 1)

        def merge(a, b):
            if not a[5]: return b
            if not b[5]: return a

            l, r, p, q, m, la = a
            L, R, P, Q, M, lb = b
            same = r == L

            return (
                l, R,
                p + P if same and p == la else p,
                q + Q if same and Q == lb else Q,
                max(m, M, q + P if same else 0),
                la + lb
            )

        for i in range(N-1, 0, -1):
            t[i] = merge(t[2*i], t[2*i+1])

        ans = []

        for c, i in zip(queryCharacters, queryIndices):
            p = N + i
            t[p] = (c, c, 1, 1, 1, 1)

            p //= 2
            while p:
                t[p] = merge(t[2*p], t[2*p+1])
                p //= 2

            ans.append(t[1][4])

        return ans