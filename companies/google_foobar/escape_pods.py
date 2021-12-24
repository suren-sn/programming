#!/usr/bin/python3

import copy

def get_path(paths, src, dest, parent):
    #BFS
    visited = [False] * len(paths)
    queue = [src]
    visited[src] = True

    while queue:
        p = queue.pop()

        for i,val in enumerate(paths[p]):
            if visited[i] == False and val > 0:
                queue.append(i)
                parent[i] = p
                visited[i] = True
    return visited[dest]

def solution(entrances, exits, _path):
    paths = copy.deepcopy(_path)
    n_rows = len(_path)
    inf = float("inf")

    if len(entrances) > 1:
        n_rows += 1

        for i in range(len(entrances)): entrances[i] += 1
        for i in range(len(exits)): exits[i] += 1

        src = [0] * n_rows
        for e in entrances: src[e] = inf
        for p in paths: p.insert(0,0)
        paths.insert(0,src)

    if len(exits) > 1:
        n_rows += 1
        dest = [0] * n_rows
        for p in paths: p.append(0)
        for e in exits: paths[e][-1] = inf
        paths.append(dest)

    total_fit = 0
    src = 0
    dest = n_rows - 1
    parent = [-1] * n_rows
    while get_path(paths, src, dest, parent):
        #Get max fit in the path
        max_fit = inf
        n = dest
        while n != src:
            max_fit = min(max_fit, paths[parent[n]][n])
            n = parent[n]

        total_fit += max_fit

        #Update capacity of corridors
        n = dest
        while n != src:
            paths[parent[n]][n] -= max_fit
            paths[n][parent[n]] += max_fit
            n = parent[n]

    return total_fit

entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

print(solution(entrances, exits, path))
print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))

