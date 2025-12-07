
grafo = {
# Linha 1 - Azul
"Jabaquara": {"Conceição": 2},
"Conceição": {"Jabaquara": 2, "São Judas": 2},
"São Judas": {"Conceição": 2, "Saúde": 2},
"Saúde": {"São Judas": 2, "Praça da Árvore": 2},
"Praça da Árvore": {"Saúde": 2, "Santa Cruz": 2},
"Santa Cruz": {"Praça da Árvore": 2, "Vila Mariana": 2, "Hospital São Paulo": 2, "Chácara Klabin": 2},
"Vila Mariana": {"Santa Cruz": 2, "Ana Rosa": 2},
"Ana Rosa": {"Vila Mariana": 2, "Paraíso": 2, "Chácara Klabin": 2},
"Paraíso": {"Ana Rosa": 2, "Vergueiro": 2, "Brigadeiro": 2},
"Vergueiro": {"Paraíso": 2, "São Joaquim": 2},
"São Joaquim": {"Vergueiro": 2, "Japão-Liberdade": 2},
"Japão-Liberdade": {"São Joaquim": 2, "Sé": 2},
"Sé": {"Japão-Liberdade": 2, "São Bento": 2, "Anhangabaú": 2, "Pedro II": 2},
"São Bento": {"Sé": 2, "Luz": 2},
"Luz": {"São Bento": 2, "Tiradentes": 2, "República": 2},
"Tiradentes": {"Luz": 2, "Armênia": 2},
"Armênia": {"Tiradentes": 2, "Portuguesa-Tietê": 2},
"Portuguesa-Tietê": {"Armênia": 2, "Carandiru": 2},
"Carandiru": {"Portuguesa-Tietê": 2, "Santana": 2},
"Santana": {"Carandiru": 2, "Jardim São Paulo-Ayrton Senna": 2},
"Jardim São Paulo-Ayrton Senna": {"Santana": 2, "Parada Inglesa": 2},
"Parada Inglesa": {"Jardim São Paulo-Ayrton Senna": 2, "Tucuruvi": 2},
"Tucuruvi": {"Parada Inglesa": 2},

# Linha 2 - Verde
"Vila Madalena": {"Sumaré": 2},
"Sumaré": {"Vila Madalena": 2, "Clínicas": 2},
"Clínicas": {"Sumaré": 2, "Consolação": 2},
"Consolação": {"Clínicas": 2, "Trianon-MASP": 2, "Paulista": 2},
"Trianon-MASP": {"Consolação": 2, "Brigadeiro": 2},
"Brigadeiro": {"Trianon-MASP": 2, "Paraíso": 2},
"Chácara Klabin": {"Ana Rosa": 2, "Santos-Imigrantes": 2, "Santa Cruz": 2},
"Santos-Imigrantes": {"Chácara Klabin": 2, "Alto do Ipiranga": 2},
"Alto do Ipiranga": {"Santos-Imigrantes": 2, "Sacomã": 2},
"Sacomã": {"Alto do Ipiranga": 2, "Tamanduateí": 2},
"Tamanduateí": {"Sacomã": 2, "Vila Prudente": 2},
"Vila Prudente": {"Tamanduateí": 2},

# Linha 3 - Vermelha
"Palmeiras-Barra Funda": {"Marechal Deodoro": 2},
"Marechal Deodoro": {"Palmeiras-Barra Funda": 2, "Santa Cecília": 2},
"Santa Cecília": {"Marechal Deodoro": 2, "República": 2},
"República": {"Santa Cecília": 2, "Anhangabaú": 2, "Luz": 2, "Higienópolis-Mackenzie": 2},
"Anhangabaú": {"República": 2, "Sé": 2},
"Pedro II": {"Sé": 2, "Brás": 2},
"Brás": {"Pedro II": 2, "Bresser-Mooca": 2},
"Bresser-Mooca": {"Brás": 2, "Belém": 2},
"Belém": {"Bresser-Mooca": 2, "Tatuapé": 2},
"Tatuapé": {"Belém": 2, "Carrão": 2},
"Carrão": {"Tatuapé": 2, "Penha": 2},
"Penha": {"Carrão": 2, "Vila Matilde": 2},
"Vila Matilde": {"Penha": 2, "Guaianazes": 2},
"Artur Alvim": {"Guaianazes": 2, "Patriarca-Vila Ré": 2},
"Patriarca-Vila Ré": {"Artur Alvim": 2, "Corinthians-Itaquera": 2},
"Corinthians-Itaquera": {"Patriarca-Vila Ré": 2},

# Linha 4 - Amarela
"Higienópolis-Mackenzie": {"República": 2, "Paulista": 2},
"Paulista": {"Higienópolis-Mackenzie": 2, "Oscar Freire": 2, "Consolação": 2},
"Oscar Freire": {"Paulista": 2, "Fradique Coutinho": 2},
"Fradique Coutinho": {"Oscar Freire": 2, "Faria Lima": 2},
"Faria Lima": {"Fradique Coutinho": 2, "Pinheiros": 2},
"Pinheiros": {"Faria Lima": 2, "Butantã": 2},
"Butantã": {"Pinheiros": 2, "São Paulo - Morumbi": 3},
"São Paulo - Morumbi": {"Butantã": 3, "Vila Sônia": 2},
"Vila Sônia": {"São Paulo - Morumbi": 2},

# Linha 5 - Lilás
"Capão Redondo": {"Campo Limpo": 2},
"Campo Limpo": {"Capão Redondo": 2, "Vila das Belezas": 2},
"Vila das Belezas": {"Campo Limpo": 2, "Giovanni Gronchi": 2},
"Giovanni Gronchi": {"Vila das Belezas": 2, "Santo Amaro": 2},
"Santo Amaro": {"Giovanni Gronchi": 2, "Largo Treze": 2},
"Largo Treze": {"Santo Amaro": 2, "Adolfo Pinheiro": 2},
"Adolfo Pinheiro": {"Largo Treze": 2, "Alto da Boa Vista": 2},
"Alto da Boa Vista": {"Adolfo Pinheiro": 2, "Borba Gato": 2},
"Borba Gato": {"Alto da Boa Vista": 2, "Brooklin": 2},
"Brooklin": {"Borba Gato": 2, "Campo Belo": 2},
"Campo Belo": {"Brooklin": 2, "Eucaliptos": 2},
"Eucaliptos": {"Campo Belo": 2, "Moema": 2},
"Moema": {"Eucaliptos": 2, "AACD-Servidor": 2},
"AACD-Servidor": {"Moema": 2, "Hospital São Paulo": 2},
"Hospital São Paulo": {"AACD-Servidor": 2, "Santa Cruz": 2}
}

print("Estações disponíveis:")
for estacao in grafo.keys():
    print(estacao)

print()

estacoes = list(grafo.keys())

inicio = input("Digite a estação inicial: ")
while inicio not in estacoes:
    print(" Estação inválida! Digite novamente.")
    inicio = input("Digite a estação inicial: ")

fim = input("Digite a estação final: ")
while fim not in estacoes:
    print("Estação inválida! Digite novamente.")
    fim = input("Digite a estação final: ")

custos = {n: float("inf") for n in grafo}
custos[inicio] = 0
pais = {inicio: None}
visitados = []
caminho = {inicio: [inicio]}

while True:
    atual = None
    menor = float("inf")
    for n in grafo:
        if n not in visitados and custos[n] < menor:
            menor = custos[n]
            atual = n
    if atual is None:
        break

    for vizinho, tempo in grafo[atual].items():
        novo_custo = custos[atual] + tempo
        if novo_custo < custos[vizinho]:
            custos[vizinho] = novo_custo
            pais[vizinho] = atual
            caminho[vizinho] = caminho[atual] + [vizinho]

    visitados.append(atual)

print("
=== RESULTADO ===")
if custos[fim] == float("inf"):
    print(f"Não há caminho entre {inicio} e {fim}.")
else:
    print("Caminho:", " → ".join(caminho[fim]))
    print("Tempo total:", custos[fim], "minutos")
    print("Número de estações:", len(caminho[fim]))

