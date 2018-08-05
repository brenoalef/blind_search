from blind_search import *
from math import ceil
from tkinter import *

class EightQueen:
    def __init__(self, initialState):
        self.initialState = initialState

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


def show(positions):
    root = Tk()
    root.title('8-Queens')
    canvas = Canvas(root, bg = 'white', height = 500, width = 500)
    canvas.pack(side = TOP, padx = 10, pady = 10)
    queen = PhotoImage(file = "queen.gif")
    queen = queen.subsample(8, 8)
    x =1
    y =1
    square_size = 500/8
    for rows in range(8):
        color_white = not (rows % 2)
        for columns in range(8):
            color = "lightgray" if color_white else "red"
            x = columns * square_size
            y = rows * square_size
            canvas.create_rectangle(x, y, x + square_size, y + square_size, fill = color)
            if rows * 8 + columns + 1 in positions:
                canvas.create_image(x, y, anchor = NW, image = queen)
            color_white = not color_white

    bou1 = Button(root, text = 'Close', width = 25, command = root.quit)
    bou1.pack(side = RIGHT, padx = 10, pady = 10)

    root.mainloop()


problem = EightQueen([])
print(dfs(problem))
print(dfs_visited(problem))
print(dls(problem, 8))
print(ids(problem))
print(bfs(problem))
print(uniform_cost(problem))

result = dfs(problem)
#result = dfs_visited(problem)
#result = dls(problem, 8)
#result = ids(problem)
#result = bfs(problem)
#result = uniform_cost(problem)
show(result)
