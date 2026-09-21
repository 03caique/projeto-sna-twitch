import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import community as community_louvain
from src.carregar_grafo import carregar_grafo_twitch

def gerar_visualizacoes():
    G = carregar_grafo_twitch()
    
    os.makedirs("relatorios", exist_ok=True)
    
    graus = [d for n, d in G.degree()]
    
    bins_log = np.logspace(np.log10(min(graus)), np.log10(max(graus)), 30)
    
    plt.figure(figsize=(8, 6))
    plt.hist(graus, bins=bins_log, color='purple', alpha=0.7, edgecolor='black')
    plt.title("Distribuição de Graus - Twitch Brasil (SNA)")
    plt.xlabel("Grau (k)")
    plt.ylabel("Frequência / Número de Nós")
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    
    caminho_dist = "relatorios/distribuicao_graus.png"
    plt.savefig(caminho_dist, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"-> Salvo em: {caminho_dist}")

    pos = nx.spring_layout(G, seed=42, k=1.5, iterations=100)
    
    partition = community_louvain.best_partition(G, random_state=42)
    cores = [partition[node] for node in G.nodes()]
    
    num_comunidades = len(set(partition.values()))
    print(f"Número de comunidades detectadas: {num_comunidades}")
    if num_comunidades > 20:
        print("Aviso: mais de 20 comunidades — cores podem se repetir na paleta tab20.")

    graus_dict = dict(G.degree())
    hub_real = max(graus_dict, key=graus_dict.get)
    
    plt.figure(figsize=(16, 16))
    
    nx.draw_networkx_edges(G, pos, alpha=0.02, edge_color='gray', width=0.3)
    
    nodes = nx.draw_networkx_nodes(
        G, pos, 
        node_color=cores, 
        cmap=plt.cm.tab20, 
        node_size=[v * 0.15 + 10 for v in graus_dict.values()],
        alpha=0.8
    )
    
    x, y = pos[hub_real]
    plt.annotate(
        f'Nó {hub_real} (Hub)', 
        xy=(x, y), 
        xytext=(x + 0.3, y + 0.3),
        fontsize=13, 
        fontweight='bold',
        arrowprops=dict(arrowstyle='->', color='black', lw=1.5)
    )
    
    plt.title("Mapa de Comunidades da Twitch Brasil (Algoritmo de Louvain)", fontsize=14)
    plt.axis('off')
    
    caminho_com = "relatorios/mapa_comunidades.png"
    plt.savefig(caminho_com, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"-> Salvo em: {caminho_com}")
    
if __name__ == "__main__":
    gerar_visualizacoes()