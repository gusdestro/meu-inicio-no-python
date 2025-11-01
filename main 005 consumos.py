bananas = int(input('Quantas bananas você tem? '))
consumo_bananas = int(input('Quantas bananas você consome por dia? '))

duracao = bananas // consumo_bananas

print(f'Ao comer {consumo_bananas} bananas por dia, levaria {duracao} dias para acabar as bananas.')