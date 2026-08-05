class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for a, b in invocations:
            graph[a].append(b)
            indegree[b] += 1

        stack = []
        stack.append(k)
        visited = [False] * n
        visited[k] = True

        while stack:
            node = stack.pop()

            for child in graph[node]:
                if not visited[child]:
                    visited[child] = True
                    stack.append(child)
                
                indegree[child] -= 1

        for node in range(n):
            if visited[node]:
                if indegree[node] > 0:
                    return list(range(n))

        return [node for node in range(n) if not visited[node]]