graph = {1 : [2,3,4], 2 : [5], 3 : [5], 4 : [], 5:[6,7],6:[],7:[3]}

#DFS(깊이우선 탐색)은 시작점이 있으면, 해당 시작점의 자식으로,
#자식의 자식으로 계속해서 깊게 들어가서 탐색하는 알고리즘
#자식이 없으면 상위 정점으로 이동후 다른 자식으로 탐색..

def dfs(v,visited=[]):
    visited.append(v)
    for i in graph(v):
        if not i in visited:
            visited = dfs(i,visited)
    return print(visited)