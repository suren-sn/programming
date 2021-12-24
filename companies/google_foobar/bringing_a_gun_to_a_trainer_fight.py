#!/usr/bin/python3

import math

class Position:
    type_hero = 100
    type_trainer = 200

    def __init__(self, pos_type, dist, direction, x, y):
        self.pos_type = pos_type
        self.dist = dist
        self.direction = direction
        self.x = x
        self.y = y

def get_distance_between_positions(p1, p2):
    #Pythagoras theorem
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5

def get_mirror_pos(box_dimen, pos, box_num):
    if box_num%2 == 0:
        return box_dimen * box_num + pos
    else:
        return box_dimen * (box_num+1) - pos

def get_direction_between_positions(p1,p2):
    return math.atan2(p2[1]-p1[1], p2[0]-p1[0])

def populate_possible_hits(vertex, pos, max_dist, possible_hits, pos_type):
    d = get_distance_between_positions(vertex, pos)
    if d > max_dist:
        return

    direc = get_direction_between_positions(vertex, pos)
    p = Position(pos_type, d, direc, pos[0], pos[1])

    if direc not in possible_hits:
        possible_hits[direc] = p
        return

    if d < possible_hits[direc].dist:
        possible_hits[direc] = p
    return

def solution(dimensions, your_position, trainer_position, distance):
    d = get_distance_between_positions(your_position, trainer_position)
    if d > distance:
        return 0
    if d == distance:
        return 1

    possible_hits = {}

    n_boxes_x = 1 + distance/dimensions[0] + (1 if distance%dimensions[0] > 0 else 0)
    n_boxes_y = 1 + distance/dimensions[1] + (1 if distance%dimensions[1] > 0 else 0)

    for box_x in range(-n_boxes_x, n_boxes_x):
        your_x = get_mirror_pos(dimensions[0], your_position[0], box_x)
        trainer_x = get_mirror_pos(dimensions[0], trainer_position[0], box_x)
        for box_y in range(-n_boxes_y, n_boxes_y):
            your_y = get_mirror_pos(dimensions[1], your_position[1], box_y)
            trainer_y = get_mirror_pos(dimensions[1], trainer_position[1], box_y)

            if [your_x,your_y] != your_position:
                populate_possible_hits(your_position,
                                    [your_x,your_y],
                                    distance,
                                    possible_hits,
                                    Position.type_hero)

            populate_possible_hits(your_position,
                                [trainer_x,trainer_y],
                                distance,
                                possible_hits,
                                Position.type_trainer)

    return len(filter(lambda p: p.pos_type == Position.type_trainer, possible_hits.values()))



print(solution([3,2], [1,1], [2,1], 4))
