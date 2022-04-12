print('-='*20)
print(' '*2,"CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print('-='*20)

anoNasc = int(input("Digite seu ano de nascimento: "))

idade = 2022 - anoNasc

print(f"Você tem {idade} anos, sua categoria é:")

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SENIOR")
elif idade > 20:
    print("MASTER")