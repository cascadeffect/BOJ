import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * 9

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

dfs(graph, 1, visited)