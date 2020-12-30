print('This is a String')

teste  = 'VARIAVEL' 
print('Temos uma %s auxiliar.' %(teste))

print('Printando pontos fluantes: %1.2f' %(13.144))

teste  = '123456' 
print('Temos uma %r auxiliar.' %(teste))

varA = 'STRING'
varB = 123456
print('Temos uma string aqui: %s. Temos um inteiro aqui: %r.' %(varA, varB))

a1 = 'One: {a}, Two: {b}, Three: {c}'
print(a1)
a1 = 'One: {a}, Two: {b}, Three: {c}'.format(a=1,b='two',c=12.3)
print(a1)