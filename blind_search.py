class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost
        i


def bfs(problem):
    node = Node(state = problem.initial_state, path_cost = 0)
    if problem.goal_test(node.state):
        return __solution(node)
    frontier = [node]
    explored = []
    while True:
        if len(frontier) == 0:
            raise Exception('Failure')
        node = frontier.pop(0)
        explored.append(node.state)
        for action in problem.actions(node.state):
            child = __child_node(problem, node, action)
            if not (child.state in explored and any(x for x in frontier if x.state == child.state)):
                if problem.goal_test(child.state):
                    return __solution(child)
                frontier.append(child)


def uniform_cost(problem):
    node = Node(state = problem.initial_state, path_cost = 0)
    frontier = [node]
    explored = []
    while True:
        if len(frontier) == 0:
            raise Exception('Failure')
        node = frontier.pop(0)
        if problem.goal_test(node.state):
            return __solution(node)
        explored.append(node.state)
        for action in problem.actions(node.state):
            child = __child_node(problem, node, action)
            if not (child.state in explored and any(x for x in frontier if x.state == child.state)):
                frontier.append(child)
                frontier = sorted(frontier)
            frontier = [child if x.state == child.state and x.path_cost > child.path_cost else x for x in frontier]

            
def dfs(problem):
    node = Node(state = problem.initial_state, path_cost = 0)
    if problem.goal_test(node.state):
        return __solution(node)
    frontier = [node]
    while True:
        if len(frontier) == 0:
            raise Exception('Failure')
        node = frontier.pop()
        for action in problem.actions(node.state):
            child = __child_node(problem, node, action)
            if not any(x for x in frontier if x.state == child.state):
                #print([x.state for x in frontier])
                #print(child.state)
                if problem.goal_test(child.state):
                    return __solution(child)
                frontier.append(child)


def dfs_visited(problem):
    node = Node(state = problem.initial_state, path_cost = 0)
    if problem.goal_test(node.state):
        return __solution(node)
    frontier = [node]
    explored = []
    while True:
        if len(frontier) == 0:
            raise Exception('Failure')
        node = frontier.pop()
        explored.append(node.state)
        for action in problem.actions(node.state):
            child = __child_node(problem, node, action)
            if not (child.state in explored or any(x for x in frontier if x.state == child.state)):
                if problem.goal_test(child.state):
                    return __solution(child)
                frontier.append(child)


def dls(problem, limit):
    node = Node(state = problem.initial_state)
    return __recursive_dls(node, problem, limit)


def __recursive_dls(node, problem, limit):
    if problem.goal_test(node.state):
        return __solution(node)
    elif limit == 0:
        raise Exception('cutoff')
    else:
        cutoff = False
        for action in problem.actions(node.state):
            child = __child_node(problem, node, action)
            try:
                result = __recursive_dls(child, problem, limit - 1)
                return result
            except Exception as e:
                if e == 'cutoff':
                    cutoff = True
        if cutoff:
            raise Exception('cutoff')
        else:
            raise Exception('Failure')


def ids(problem):
    depth = 0
    while True:
        try:
            result = dls(problem, depth)
            return result
        except Exception as e:
            if e == 'Failure':
                raise e
        depth += 1


def __child_node(problem, parent, action):
    new_state = problem.result(parent.state, action)
    new_path_cost = parent.path_cost + problem.step_cost(parent.state, action)
    return Node(new_state, parent, action, new_path_cost)


def __solution(node):
    sol = []
    while node.action != None:
        sol.insert(0, node.action)
        node = node.parent
    return sol

