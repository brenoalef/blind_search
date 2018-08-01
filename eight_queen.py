from blind_search import *
from math import ceil
from tkinter import *

class EightQueen:
    board = range(1, 65)

    def __init__(self, initialState):
        self.initialState = initialState

    def goal_test(self, state):
        return len(state) == 8

    def actions(self, state):
        not_allowed = []
        for p in state:
            l = ceil(p / 8)
            c = 1 + (p-1) % 8
            not_allowed += range(c, 65, 8)
            not_allowed += range((l-1)*8 + 1, l*8 + 1, 1)
            not_allowed += range(p - (min(l, c) - 1)*9, p + (8 - max(l, c))*9 + 1, 9)
            not_allowed += range(p - (min(l - 1, 8 - c))*7, p + min(8 - l, c - 1)*7 + 1, 7)
        return [ x for x in self.board if not x in not_allowed ]


    def result(self, state, action):
        return state + [action]

    def step_cost(self, state, action):
        return 1

problem = EightQueen([])
print(dfs(problem))
print(dfs_visited(problem))
print(dls(problem, 8))
print(ids(problem))
print(bfs(problem))
print(uniform_cost(problem))


result = dls(problem, 8)
print(result)
root = Tk()
root.title(str(8) + ' queens')
canvas = Canvas(root,bg='white',height=500,width=500)
canvas.pack(side=TOP,padx=10,pady=10)
queen = PhotoImage(file="queen.gif")
queen = queen.subsample(8, 8)
board_rows=8
board_cols=8
x=1
y=1
square_size= 500/8
for rows in range(board_rows):
    color_white = not (rows%2)
    for columns in range(board_cols):
        color="lightgray"
        if not color_white:
            color="red"
        x=columns*square_size
        y=rows*square_size
        canvas.create_rectangle(x, y, x+square_size, y+square_size, fill=color)
        if rows*8 + columns + 1 in result:
            canvas.create_image(x, y, anchor = NW, image=queen)
        color_white = not color_white

bou1 = Button(root,text='Close',width=25,command=root.quit)
bou1.pack(side=RIGHT,padx=10,pady=10)

root.mainloop()
