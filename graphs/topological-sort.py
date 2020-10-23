def topologicalSort(edges, V):
    adj = [[] for _ in range(V)]
    visited = [False for _ in range(V)]
    stack = []

    for x, y in edges:
        adj[x].append(y)

    def topologicalUtil(curr):
        visited[curr] = True

        for x in adj[curr]:
            if not visited[x]:
                topologicalUtil(x)
            else:
                print('its not topological sort')
        stack.append(curr)

    for i in range(V):
        if not visited[i]:
            topologicalUtil(i)
    
    stack.reverse()
    print(stack)

def driver():
    edges = [[0,1],[0,5],[1,7],[3,2],[3,8],[3,4],[4,8],[6,0],[6,1],[8,2],[9,4]]
    V = 10
    topologicalSort(edges, V)


if __name__ == "__main__":
    driver()