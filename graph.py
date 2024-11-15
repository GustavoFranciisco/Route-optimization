class Graph:
    def __init__(self, graph_data):
        
        # Inicializa o grafo com os dados fornecidos.
        # graph_data: Dicionário contendo os nós e arestas do grafo.

        self.nodes = set()
        self.edges = {}
        self._load_graph(graph_data)

    def _load_graph(self, graph_data):

        # Carregando os nós e arestas do grafo a partir dos dados.
        # graph_data: Dicionário contendo os dados do grafo.
        
        for node, neighbors in graph_data.items():
            self.add_node(node)
            for neighbor, weight in neighbors.items():
                self.add_edge(node, neighbor, weight)

    def add_node(self, node):

        # Adicionando um nó ao grafo.
        # node: O nome do nó.

        self.nodes.add(node)
        if node not in self.edges:
            self.edges[node] = {}

    def add_edge(self, from_node, to_node, weight):

        # Adiciona uma aresta entre dois nós.
        # from_node: Nó de origem.
        # to_node: Nó de destino.
        # weight: Peso da aresta.

        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight

    def get_neighbors(self, node):

        # Retorna os vizinhos de um nó.
        # node: O nó cujos vizinhos serão retornados.
        # aqui return é um dicionário de vizinhos com pesos.

        return self.edges.get(node, {})

    def __str__(self):

        # Representação do grafo em formato legível.
        # aqui return é uma string representando o grafo.

        output = []
        for node in self.nodes:
            neighbors = ', '.join(f"{neighbor} (peso {weight})"
                                  for neighbor, weight in self.get_neighbors(node).items())
            output.append(f"{node}: {neighbors}")
        return "\n".join(output)
