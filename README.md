Este programa calcula o menor caminho entre duas estações do metrô. Ele começa criando um grafo, que é um conjunto de estações onde cada uma contém suas estações vizinhas e o tempo de viagem entre elas. Esse grafo é apenas um dicionário de Python organizado por linhas.

Depois o código mostra todas as estações para o usuário e pede duas entradas: início e fim. Há validação simples para garantir que o nome digitado existe no grafo.

Com as entradas confirmadas, o programa cria três estruturas importantes: custos, que guarda o tempo acumulado até cada estação; visitados, que marca as estações já analisadas; e caminho, que armazena o trajeto completo até cada ponto. O algoritmo usado é o Dijkstra, que sempre escolhe a estação com menor custo ainda não visitada e tenta melhorar os caminhos para seus vizinhos.

Ao final, o programa imprime o trajeto completo, o tempo total e o número de estações.

Exemplo de trecho explicado:

grafo = {
"Jabaquara": {"Conceição": 2}
}

Acima, Jabaquara está conectada a Conceição com tempo de 2 minutos.# Subway-Maps
