import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import community as community_louvain
from src.carregar_grafo import carregar_grafo_twitch

def gerar_visualizacoes():
    G = carregar_grafo_twitch()
    
    os.makedirs("relatorios", exist_ok=True)
    
    graus_contagem = nx.degree_histogram(G)
    graus_valores = range(len(graus_contagem))

    x = [g for g in graus_valores if graus_contagem[g] > 0]
    y = [graus_contagem[g] for g in graus_valores if graus_contagem[g] > 0]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='purple', alpha=0.8, edgecolors='black', s=40, zorder=3)
    plt.plot(x, y, color='purple', alpha=0.4, linestyle='--', zorder=2)

    plt.title("Distribuição de Graus - Twitch Brasil", fontsize=13, fontweight='bold')
    plt.xlabel("Grau")
    plt.ylabel("Número de Nós")
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)

    caminho_dist = "relatorios/distribuicao_graus.png"
    plt.savefig(caminho_dist, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"-> Salvo em: {caminho_dist}")

    pos = nx.spring_layout(G, seed=42, k=2.5, iterations=150)
    
    partition = community_louvain.best_partition(G, random_state=42)
    cores = [partition[node] for node in G.nodes()]
    
    graus_dict = dict(G.degree())
    hub_real = max(graus_dict, key=graus_dict.get)
    
    plt.figure(figsize=(18, 18), facecolor='white')
    
    nx.draw_networkx_edges(G, pos, alpha=0.20, edge_color='#777777', width=0.25)
    
    tamanhos_nos = [v * 0.8 + 25 for v in graus_dict.values()]
    
    nodes = nx.draw_networkx_nodes(
        G, pos, 
        node_color=cores, 
        cmap=plt.cm.tab20, 
        node_size=tamanhos_nos,
        alpha=0.9,
        edgecolors='black',
        linewidths=0.3
    )
    
    x, y = pos[hub_real]
    plt.annotate(
        f'Hub Principal (Nó {hub_real})\n{graus_dict[hub_real]} conexões', 
        xy=(x, y), 
        xytext=(x + 0.15, y + 0.15),
        fontsize=12, 
        fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.4", fc="#ffeb3b", ec="black", lw=1.2),
        arrowprops=dict(arrowstyle='->', color='black', lw=1.5)
    )
    
    plt.title("Mapa de Comunidades da Twitch Brasil", fontsize=16, fontweight='bold')
    plt.axis('off')
    
    caminho_com = "relatorios/mapa_comunidades.png"
    plt.savefig(caminho_com, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"-> Salvo em: {caminho_com}")

if __name__ == "__main__":
    gerar_visualizacoes()