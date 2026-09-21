import pandas as pd
import networkx as nx
import community as community_louvain
from src.carregar_grafo import carregar_grafo_twitch

def analisar_comunidades():
    G = carregar_grafo_twitch()
    
    partition = community_louvain.best_partition(G, random_state=42)
    
    Q = community_louvain.modularity(partition, G)
    print(f"Modularidade global: {Q:.4f}")
    
    df_nos = pd.DataFrame(list(partition.items()), columns=['No', 'Comunidade'])
    contagem = df_nos['Comunidade'].value_counts()
    print(f"Número total de comunidades detectadas: {len(contagem)}\n")
    
    bet_global = nx.betweenness_centrality(G)
    
    top_comunidades = contagem.head(4).index.tolist()
    
    resultados_comunidades = []
    
    for rank, com_id in enumerate(top_comunidades, 1):
        nos_com = df_nos[df_nos['Comunidade'] == com_id]['No'].tolist()
        
        subG = G.subgraph(nos_com).copy()
        
        v_sub = subG.number_of_nodes()
        e_sub = subG.number_of_edges()
        densidade = nx.density(subG)
        grau_medio = sum(d for n, d in subG.degree()) / v_sub if v_sub > 0 else 0
        clustering_medio = nx.average_clustering(subG)
        
        hub_local = max(subG.degree(), key=lambda x: x[1])[0]
        grau_hub_local = subG.degree(hub_local)
        
        conector = max(nos_com, key=lambda n: bet_global[n])
        bet_conector = bet_global[conector]
        
        resultados_comunidades.append({
            'Rank': f"{rank}ª maior",
            'ID_Comunidade': com_id,
            'Nós': v_sub,
            'Arestas': e_sub,
            'Densidade': round(densidade, 4),
            'Grau médio': round(grau_medio, 2),
            'Clustering': round(clustering_medio, 4),
            'Hub local': f"Nó {hub_local} ({grau_hub_local} conexões)",
            'Conector global': f"Nó {conector} ({bet_conector:.4f})"
        })
    
    df_res = pd.DataFrame(resultados_comunidades)
    
    for row in resultados_comunidades:
        print(f"\n--- {row['Rank'].upper()} COMUNIDADE (ID {row['ID_Comunidade']}) ---")
        print(f"• Volume de nós: {row['Nós']} ({(row['Nós']/G.number_of_nodes())*100:.2f}% do grafo total)")
        print(f"• Arestas internas: {row['Arestas']}")
        print(f"• Densidade interna: {row['Densidade']}")
        print(f"• Grau médio interno: {row['Grau médio']}")
        print(f"• Coeficiente de agrupamento: {row['Clustering']}")
        print(f"• Hub local: {row['Hub local']}")
        print(f"• Conector: {row['Conector global']}")
        print("-" * 50)
        
    return partition, df_res

if __name__ == "__main__":
    analisar_comunidades()