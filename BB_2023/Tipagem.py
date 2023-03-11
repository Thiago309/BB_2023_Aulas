def calculaIMC(peso, altura):
    imc = peso / altura**2
    return imc


meuIMC = calculaIMC(80.1, 1.75)
print(meuIMC)

meuIMC = "Tenho que malhar!"
print(meuIMC)

minhaMetaImc = 8 * meuIMC
print(minhaMetaImc)
