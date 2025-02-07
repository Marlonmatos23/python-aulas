#ler a largura e a altura de uma parede em metros
#e calcular a sua area e a quantidade de necessario para pintar
larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
print('A dimensao de',larg ,'junto com a dimensao de',alt ,'é',larg*alt ,'m²' ,'\nVoce vai precisar de',(larg*alt)/2,'l')