print('=-'*20)
print('EMPRÉSTIMO IMOBILIÁRIO')
print('=-'*20)

nome = str(input('Nome completo: '))
sal = float(input('Digite seu salário:'))
val = float(input('Qual o valor do imóvel:' ))
anos = int(input('Quantos anos irá pagar: '))

print(f"Olá, {nome}")
print('Estamos avaliando o crédito.....')


n1 = anos * 12
mensal = val / n1
reprovado = sal - (sal * (70/100))


if mensal > reprovado:
    print(f"infelizmente não conseguimos a sua aprovação no momento")

else:
    print (f"Crédito aprovado, sua mensalidade é R${mensal:,.2f}")