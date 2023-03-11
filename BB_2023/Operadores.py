'''
    OPERADORES NUMERICOS

X+Y     Adição
X-Y     Subtração
X*Y     Multiplicação
X/Y     Divisão
X//Y    Divisão Arredondar --> Arredonda o resultado da divisão para um nº inteiro mais próximo.
X**Y    Potenciação

'''
'''
    OPERADORES BOLEANOS

X < Y       Menor
X <= Y      Menor ou igual
X > Y       Maior
X >= Y      Maior ou igual
X == Y      Igual
X != Y      Diferente
X is Y      Testa se X e Y são o mesmo objeto
X is not Y  Testa se X e Y não são o mesmo objeto
X < Y < Z   Comparação Tripla
not X       Inverte o valor lógico de X
'''


''' Exemplo para o operador IS.

x = ["Maca", "Abacaxi"]
y = ["Maca", "Abacaxi"]
z = x

# Tem retorno verdadeiro por que Z recebe os objetos da lista X.
print(x is z)

# Tem retorno falso por que Y tem os mesmos objetos que X, porém em lista diferentes.
print(x is y)

# Tem verdadeiro objetos iguais idependente se em mesma listas ou não.
print(x == y)
'''

'''
    OPERADOR SEQUENCIAL

X in S      Verifica se o elemento X pertence à sequência S
X not is S  Verifica se o elemento X não pertence à sequeência S
S1 + S2     Concatena as sequências S1 e S2
n * S       Repete n vezes a sequência S
len(S)      Retorna o tamanho de S
min(S)      Retorna o mínimo elemento de S
max(S)      Retorna o máximo elemento de S
for X in S  Percorre todos os elementos de S armazenando o elemento corrente em X
del S[i]    Deleta o elemento localizado no índice i
S[i:j]      Fatia a sequencia S entre os índices i e j

lista = "Ismael"
print(lista[0:4])       EXEMPLO
'''