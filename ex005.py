n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))

media = (n1 + n2 + n3) / 3

print(f"Sua média é {media}")

if media < 5.0:
    print("REPROVADO")
elif media < 7:
    print("RECUPERAÇÃO")
elif media >= 7.0:
    print("APROVADO")