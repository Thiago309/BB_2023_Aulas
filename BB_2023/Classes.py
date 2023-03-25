class Cachorro:
    tipo = "Canino"

    def __init__(self, nome):
        self.nome = nome

caozinho1 = Cachorro("Bob")
caozinho2 = Cachorro("Rex")
 
print(caozinho1.tipo)
print(caozinho1.nome)

print(caozinho2.tipo)
print(caozinho2.nome)