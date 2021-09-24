n, s, t = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

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

print(dijkstra(g, s)[t])