idade = int(input("Digite a sua idade: "))
autoriza_pais = input("Você tem autorização dos pais? (sim/não): ")

if idade >= 18:
    print('Autorizado')

elif idade >= 16 and autoriza_pais == 'sim':
    print('Autorizado com autorização dos pais')

else:
    print('Não autorizado')