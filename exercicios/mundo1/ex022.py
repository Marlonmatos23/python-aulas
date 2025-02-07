#ler um nome e mostrar com as letra maiuscula e minuscula e contar
#as letras sem espaco e conta quantas tem o primeiro nome
n = str(input('Digite o seu nome completo: ')).strip()
print('hummmm...')
print('Seu nome completo fica {}'.format(n.upper()))
print('Seu nome minusculo fica {}'.format(n.lower()))
print('Seu nome tem no total {} de letras'.format(len(n) -n.count(' ')))
print('Seu primeiro nome tem {} de letras'.format(n.find(' ')))
