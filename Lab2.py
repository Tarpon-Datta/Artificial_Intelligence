# Uniform Cost Search
import random
def UCS(goal, start):

    global graph, cost
    result = []

    queue = []

    for i in range(len(goal)):
        result.append(10**8)

    queue.append([0, start])

    visited = {}

    count = 0

    while (len(queue) > 0):

        queue = sorted(queue)
        p = queue[-1]

        del queue[-1]

        p[0] *= -1

        if (p[1] in goal):

            index = goal.index(p[1])

            if (result[index] == 10**8):
                count += 1

            if (result[index] > p[0]):
                result[index] = p[0]

            del queue[-1]

            queue = sorted(queue)
            if (count == len(goal)):
                return result

        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):

                queue.append(
                    [(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        visited[p[1]] = 1

    return result

if __name__ == '__main__':
    V, E = input().split()
    V = int(V)
    E = int(E)

    graph, cost = [[] for i in range(V)], {}

    for i in range(E):
        x, y, w = input().split()
        x = int(x)
        y = int(y)
        w = int(w)
        x = x-1
        y = y-1
        graph[x].append(y)
        cost[(x, y)] = w

    goal = []

    S, D = input().split()
    S = int(S)
    D = int(D)
    S = S-1
    D = D-1

    goal.append(D)

    result =UCS(goal, S)
    print(result[0])
    

