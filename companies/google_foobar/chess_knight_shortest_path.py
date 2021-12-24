#!/usr/bin/python3

from queue import Queue

class Cell:
    def __init__(self, row, col, deapth=0):
        self.row = row
        self.col = col
        self.deapth = deapth

def isValidMove (r, c, board_size):
    if r<0 or c<0 or r>=board_size or c>=board_size:
        return False
    return True

def solution(src, dest):
    if src == dest:
        return 0

    board_size = 8

    srow = int(src/board_size)
    scol = src%board_size
    drow = int(dest/board_size)
    dcol = dest%board_size

    possible_moves = (
        (2,1)
        ,(2,-1)
        ,(-2,1)
        ,(-2,-1)
        ,(1,2)
        ,(-1,2)
        ,(1,-2)
        ,(-1,-2))

    # Using Breadth first search
    q = Queue(maxsize=board_size**2)
    visited = []

    root = Cell(srow,scol)
    q.put(root)
    visited.append((root.row,root.col))

    while not q.empty():
        cell = q.get()

        for prow,pcol in possible_moves:
            r = cell.row + prow
            c = cell.col + pcol
            if isValidMove(r,c,board_size) and (r,c) not in visited:
                if r==drow and c==dcol:
                    return cell.deapth + 1
                visited.append((r,c))
                q.put(Cell(r,c,cell.deapth+1))

    return -1

print(solution(0,1))
print(solution(19,36))
