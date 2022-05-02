import copy
import math
import random


# https://www.geeksforgeeks.org/2-satisfiability-2-sat-problem/amp/


MAX = 1000
adj = [[0 for i in range(MAX)] for j in range(MAX)]
adjInv = [[0 for i in range(MAX)] for j in range(MAX)]
visited = [None for i in range(MAX)]
visitedInv = [None for i in range(MAX)]
s = []
scc = [0 for i in range(MAX)]
counter = 1


def add_edges(a, b):
    adj[a].append(b)


def add_edges_inverse(a, b):
    adjInv[b].append(a)


def dfs_first(u):
    if visited[u]:
        return
    visited[u] = True
    for i in range(len(adj[u])):
        dfs_first(adj[u][i])
    s.append(u)


def dfs_second(u):
    if visitedInv[u]:
        return
    visitedInv[u] = True
    for i in range(len(adjInv[u])):
        dfs_second(adjInv[u][i])
    scc[u] = counter


def is2_satisfiable(n, m, a, b):
    global counter, s
    for i in range(m):
        if a[i] > 0 and b[i] > 0:
            add_edges(a[i] + n, b[i])
            add_edges_inverse(a[i] + n, b[i])
            add_edges(b[i] + n, a[i])
            add_edges_inverse(b[i] + n, a[i])
        elif a[i] > 0 and b[i] < 0:
            add_edges(a[i] + n, n - b[i])
            add_edges_inverse(a[i] + n, n - b[i])
            add_edges(-b[i], a[i])
            add_edges_inverse(-b[i], a[i])
        elif a[i] < 0 and b[i] > 0:
            add_edges(-a[i], b[i])
            add_edges_inverse(-a[i], b[i])
            add_edges(b[i] + n, n - a[i])
            add_edges_inverse(b[i] + n, n - a[i])
        else:
            add_edges(-a[i], n - b[i])
            add_edges_inverse(-a[i], n - b[i])
            add_edges(-b[i], n - a[i])
            add_edges_inverse(-b[i], n - a[i])

    for i in range(1, (2 * n) + 1):
        if not visited[i]:
            dfs_first(i)

    while len(s) > 0:
        top = s[-1]
        s.remove(s[-1])
        if not visitedInv[top]:
            dfs_second(top)
            counter += 1

    for i in range(1, n + 1):
        if scc[i] == scc[i + n]:
            return "Unsatisfiable", None

    solutions = [None for i in range(n+1)]
    for i in range(1, n+1):
        if scc[i] == scc[i + n]:
            return False
        solutions[i] = True if scc[i] > scc[i + n] else False

    return "Satisfiable", solutions[1:n+1]
