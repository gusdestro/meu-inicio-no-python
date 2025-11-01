usuario = input('Digite seu username: ')
senha = input('Digite sua senha: ')

login_valido = usuario == 'admin' and senha == '1234'

if login_valido:
    print('Bem-vindo, admin!')
else:
    print('Usuário ou senha inválidos.')