import pandas as pd
import networkx as nx
from src.carregar_grafo import carregar_grafo_twitch

def calcular_centralidades():
    G = carregar_grafo_twitch()

    deg_centrality = nx.degree_centrality(G)
    bet_centrality = nx.betweenness_centrality(G)
    close_centrality = nx.closeness_centrality(G)
    eigen_centrality = nx.eigenvector_centrality(G, max_iter=1000)

    nos = list(G.nodes())
    dados = []
    
    for no in nos:
        dados.append({
            'No': no,
            'Grau_Absoluto': G.degree(no),
            'Degree_Centrality': deg_centrality[no],
            'Betweenness_Centrality': bet_centrality[no],
            'Closeness_Centrality': close_centrality[no],
            'Eigenvector_Centrality': eigen_centrality[no]
        })
        
    df = pd.DataFrame(dados).set_index('No')

    def exibir_top10(coluna, nome_metrica):
        top10 = df.sort_values(by=coluna, ascending=False).head(10)
        print(f"TOP 10: {nome_metrica.upper()}")
        print(top10[[coluna, 'Grau_Absoluto']].to_string())
        print("\n" + "-"*50 + "\n")

    exibir_top10('Degree_Centrality', 'Degree Centrality')
    exibir_top10('Betweenness_Centrality', 'Betweenness Centrality')
    exibir_top10('Closeness_Centrality', 'Closeness Centrality')
    exibir_top10('Eigenvector_Centrality', 'Eigenvector Centrality')
    
    return df

if __name__ == "__main__":
    calcular_centralidades()