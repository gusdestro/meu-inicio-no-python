preco = float(input("Digite o preço do produto: ")) # Valor em €
desconto = float(input("Digite a porcentagem do desconto: ")) # Desconto em %

preco_final = preco - (preco * desconto / 100)

print(f"O preço final do produto é: € {preco_final:.2f}")
print("Obrigado por usar o calculador de desconto!")