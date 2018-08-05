from blind_search import *

class VacuumWorld:
    LEFT = "Left"
    RIGHT = "Right"
    SUCK = "Suck"    

    actions_list = [LEFT, RIGHT, SUCK]

    def __init__(self, initial_state):
        self.initial_state = initial_state

    def goal_test(self, state):
        return len(state[1]) == 0

    def actions(self, state):
        return self.actions_list

    def result(self, state, action):
        if action == self.SUCK:
            return (state[0], [x for x in state[1] if x != state[0]])
        elif action == self.LEFT:
            return (self.LEFT, state[1])
        else:
            return (self.RIGHT, state[1])

    def step_cost(self, state, action):
        return 1


problem = VacuumWorld((VacuumWorld.LEFT, [VacuumWorld.LEFT, VacuumWorld.RIGHT]))
print(dfs(problem))
print(dfs_visited(problem))
print(dls(problem, 3))
print(ids(problem))
print(bfs(problem))
print(uniform_cost(problem))
