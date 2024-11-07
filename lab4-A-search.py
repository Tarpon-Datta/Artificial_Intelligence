import heapq as hq
 
Q = []
visited = []                    # list of visited states
par = {}                        # dictionary to keep track of parent states
hq.heapify(Q)                   # using heapq to make priority queue
    
def moveRight(state,x):         # functions for tile movement
    
    temp = state[x+1]
    state1 = state.replace(state[x+1],'y',1)
    state2 = state1.replace(state1[x],temp,1)
    state2 = state2.replace('y','X',1)
    return state2
        
def moveLeft(state,x):    
    
    temp = state[x-1]
    state1 = state.replace(state[x-1],'y',1)
    state2 = state1.replace(state1[x],temp,1)
    state2 = state2.replace('y','X',1)
    return state2

def moveUp(state,x):
    
    temp = state[x-3]
    state1 = state.replace(state[x-3],'y',1)
    state2 = state1.replace(state1[x],temp,1)
    state2 = state2.replace('y','X',1)
    return state2
    
def moveDown(state,x):
    
    temp = state[x+3]
    state1 = state.replace(state[x+3],'y',1)
    state2 = state1.replace(state1[x],temp,1)
    state2 = state2.replace('y','X',1)
    return state2


def heuristic(state):   # function to calculate manhattan distance of each tile

    h = 0
    for i in range(9):
        if state[i] == '1':
            h = h + abs(int(i/3) - 0) + abs((i%3) - 1)
        if state[i] == '2':
            h = h + abs(int(i/3) - 0) + abs((i%3) - 2)
        if state[i] == '3':
            h = h + abs(int(i/3) - 1) + abs((i%3) - 0)
        if state[i] == '4':
            h = h + abs(int(i/3) - 1) + abs((i%3) - 1)
        if state[i] == '5':
            h = h + abs(int(i/3) - 1) + abs((i%3) - 2)
        if state[i] == '6':
            h = h + abs(int(i/3) - 2) + abs((i%3) - 0)
        if state[i] == '7':
            h = h + abs(int(i/3) - 2) + abs((i%3) - 1)
        if state[i] == '8':
            h = h + abs(int(i/3) - 2) + abs((i%3) - 2)
    return h

def A_star(start, goal):            # function of A* search 
    
    g = 0
    h = heuristic(start)
    cost = g + h
    hq.heappush(Q,(cost,g,h,start))
    
    while Q:
        temp = hq.heappop(Q)
        u = temp[3]
        g = temp[1]        
        if u == goal:
            return 
        x = u.index('X')
        
        if x > 2:
            v = moveUp(u,x)
            if v not in visited:
                visited.append(v)
                h = heuristic(v)
                temp_g = g+1
                hq.heappush(Q,(h+temp_g,temp_g,h,v))
                par[v] = u

        if x < 6:
            v = moveDown(u,x)
            if v not in visited:
                visited.append(v)
                h = heuristic(v)
                temp_g = g+1
                hq.heappush(Q,(h+temp_g,temp_g,h,v))
                par[v] = u
                
        if (x+1)%3 != 1:
            v = moveLeft(u,x)
            if v not in visited:
                visited.append(v)
                h = heuristic(v)
                temp_g = g+1
                hq.heappush(Q,(h+temp_g,temp_g,h,v))
                par[v] = u
                
        if (x+1)%3 != 0:
            v = moveRight(u, x)
            if v not in visited:
                visited.append(v)
                h = heuristic(v)
                temp_g = g+1
                hq.heappush(Q,(h+temp_g,temp_g,h,v))
                par[v] = u

p = []                  

def path(start, goal):          # function of minimum step path
    
    p.append(goal)
    if goal == start:
        p.reverse()
        for i in range(len(p)):
            print(f'step #{i+1}')
            for j in range(3):
                print(f'{p[i][3*j]} {p[i][3*j+1]} {p[i][3*j+2]}') 
            print()
        return    
    goal = par[goal]
    path(start,goal)

# inputs     
print('Enter intial state:')
states = [x for i in range(3) for x in input().split()]
print('Enter goal state:')
goal = [x for i in range(3) for x in input().split()]

# joining input strings
string_state = ''.join(states)
string_goal = ''.join(goal)


# function call
A_star(string_state,string_goal)
path(string_state,string_goal) 