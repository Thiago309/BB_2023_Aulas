'''nome = "Michael "
sobreNome = "Jordan"

nomeCompleto = nome + sobreNome
print(nomeCompleto)

repetindoNome = nome*2 + sobreNome*3
print(repetindoNome)

citacao = "Escrevi, e sai correndo, pau no aro ,de quem ta lendo"

tamanhoDaCitacao = len(citacao)
# print(tamanhoDaCitacao)

# Escaneia a frase e informa onde se encontra a string que você deseja.
scanKey = citacao.find("pau")
# O numero printado é a uma casa anterior da string.
# print(scanKey)

# Transforma a citação em lista, dividindo a partir de cada virgula encontrada na citacao
# Mesmo utilizando a função split, nada acontece com a citacao original
citacaoLista = citacao.split(',')
# String são imutaveis.
k = len(citacaoLista)
print(citacaoLista)
print(k)
print(citacao)'''

meuPais = " República Federativa do Brasil "

# meuPaisCaseInvertido = meuPais.swapcase() #A função swap inverte o sensitive Case de cada palavra da string meuPais.
# print(meuPaisCaseInvertido)

meuPaisSemEspaco = meuPais.strip()
print(meuPaisSemEspaco)  # Retira os Espacos do final da string meuPais

outroPais = meuPaisSemEspaco.replace("do Brasil", "da Espanha.")
print(outroPais)
