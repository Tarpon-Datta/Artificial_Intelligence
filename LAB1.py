from re import A
import queue
goal = dict()

def addEdge(edge1, edge2):
    if edge1 not in goal:
        goal[edge1]=[]
    if edge2 not in goal:
        goal[edge2]=[]
        
    goal[edge1].append(edge2)
    if edge1 != edge2:
        goal[edge2].append(edge1)


def bfs(source, dest, n):
  q = queue.Queue()
  dist = [-1]*n
  prnt = [-1]*n
  dist[source]=0
  q.put(source)

  while(q.empty()==False):
    x=q.get()

    for i in goal:
      if dist[i]==-1:
        prnt[i] = x
        dist[i] = 1+dist[x]
        q.put(i)
  print(dist[dest])

  child = int(dest)
  path = []

  while prnt[child] != -1:
    step = f"{prnt[child]} {child}"
    path.append(step)
    child = prnt[child]

  for i in range(len(path)-1, -1, -1):
    print(path[i])

def serial(source, n):
  q = queue.Queue()
  dist = [-1]*n
  serl = [-1]*n
  a = 1

  dist[source]=0
  serl[source] = a 
  a+=1
  q.put(source)

  while(q.empty()==False):
    x = q.get()
    for i in goal:
      if dist[i] == -1:
        serl[i] = a
        dist[i] = 1 + dist[x]
        q.put(i)
        a+=1
      
  
  for i in range(1, len(serl)):
    print(serl[i])

v, e = input().split()

for i in range(int(e)):
  edge1, edge2 = input().split()
  addEdge(int(edge1), int(edge2))


source, dest = input().split()
print("----")
print(source, dest)

for key, val in goal.items():
        print(f"{key}-->{val}")

bfs(int(source), int(dest), int(v)+1)

serial(1, int(v)+1)