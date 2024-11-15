import json
from graph import Graph
from algorithms import dijkstra

def load_graph(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{file_path}' não está em formato JSON válido.")
        return None

def main():
    print("=== Otimizador de Rotas ===")
    
    # Carregar o grafo (JSON)
    graph_data = load_graph("Locais.json")
    if not graph_data:
        return

    # Criando o grafo
    graph = Graph(graph_data)

    # Pegar entrada do usuário
    start = input("Digite a cidade que será o ponto de partida: ")
    end = input("Digite a cidade que será o ponto de destino: ")

    if start not in graph.nodes or end not in graph.nodes:
        print("Erro: Um ou ambos os pontos de partida ou destino não estão no grafo.")
        return

    # Calcular a melhor rota (Dijkstra)
    print("\nCalculando a melhor rota...")
    shortest_path, distance = dijkstra(graph, start, end)


    if shortest_path:
        print(f"\nRota mais curta de {start} para {end}: {' -> '.join(shortest_path)}")
        print(f"Distância total: {distance}")
    else:
        print(f"Não foi possível encontrar uma rota de {start} para {end}.")

if __name__ == "__main__":
    main()
