'''
idade = 18

if idade < 20:
    print("JOVEM")
elif idade < 60:
    print("Adulto")
else:
    print("Melhor idade")
'''

concursos = ["PF", "PRF", "PCDF", "DEPEN"]

for vaga in concursos:
    if vaga[0] == "P":
        print(vaga)
