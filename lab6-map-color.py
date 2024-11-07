adj = []
color = []

def backtrack(node):
    global v
    global k
    for c in range(k):
        if colorcheck(node,c):
            color[node] = c
            if(node+1<v+1):
                backtrack(node+1)
            else: 
                break

def colorcheck(node, c):
    global v
    for i in range(v+1):
        if(adj[node][i] == 1 and c == color[i]):
            return False
    return True

v, e = input().split()
v, e = int(v), int(e)

for i in range(v+1):
    adj.append([])
    color.append(-1)
    for j in range(v+1):
        adj[i].append(0)    

for i in range(e):
    v1, v2 = input().split()
    v1, v2 = int(v1), int(v2)
    adj[v1][v1] = 1
    adj[v2][v2] = 1
    adj[v1][v2] = 1
    adj[v2][v1] = 1

k = int(input())

backtrack(0)

if -1 in color:
    print("NO")
else:
    for i in range(1, len(color)):
        print(color[i])