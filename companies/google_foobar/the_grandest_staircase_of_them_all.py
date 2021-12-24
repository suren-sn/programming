#!/usr/bin/python3

def get_staircase_variations1(nbricks, max_height):
    if nbricks <= 0: return 1
    if max_height <= 0: return 0

    max_possible_height = max_height if max_height < nbricks else nbricks

    variations = 0
    for i in range(max_possible_height, 0, -1):
        variations += get_staircase_variations1(nbricks-i, i-1)
    return variations

def solution1(n):
    return get_staircase_variations1(n,n) - 1

def get_staircase_variations(nbricks, max_height, visited=None):
    if nbricks <= 0: return 1
    if max_height <= 0: return 0

    if not visited:
        visited = {}

    max_possible_height = max_height if max_height < nbricks else nbricks

    variations = 0
    for i in range(max_possible_height, 0, -1):
        #Form a step with i bricks
        remaining_bricks = nbricks - i
        next_step_max_height = i-1
        if next_step_max_height > remaining_bricks:
            next_step_max_height = remaining_bricks

        if remaining_bricks not in visited.keys():
            visited[remaining_bricks] = {}
        if next_step_max_height not in visited[remaining_bricks].keys():
            visited[remaining_bricks][next_step_max_height] = get_staircase_variations(remaining_bricks, next_step_max_height, visited)

        variations += visited[remaining_bricks][next_step_max_height]
    return variations

def solution(n):
    return get_staircase_variations(n,n) - 1


print("------------------0")
print(solution(0))
print("------------------0")
print(solution(1))
print("------------------0")
print(solution(2))
print("------------------1")
print(solution(3))
print("------------------1")
print(solution(4))
print("------------------2")
print(solution(5))
print("------------------3")
print(solution(6))
print("------------------4")
print(solution(7))
print("------------------9")
print(solution(10))
print("------------------487067745")
print(solution(200))



#
#  #
#  #  #  #
#  #  #  #   #  #
#  #  #  #   #  #   #   #
#  #  #  #   ## #   ##  #   #
#  #  ## #   ## ##  ##  ##  ##
#  ## ## ##  ## ##  ##  ### ###
## ## ## ### ## ### ### ### ####
#n=10,possibilities=9





