#!/usr/bin/python3

class Bombs:
    def __init__(self, m, f, rep_count=0):
        self.m = m
        self.f = f
        self.rep_count = rep_count

def isBombCountValid (m_exp, f_exp, m, f):
    if m > m_exp or f > f_exp:
        return False
    return True

def solution1(x_str, y_str):
    if (x_str,y_str) == ('1','1'): return '0'

    x = int(x_str)
    y = int(y_str)

    #Breadth first search
    root = Bombs(1,1)
    q = [root]

    while len(q):
        b = q.pop(0)

        possibilities = []

        #Replicate using M
        m = b.m
        f = b.f + b.m
        possibilities.append((m,f))

        #Replicate using F
        m = b.m + b.f
        f = b.f
        possibilities.append((m,f))

        rep_count = b.rep_count + 1
        for m,f in possibilities:
            if (m,f) == (x,y):
                return str(rep_count)

            if isBombCountValid(x,y,m,f):
                q.append(Bombs(m, f, rep_count))
    return "impossible"

def solution(x_str, y_str):
    x = int(x_str)
    y = int(y_str)
    rep_count = 0
    while (x>0) and (y>0) and (x!=y):
        if x>y:
            count = int(x/y) - 1
            if count==0: count=1
            x = x-y*count
        else:
            count = int(y/x) - 1
            if count==0: count=1
            y = y-x*count
        rep_count += count

    if x==1 and y==1:
        return str(rep_count)
    return "impossible"


#print(type(solution('2','1')))
print ("--------------------1")
print(solution('2','1'))
print ("--------------------4")
print(solution('4','7'))
print ("--------------------impossible")
print(solution('2','4'))
print ("--------------------0")
print(solution('1','1'))
print ("--------------------5")
print(solution('4','9'))
print ("--------------------long")
print(solution(str(10**50),str(10**50)))
print ("--------------------long1")
print(solution('1',str(10**50)))
