parent = []
explore = []
trace  = []
path = []
adj = []
goalFound = False

def addEdge(u, v, weight):
    adj[u].append([v, weight])
    adj[v].append([u, weight])

def dfs(start, goal, cost):
    global d
    global goalFound
    if start == goal:
        d = cost
        goalFound = True
        print(d)
        return
    trace[start] = 1
    for i in adj[start]:
        v = i[0]
        w = i[1]
        if trace[v] == 0:
            parent[v] = start
            dfs(v, goal, cost+w)
            explore[v] = 1
            if goalFound:
                return

def findPath(start, goal):
    path.append(goal)
    if goal!=start:
        if parent[goal]!=-1:    
            findPath(start,parent[goal])
        else:
            print("-1")        
            return

def printPath():
    path.reverse()
    print(len(path))
    for i in range(len(path)):
        print(path[i])

if __name__=="__main__":            
    v, e = input().split()
    v, e = int(v), int(e)
    count = 0
    
    for i in range(v+1):
        adj.append([])
        parent.append(-1)
        trace.append(0)
        explore.append(0)
    
    for i in range(e):
        v1, v2, w = input().split()
        v1, v2, w = int(v1), int(v2), int(w)
        addEdge(v1, v2, w)
        
    s, g = input().split()
    s, g = int(s), int(g)
    
    dfs(s, g, 0)
    findPath(s, g)
    printPath()
    for i in explore:
            if i == 1:
                count = count + 1
    print(count)