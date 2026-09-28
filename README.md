# Análise de Redes Sociais Complexas — Twitch Brasil (PT-BR)

Projeto da disciplina de Tópicos Avançados em Sistemas para Internet — CST em Sistemas para Internet (6º período), IFSertãoPE Campus Salgueiro.

## Dataset

Rede social de usuários do Twitch que transmitem em português, extraída do MUSAE Twitch Social Networks (SNAP/Stanford). Nós representam usuários; arestas representam amizades mútuas.

- Fonte: https://snap.stanford.edu/data/twitch-social-networks.html
- Nós: 1.912 | Arestas: 31.299 | Densidade: 0,017

## Estrutura do projeto

projeto-sna-twitch/
├── dados/
│ └── musae_PTBR_edges.csv
├── src/
│ ├── carregar_grafo.py # Carregamento do grafo
│ ├── metricas_globais.py # Etapa 1: densidade, grau médio, diâmetro etc.
│ ├── centralidades.py # Etapa 2: degree, betweenness, closeness, eigenvector
│ ├── comunidades.py # Etapa 3: detecção Louvain e análise por comunidade
│ └── visualizacao.py # Etapa 4: histograma e mapa de comunidades
├── relatorios/ # Gráficos gerados (.png)
├── main.py # Executa o pipeline completo
└── requirements.txt


## Como executar

1. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o pipeline completo:
```bash
python main.py
```

Os gráficos serão salvos automaticamente em `relatorios/`.

## Principais achados

- O nó 127 é o hub dominante da rede, líder simultâneo nas quatro métricas de centralidade (degree, betweenness, closeness e eigenvector).
- Rede altamente conectada: um único componente conexo (100% giant component), diâmetro 7, caminho médio de 2,53 — características de rede "mundo pequeno".
- Modularidade Q obtida com Louvain: 0.2909