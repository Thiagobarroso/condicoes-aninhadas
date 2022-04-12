print('-='*20)
print(' '*10,"CALCULO IMC")
print('-='*20)

peso = float(input("Digite o seu peso: "))
alt = float(input("Digite sua altura: "))

imc = peso / alt**2

print(f"Seu IMC é {imc:,.2f}")

if imc < 18.5:
    print("Você está abixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade ')
elif imc > 40:
    print('Obesidade grave')