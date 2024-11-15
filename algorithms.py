import heapq

def dijkstra(graph, start, end):
    # Objetivos principais aqui:

    # Implementa o algoritmo de Dijkstra para encontrar o menor caminho entre dois nós.
    # graph: Objeto do tipo Graph.
    # start: Nó inicial.
    # end: Nó final.
    # return: Uma tupla contendo (menor caminho como lista de nós, distância total).

    
    # Dicionários para armazenar distâncias mínimas e predecessores
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes}

    # Fila de prioridade para processar os nós
    priority_queue = [(0, start)]  # (distância acumulada, nó)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        # Processar nós vizinhos
        for neighbor, weight in graph.get_neighbors(current_node).items():
            distance = current_distance + weight

            # Atualizar se encontrar uma distância menor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruindo o caminho mais curto
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = predecessors[current]

    # Se o caminho não leva ao início, é inválido
    if path and path[0] != start:
        return None, float('inf')

    return path, distances[end]
