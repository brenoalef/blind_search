from blind_search import *

class RomaniaMap:
    ARAD = "Arad"
    BUCHAREST = "Bucharest"
    CRAIOVA = "Craiova"
    DOBRETA = "Dobreta"
    EFORIE = "Eforie"
    FAGARAS = "Fagaras"
    GIURGIU = "Giurgiu"
    HIRSOVA = "Hirsova"
    IASI = "Iasi"
    LUGOJ = "Lugoj"
    MEHADIA = "Mehadia"
    NEAMT = "Neamt"
    ORADEA = "Oradea"
    PITESTI = "Pitesti"
    RIMNICU_VILCEA = "Riminicu Vilcea"
    SIBIU = "Sibiu"
    TIMISOARA = "Timisoara"
    URZICENI = "Urziceni"
    VASLUI = "Vaslui"
    ZERIND = "Zerind"

    map = {
        ARAD: [(ZERIND, 75), (TIMISOARA, 118), (SIBIU, 140)],
        BUCHAREST: [(URZICENI, 85), (GIURGIU, 90), (PITESTI, 101), (FAGARAS, 211)],
        CRAIOVA: [(DOBRETA, 120), (PITESTI, 138), (RIMNICU_VILCEA, 146)],
        DOBRETA: [(MEHADIA, 75), (CRAIOVA, 120)],
        EFORIE: [(HIRSOVA, 86)],
        FAGARAS: [(SIBIU, 99), (BUCHAREST, 211)],
        GIURGIU: [(BUCHAREST, 90)],
        HIRSOVA: [(EFORIE, 86), (URZICENI, 98)],
        IASI: [(NEAMT, 87), (VASLUI, 142)],
        LUGOJ: [(MEHADIA, 70), (TIMISOARA, 111)],
        MEHADIA: [(LUGOJ, 70), (DOBRETA, 75)],
        NEAMT: [(IASI, 87)],
        ORADEA: [(ZERIND, 71), (SIBIU, 151)],
        PITESTI: [(RIMNICU_VILCEA, 97), (BUCHAREST, 101), (CRAIOVA, 138)],
        RIMNICU_VILCEA: [(SIBIU, 80), (PITESTI, 97), (CRAIOVA, 146)],
        SIBIU: [(RIMNICU_VILCEA, 80), (FAGARAS, 99), (ARAD, 140), (ORADEA, 151)],
        TIMISOARA: [(LUGOJ, 111), (ARAD, 118)],
        URZICENI: [(BUCHAREST, 85), (HIRSOVA, 98), (VASLUI, 142)],
        VASLUI: [(IASI, 92), (URZICENI, 142)],
        ZERIND: [(ORADEA, 71), (ARAD, 75)]
    }

    def __init__(self, initial_state, goal):
        self.initial_state = initial_state
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):
        return self.map[state]

    def result(self, state, action):
        return action[0]

    def step_cost(self, state, action):
        return action[1]


problem = RomaniaMap(RomaniaMap.ARAD, RomaniaMap.BUCHAREST)
#print(dfs(problem))
print(dfs_visited(problem))
print(dls(problem, 3))
print(ids(problem))
print(bfs(problem))
print(uniform_cost(problem))
