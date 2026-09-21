import networkx as nx
from src.carregar_grafo import carregar_grafo_twitch

def carregar_metricas():
    G = carregar_grafo_twitch()

    v = nx.number_of_nodes(G)
    e = nx.number_of_edges(G)
    print(f"Ordem: {v}")
    print(f"Tamanho: {e}")

    if (nx.is_directed(G)):
        print("Tipo: Direcionada")
    else:
        print("Tipo: Não-direcionada")

    if nx.is_weighted(G):
        print("Ponderada: Sim")
    else:
        print("Ponderada: Não")

    densidade = nx.density(G)
    print(f"Densidade: {densidade:.6f}")
    
    graus = [d for n, d in nx.degree(G)] 
    grau_medio = sum(graus) / v 
    print(f"Grau médio: {grau_medio:.2f}")

    componentes = list(nx.connected_components(G))
    print(f"Quantidade de componentes conexos: {len(componentes)}")

    maior_comp_nos = max(componentes, key=len)
    G_giant = G.subgraph(maior_comp_nos).copy()
    pct_giant = (G_giant.number_of_nodes() / v) * 100
    print(f"Giant component: {G_giant.number_of_nodes()} nós ({pct_giant:.2f}% da rede toda)")

    media_caminhos = nx.average_shortest_path_length(G_giant)
    diametro = nx.diameter(G_giant)
    print(f"Comprimento Médio do Caminho Mais Curto: {media_caminhos:.4f}")
    print(f"Diâmetro da Rede: {diametro}")

    agrupamento_medio = nx.average_clustering(G)
    transitividade = nx.transitivity(G)
    print(f"Coeficiente de Agrupamento Médio: {agrupamento_medio:.4f}")
    print(f"Transitividade: {transitividade:.4f}")

if __name__ == "__main__":
    carregar_metricas()
    