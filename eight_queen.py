import time
from tkinter import *
from math import ceil
from functools import partial
from blind_search import *

class EightQueen:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def goal_test(self, state):
        return len(state) == 8

    def actions(self, state):
        col = len(state) + 1
        available = range(col, 65, 8)
        for p in state:
            l = ceil(p / 8)
            c = 1 + (p - 1) % 8
            not_allowed = [(p + col - c), (p + (col - c) * 9), (p - (col - c) * 7)]
            available = [x for x in available if not x in not_allowed]
        return available

    def result(self, state, action):      
        return state + [action]

    def step_cost(self, state, action):
        return 1


root = Tk()
root.title('8-Queens')
canvas = Canvas(root, bg = 'white', height = 500, width = 500)
canvas.pack(side = TOP, padx = 10, pady = 10)
queen = PhotoImage(file = "queen.gif")
queen = queen.subsample(8, 8)
square_size = 500/8
images = []

def update_pos(pos):
    l = ceil(pos / 8) - 1
    c = 1 + (pos - 1) % 8 - 1
    images.append(canvas.create_image(c * square_size , l * square_size, anchor = NW, image = queen))


def clear_show(search):
    for image in images:
        canvas.delete(image)
    search(problem, callback = update_pos)


def show(problem):    
    for rows in range(8):
        color_white = not (rows % 2)
        for columns in range(8):
            color = "lightgray" if color_white else "red"
            x = columns * square_size
            y = rows * square_size
            canvas.create_rectangle(x, y, x + square_size, y + square_size, fill = color)
            color_white = not color_white

    bou1 = Button(root, text = 'DLS', width = 10, command = partial(clear_show, partial(dls_agent, limit=8)))
    bou2 = Button(root, text = 'DFS', width = 10, command = partial(clear_show, dfs_agent))
    bou3 = Button(root, text = 'BFS', width = 10, command = partial(clear_show, bfs_agent))
    bou4 = Button(root, text = 'DFS VISITED', width = 10, command = partial(clear_show, dfs_visited_agent))
    bou5 = Button(root, text = 'IDS', width = 10, command = partial(clear_show, ids_agent))
    bou6 = Button(root, text = 'UNIFORM COST', width = 10, command = partial(clear_show, uniform_cost_agent))
    bou1.pack(side = RIGHT, padx = 10, pady = 10)
    bou2.pack(side = RIGHT, padx = 10, pady = 10)
    bou3.pack(side = RIGHT, padx = 10, pady = 10)
    bou4.pack(side = RIGHT, padx = 10, pady = 10)
    bou5.pack(side = RIGHT, padx = 10, pady = 10)
    bou6.pack(side = RIGHT, padx = 10, pady = 10)

    root.mainloop()


def raw_exec_time(problem):
    start_time = time.clock()
    dfs_agent(problem)
    print("DFS: " + format(time.clock() - start_time, '.5f') + " seconds")
    
    start_time = time.clock()
    dfs_visited_agent(problem)
    print("DFSV: " + format(time.clock() - start_time, '.5f') + " seconds")

    start_time = time.clock()
    dls_agent(problem, 8)
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
    problem = EightQueen([])
    
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
    dls_agent(problem, 8, lambda x: solution.append(x))
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

    show(problem)
