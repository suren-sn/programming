#!/usr/bin/python3

def get_xor(n):
    mod = n%4
    if mod == 0: return n
    if mod == 3: return 0
    if mod == 2: return n+1
    if mod == 1: return 1

def solution(start, length):
    checksum = 0
    for i in range(length):
        line_start = (start + i*length)
        line_end = line_start + length-i-1
        line_checksum = get_xor(line_start-1) ^ get_xor(line_end)
        #print("line_start:%s  line_end:%s  st_xor:%s end_xor:%s line_xor:%s"%(line_start,line_end,get_xor(line_start-1),get_xor(line_end),line_checksum))
        checksum = checksum ^ line_checksum
        #for j in range(length-i):
        #    checksum = checksum ^ (start + i*length + j)
    return checksum

print(solution(0,3))
print(solution(17,4))

print(solution(2,1))
#print(solution(10,0))
print(solution(2000000000,1))
print(solution(0,2000000))
