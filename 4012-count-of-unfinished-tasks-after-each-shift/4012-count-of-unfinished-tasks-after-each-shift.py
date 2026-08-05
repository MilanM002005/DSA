from bisect import bisect_right
from typing import List

class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        pref = [0] * (n + 1)
        for k in range(n):
            pref[k + 1] = pref[k] + tasks[k]

        ans = []
        i = 0
        rem = 0 
        for t in shifts:
            if i == n:
                i = 0
                rem = 0
            if rem > 0:
                if t < rem:
                    rem -= t
                    t = 0
                else:
                    t -= rem
                    rem = 0
                    i += 1
            if t > 0 and i < n:
                j = bisect_right(pref, t + pref[i]) - 1
                
                if j == n:
                    i = n
                    rem = 0
                else:
                    t_left = t - (pref[j] - pref[i])
                    i = j
                    rem = tasks[j] - t_left

            ans.append(n - i)

        return ans