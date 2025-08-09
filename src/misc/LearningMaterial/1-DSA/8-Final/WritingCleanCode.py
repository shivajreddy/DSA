# The bad code.

"""
Following PEP-8 guide

"""


class NetworkNode:  # class names must me in camel
    def __init__(self, input_type: str, value: int):  # type is a reserved keyword
        self.input_type = input_type
        self.value = value


def check_connected(grid: list[list[NetworkNode]], max_diff: int) -> bool:
    good_nodes = set()  # consistent with naming: class names-> CamelCase,
    todo_node_q = [(0, 0)]

    while len(todo_node_q) > 0:
        curr_node = todo_node_q.pop()
        if (curr_node[0], curr_node[1]) not in good_nodes:
            good_nodes.add((curr_node[0], curr_node[1]))
            if (curr_node[0], curr_node[1]) == (len(grid) - 1, len(grid[0]) - 1):
                return True

            if 0 <= curr_node[0] + 1 and curr_node[0] + 1 < len(grid):
                cur_Node = grid[curr_node[0]][curr_node[1]]
                nodeplusOne_toX = grid[curr_node[0] + 1][curr_node[1]]
                if nodeplusOne_toX.type == cur_Node.type:
                    good_nodes.add((curr_node[0] + 1, curr_node[1]))
                    todo_node_q.append((curr_node[0] + 1, curr_node[1]))

                elif abs(cur_Node.value - nodeplusOne_toX.value) <= max_diff:
                    good_nodes.add((curr_node[0] + 1, curr_node[1]))
                    todo_node_q.append((curr_node[0] + 1, curr_node[1]))

            if 0 <= curr_node[0] - 1 and curr_node[0] - 1 < len(grid):
                cur_Node = grid[curr_node[0]][curr_node[1]]
                nodeMinusOne_toX = grid[curr_node[0] - 1][curr_node[1]]
                if nodeMinusOne_toX.type == cur_Node.type:
                    good_nodes.add((curr_node[0] - 1, curr_node[1]))
                    todo_node_q.append((curr_node[0] - 1, curr_node[1]))

                elif abs(cur_Node.value - nodeMinusOne_toX.value) <= max_diff:
                    good_nodes.add((curr_node[0] - 1, curr_node[1]))
                    todo_node_q.append((curr_node[0] - 1, curr_node[1]))

            if 0 <= curr_node[1] - 1 and curr_node[0] - 1 < len(grid)[0]:
                cur_Node = grid[curr_node[0]][curr_node[1]]
                nodeMinusOne_toY = grid[curr_node[0]][curr_node[1] - 1]
                if nodeMinusOne_toY.type == cur_Node.type:
                    good_nodes.add((curr_node[0], curr_node[1] - 1))
                    todo_node_q.append((curr_node[0], curr_node[1] - 1))

                elif abs(cur_Node.value - nodeMinusOne_toY.value) <= max_diff:
                    good_nodes.add((curr_node[0], curr_node[1] - 1))
                    todo_node_q.append((curr_node[0], curr_node[1] - 1))

            if 0 <= curr_node[1] + 1 and curr_node[0] + 1 < len(grid)[0]:
                cur_Node = grid[curr_node[0]][curr_node[1]]
                nodePlusOne_toY = grid[curr_node[0]][curr_node[1] + 1]
                if nodePlusOne_toY.type == cur_Node.type:
                    good_nodes.add((curr_node[0], curr_node[1] + 1))
                    todo_node_q.append((curr_node[0], curr_node[1] + 1))

                elif abs(cur_Node.value - nodePlusOne_toY.value) <= max_diff:
                    good_nodes.add((curr_node[0], curr_node[1] + 1))
                    todo_node_q.append((curr_node[0], curr_node[1] + 1))

    if (len(grid) - 1, len(grid[0]) - 1) in good_nodes:
        return True

    return False
