from readFile import load_input


MAX = 10000
adj = [[0 for i in range(MAX)] for j in range(MAX)]
adjInv = [[0 for i in range(MAX)] for j in range(MAX)]
visited = [None for i in range(MAX)]
visitedInv = [None for i in range(MAX)]
s = []
scc = [0 for i in range(MAX)]
counter = 1


def addEdges(a, b):
    adj[a].append(b)


def addEdgesInverse(a, b):
    adjInv[b].append(a)


def dfsFirst(u):
    if visited[u]:
        return
    visited[u] = True
    for i in range(len(adj[u])):
        dfsFirst(adj[u][i])
    s.append(u)


def dfsSecond(u):
    if visitedInv[u]:
        return
    visitedInv[u] = True
    for i in range(len(adjInv[u])):
        dfsSecond(adjInv[u][i])
    scc[u] = counter


def is2Satisfiable(n, m, a, b):
    global counter
    for i in range(m):
        if a[i] > 0 and b[i] > 0:
            addEdges(a[i] + n, b[i])
            addEdgesInverse(a[i] + n, b[i])
            addEdges(b[i] + n, a[i])
            addEdgesInverse(b[i] + n, a[i])
        elif a[i] > 0 and b[i] < 0:
            addEdges(a[i] + n, n - b[i])
            addEdgesInverse(a[i] + n, n - b[i])
            addEdges(-b[i], a[i])
            addEdgesInverse(-b[i], a[i])
        elif a[i] < 0 and b[i] > 0:
            addEdges(-a[i], b[i])
            addEdgesInverse(-a[i], b[i])
            addEdges(b[i] + n, n - a[i])
            addEdgesInverse(b[i] + n, n - a[i])
        else:
            addEdges(-a[i], n-b[i])
            addEdgesInverse(-a[i], n-b[i])
            addEdges(-b[i], n-a[i])
            addEdgesInverse(-b[i], n-a[i])

    for i in range(1, (2*n) + 1):
        if not visited[i]:
            dfsFirst(i)

    while len(s) > 0:
        top = s[-1]
        s.remove(s[-1])
        if not visitedInv[top]:
            dfsSecond(top)
            counter += 1

    for i in range(1, n+1):
        if scc[i] == scc[i + n]:
            return "Unsatisfiable"
    return "Satisfiable"
