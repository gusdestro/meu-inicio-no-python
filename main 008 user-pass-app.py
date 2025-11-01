usuario = input('Digite seu username: ')
senha = input('Digite sua senha: ')

login_valido = usuario == 'admin' and senha == '1234'

print(f'Login permitido? {login_valido}')