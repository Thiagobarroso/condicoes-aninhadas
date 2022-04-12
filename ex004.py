print("=-"*20)
print("ALISTAMENTO - SERVIÇO MILITAR")
print("=-"*20)

nasc = int(input("Digite o ano de nascimento: "))

idade = 2022 - nasc
temp = 18 - idade
temp2 = idade - 18

if idade == 18:
    print("Está na hora de você se alistar ao serviço militar")
elif idade >= 18:
    print(f"Vixe!!! já passou {temp2} anos, para você se alistar")
elif idade < 18:
    print(f"Ainda vai se alistar, falta {temp} anos")