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


def a_star(start_pos, end_pos, map_: list):
    open_list = []
    close_list = []
    """start search"""
    close_list.append(start_pos)
    next_node = start_pos
    while next_node != end_pos:
        _search_neighbor(map_, next_node, open_list, close_list)
        for n in open_list:
            print(n.POS, n.F, end=' ')
        print()
        next_node = _next_step(next_node, end_pos, open_list, close_list)
        print(next_node.POS)
        end_pos.FROM = next_node
    previous_node = end_pos.FROM
    route = []
    while previous_node is not None:
        route.append(previous_node.POS)
        previous_node = previous_node.FROM
    route.reverse()
    return route


def _search_neighbor(map_: list, now: Node, open_list: list, close_list: list):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if now.POS[0] + x >= 0 and now.POS[1] + y >= 0 and map_[now.POS[0] + x][now.POS[1] + y] == 0:
                t = Node(now.POS[0] + x, now.POS[1] + y, now)
                if t not in open_list and t not in close_list and t != now:
                    open_list.append(t)


def _next_step(from_: Node, end_pos: Node, open_list: list, close_list: list) -> Node:
    min_node = None
    for node in open_list:
        if node.is_near_by(from_):
            g = from_.F + 1 if node.straight_to(from_) else from_.F + 1.4
            h = _distance(node, end_pos)
            f = g + h
            if f <= node.F:
                node.G = g
                node.H = h
                node.F = f
                node.FROM = from_
                min_node = node
            else:
                min_node = node
    for node in open_list:
        if node.FROM == from_ and node < min_node:
            min_node = node
    close_list.append(min_node)
    open_list.remove(min_node)
    # open_list.remove(from_)
    return min_node


def _distance(a: Node, b: Node):
    return round(math.sqrt((a.POS[0] - b.POS[0]) ** 2 + (a.POS[1] - b.POS[1]) ** 2), 5)


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
    print(route)


if __name__ == '__main__':
    main()
