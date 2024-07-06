# Sintaxe:
# print(objetos, argumentos)

# mensagem = " Função Print()"
# print(mensagem)

# print('Imprime a mensagem e muda de linha')
# print("Imprime a mensagem e permanece na linha.", end='')
# print(' Continuo na mesma linha!')

nome = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome, idade)
print(msg_formatada)

msg = f'Meu nome é {nome} e tenho {idade} anos.'
print(msg)

a = 10
b = 5
res = f'A soma de {a} com {b} é igual a {a+b}'
print(res)