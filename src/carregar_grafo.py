import networkx as nx
import pandas as pd

def carregar_grafo_twitch():
    caminho_csv = "dados/musae_PTBR_edges.csv"
    df = pd.read_csv(caminho_csv)
    G = nx.from_pandas_edgelist(df, source="from", target="to", create_using=nx.Graph())
    return G

if __name__ == "__main__":
    G = carregar_grafo_twitch()
    print("Grafo carregado com sucesso!")
    print(f"Número total de nós: {G.number_of_nodes()}")
    print(f"Número total de arestas: {G.number_of_edges()}")
    