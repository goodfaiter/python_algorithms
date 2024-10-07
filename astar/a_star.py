from typing import Dict, List
import math

def generate_h_from_2d_grid(current_index, goal_index, total):
    grid_size = math.sqrt(total)
    current_row = current_index / grid_size
    current_col = current_index % grid_size
    goal_row = goal_index / grid_size
    goal_col = goal_index % grid_size
    return math.sqrt(math.pow(goal_row - current_row, 2) + math.pow(goal_col - current_col, 2))

class AStar:
    def __init__(self):
        self._to_visit: Dict[int, float] = dict() # [index, f_score]
        self._visited: Dict[int, (float, float)] = dict() # [index, (f_score, g_score)]

    def solve(self, startIndex: int, goalIndex: int, transitions: Dict[int, Dict[int, float]]) -> (int, int):
        self._to_visit[startIndex] = generate_h_from_2d_grid(startIndex, goalIndex, len(transitions))
        self._visited[startIndex] = (0, 0 + generate_h_from_2d_grid(startIndex, goalIndex, len(transitions)))

        while self._to_visit:
            sorted(self._to_visit, reverse=True)
            current_index, current_f = self._to_visit.popitem()

            if current_index == goalIndex:
                return self._visited[current_index]

            for neighbor_index, transition in transitions[current_index].items():
                g = self._visited[current_index][0] + transition
                h = generate_h_from_2d_grid(neighbor_index, goalIndex, 9)
                f = g + h

                if neighbor_index in self._visited.keys():
                    if g < self._visited[neighbor_index][0]:
                        self._to_visit[neighbor_index] = f
                        self._visited[neighbor_index][0] = g
                        self._visited[neighbor_index][1] = f
                else:
                    self._to_visit[neighbor_index] = f
                    self._visited[neighbor_index] = (g, f)

        return (-1, -1)


if __name__ == "__main__":
    print("Let it begin!")

    # Setup start and goal
    startIndex = 6
    goalIndex = 2

    # Setup transitions
    # 0 - 1 - 2
    # |
    # 3   4   5
    # |       |
    # 5 - 7 - 8
    # each vertex/transition cost 1

    # TODO
    # 1 - generate_h should be an object we pass into AStar
    # 2 - array of f and g should be an object. we are currently storing f twice
    # 3 - add chain of visitation

    transitions = {}
    transitions[0] = {1 : 1, 3 : 1}
    transitions[1] = {0 : 1, 2 : 1}
    transitions[2] = {1 : 1}
    transitions[3] = {0 : 1, 6 : 1}
    transitions[4] = {}
    transitions[5] = {8 : 1}
    transitions[6] = {3 : 1, 7 : 1}
    transitions[7] = {6 : 1, 8 : 1}
    transitions[8] = {7 : 1, 5 : 1}

    astar = AStar()

    print(astar.solve(startIndex, goalIndex, transitions))
