import time
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


def raw_exec_time(problem):
    start_time = time.clock()
    dfs_agent(problem)
    print("DFS: " + format(time.clock() - start_time, '.5f') + " seconds")
    
    start_time = time.clock()
    dfs_visited_agent(problem)
    print("DFSV: " + format(time.clock() - start_time, '.5f') + " seconds")

    start_time = time.clock()
    dls_agent(problem, 3)
    print("DLS: " + format(time.clock() - start_time, '.5f') + " seconds")

    start_time = time.clock()
    ids_agent(problem)
    print("IDS: " + format(time.clock() - start_time, '.5f') + " seconds")

    start_time = time.clock()
    bfs_agent(problem)
    print("BFS: " + format(time.clock() - start_time, '.5f') + " seconds")

    start_time = time.clock()
    uniform_cost_agent(problem)
    print("UCS: " + format(time.clock() - start_time, '.5f') + " seconds")


if __name__ == '__main__':
    problem = VacuumWorld((VacuumWorld.LEFT, [VacuumWorld.LEFT, VacuumWorld.RIGHT]))
    
    raw_exec_time(problem)
    
    solution = []
    '''
    dfs_agent(problem, lambda x: solution.append(x))
    print("DFS: ", solution)
    solution = []
    '''
    '''
    dfs_visited_agent(problem, lambda x: solution.append(x))
    print("DFSV: ", solution)
    solution = []
    '''
    '''
    dls_agent(problem, 3, lambda x: solution.append(x))
    print("DLS: ", solution)
    solution = []
    '''
    '''
    ids_agent(problem, lambda x: solution.append(x))
    print("IDS: ", solution)
    solution = []
    '''
    '''
    bfs_agent(problem, lambda x: solution.append(x))
    print("BFS: ", solution)
    solution = []
    '''
    uniform_cost_agent(problem, lambda x: solution.append(x))
    print("UCS: ", solution)
