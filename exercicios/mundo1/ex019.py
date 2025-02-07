#sortear um dos 4 alunos para apagar o quadro
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
l = [n1,n2,n3,n4]
e = random.choice(l)
print('Quem vai limpar vai ser {}'.format(e))
