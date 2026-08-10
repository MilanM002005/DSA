class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, target, path):
            if target == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue

                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        candidates.sort()
        backtrack(0, target, [])

        return ans