n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"O {n1} é maior que {n2}")
elif n1 < n2:
    print(f"O {n2} é maior que {n1}")
elif n1 == n2:
    print("Não existe valor maior, os dois são iguais")
