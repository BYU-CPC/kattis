# read in data
x0, y0 = map(float, input().split())
xt, yt = map(float, input().split())
n = int(input())
cannon = [tuple(map(float, input().split())) for _ in range(n)]

# calculate distance between every point
g = [[0]*(n+2) for _ in range(n+2)]
for i in range(n):
    for j in range(i+1, n):
        dist = ( (cannon[i][0] - cannon[j][0])**2 + (cannon[i][1] - cannon[j][1])**2 )**0.5
        g[i][j] = g[j][i] = min(2 + abs(dist - 50)/5, dist/5)
    
    # distance between cannon and start
    dist = ( (cannon[i][0] - x0)**2 + (cannon[i][1] - y0)**2 )**0.5
    g[i][n] = min(2 + abs(dist - 50)/5, dist/5)
    g[n][i] = dist/5

    # distance between cannon and end
    dist = ( (cannon[i][0] - xt)**2 + (cannon[i][1] - yt)**2 )**0.5
    g[i][n+1] = min(2 + abs(dist - 50)/5, dist/5)
    g[n+1][i] = dist/5

# distance between start and end
g[n][n+1] = g[n+1][n] = ( (x0 - xt)**2 + (y0 - yt)**2 )**0.5 / 5

def dijkstra(graph, source):
    visited = [False]*len(graph)
    numLeft = len(graph)
    dist = [float('inf')]*len(graph)
    dist[source] = 0

    while numLeft > 0:
        visited[source] = True
        numLeft -= 1
        for n in range(len(graph)):
            if n != source and not visited[n]:
                dist[n] = min(dist[n], dist[source] + graph[source][n])
        
        loDist = float('inf')
        for n in range(len(graph)):
            if not visited[n] and dist[n] <= loDist:
                source = n
                loDist = dist[n]
    
    return dist

# answer will be stored in resulting list at index n+1
print(dijkstra(g, n)[n+1])