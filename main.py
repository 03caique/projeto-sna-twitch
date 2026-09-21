from src.metricas_globais import carregar_metricas
from src.centralidades import calcular_centralidades
from src.comunidades import analisar_comunidades
from src.visualizacao import gerar_visualizacoes

def main():
    print("="*80)
    print("ANÁLISE DE REDES SOCIAIS COMPLEXAS — TWITCH BRASIL (PT-BR)")
    print("="*80)

    print("\n--- ETAPA 1: MÉTRICAS GLOBAIS DA REDE ---\n")
    carregar_metricas()

    print("\n--- ETAPA 2: CENTRALIDADES ---\n")
    calcular_centralidades()

    print("\n--- ETAPA 3: DETECÇÃO E ANÁLISE DE COMUNIDADES ---\n")
    analisar_comunidades()

    print("\n--- ETAPA 4: VISUALIZAÇÕES GRÁFICAS ---\n")
    gerar_visualizacoes()

    print("\n" + "="*80)
    print("PIPELINE CONCLUÍDO — verifique a pasta 'relatorios/' para os gráficos gerados.")
    print("="*80)

if __name__ == "__main__":
    main()