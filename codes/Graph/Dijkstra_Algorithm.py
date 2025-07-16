import heapq # TODO: what is a heap

def dijkstra(graph, start):
    min_heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while min_heap:
        curr_distance, curr_node = heapq.heappop(min_heap)
        
        if curr_distance > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
                


    return distances
    

graph = {
    'A':{'B': 1, 'C': 4},
    'B':{'A': 1, 'C': 2, 'D': 5},
    'C':{'A': 4, 'B': 2, 'D': 1},
    'D':{'B': 5, 'C': 1},
}

shortest_path = dijkstra(graph,'A')
print(shortest_path)