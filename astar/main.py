import math


class Node:
    POS = (0, 0)
    F = 999
    G = 999
    H = 999
    FROM = None

    def __init__(self, x, y, from_=None):
        self.POS = (x, y)
        self.FROM = from_

    def __eq__(self, other):
        return self.POS == other.POS

    def __ne__(self, other):
        return self.POS[0] != other.POS[0] or self.POS[1] != other.POS[1]

    def __gt__(self, other):
        return self.F > other.F

    def __ge__(self, other):
        return self.F >= other.F

    def __lt__(self, other):
        return self.F < other.F

    def __le__(self, other):
        return self.F <= other.F

    def straight_to(self, other):
        if (self.POS[0] - other.POS[0]) ** 2 + (self.POS[1] - other.POS[1]) ** 2 == 2:
            return False
        else:
            return True

    def is_near_by(self, other):
        if (self.POS[0] - other.POS[0]) ** 2 + (self.POS[1] - other.POS[1]) ** 2 <= 2:
            return True
        else:
            return False


class StartNode(Node):
    F = 0
    G = 0
    H = 0


class PathNotFoundError(Exception):
    pass


def a_star(start_pos, end_pos, map_: list):
    open_list = [start_pos]
    close_list = []
    """start search"""
    start_pos.G = 0
    start_pos.H = _distance(start_pos, end_pos)
    start_pos.F = start_pos.H

    while len(open_list) != 0:
        x = lowest_f_in(open_list)
        if x == end_pos:
            print('Found path!')
            return construct_route(end_pos)
        open_list.remove(x)
        close_list.append(x)
        for y in neighbor_of(x, map_):
            if y in close_list:
                continue
            guess_g = x.G + _real_distance(x, y)
            if y not in open_list:
                guess_better = True
            elif guess_g < y.G:
                guess_better = True
            else:
                guess_better = False
            if guess_better:
                print(f'from {x.POS} to {y.POS}')
                y.FROM = x
                y.G = guess_g
                y.H = _distance(y, end_pos)
                y.F = y.G + y.H
                open_list.append(y)
            if y == end_pos:
                end_pos = y
    raise PathNotFoundError()


def construct_route(end_pos):
    route = [end_pos]
    previous = end_pos.FROM
    while previous is not None:
        route.append(previous)
        previous = previous.FROM
    route.reverse()
    return route


def lowest_f_in(open_list: list) -> Node:
    min_node = open_list[0]
    for n in open_list:
        if n < min_node:
            min_node = n
    return min_node


def neighbor_of(x: Node, map_):
    neighbor = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            try:
                if map_[x.POS[0] + x_offset][x.POS[1] + y_offset] == 0:
                    if not(x_offset == 0 and y_offset == 0):
                        if x.POS[0] + x_offset >= 0 and x.POS[1] + y_offset >= 0:
                            neighbor.append(Node(x.POS[0] + x_offset, x.POS[1] + y_offset))
            except IndexError:
                pass
    return neighbor


def _distance(a: Node, b: Node):
    return math.sqrt((a.POS[0] - b.POS[0]) ** 2 + (a.POS[1] - b.POS[1]) ** 2)


def _real_distance(a: Node, b: Node):
    d = (a.POS[0] - b.POS[0]) ** 2 + (a.POS[1] - b.POS[1]) ** 2
    if d >= 2:
        return 1.4
    else:
        return 1


def print_node_list(l: list):
    for n in l:
        print(n.POS, end=' ')
    print()


def main():
    exam_map = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1]
    ]
    '''
    exam_map = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    '''
    start_pos = StartNode(0, 0)
    end_pos = Node(5, 2)
    route = a_star(start_pos, end_pos, exam_map)
    print_node_list(route)


if __name__ == '__main__':
    main()
