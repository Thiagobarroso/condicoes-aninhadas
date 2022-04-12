print('=-'*20)
print("Quem é você na familia?")
print('=-'*20)
nome = str(input("Digite seu nome: "))
if nome == "Thiago":
    print("Você é o filho casula")
elif nome == "Gisele" or nome == "Felipe":
    print("Você é irmão do Thiago, e filho do Jorge e Sueli")
elif nome == 'Sueli' or nome == 'Jorge':
    print("Você é Matriarca ou Patriarca da familia")
elif nome == "Andressa":
    print("Você é esposa do Thaigo")
elif nome == "Bernardo":
    print("você é filho do Thiago e Andressa")

else:
    print("Você não faz parte da Familia")
    print("Tenha um bom dia!")