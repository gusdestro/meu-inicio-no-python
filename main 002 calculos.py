nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

mensagem = f"Olá, {nome}! Você tem {idade} anos." # Concatenação de strings usando f-strings
mensagem_idade = f"Daqui a 5 anos, você terá {int(idade) + 5} anos." # Cálculo simples dentro de f-strings

print(mensagem)
print(mensagem_idade)