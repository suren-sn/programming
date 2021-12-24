#!/usr/bin/python3

def is_version_lesser_recursion (v1, v2):
    #if v1 < v2 return True, else return False
    n1 = int(v1[0])
    n2 = int(v2[0])

    if n1 < n2: return True
    if n1 > n2: return False

    if len(v1) == 1: return True
    if len(v2) == 1: return False

    return is_version_lesser_recursion (v1[1:],v2[1:])

def is_version_lesser(v1, v2):
    #if v1 < v2 return True, else return False
    return is_version_lesser_recursion (v1.split('.'), v2.split('.'))

def solution(l):
    #Selection sort
    for i in range(len(l)-1):
        min_idx = i
        for j in range(i+1,len(l)):
            if is_version_lesser (l[j], l[min_idx]):
                min_idx = j
        #Swap
        swap = l[i]
        l[i] = l[min_idx]
        l[min_idx] = swap

    return l

print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
