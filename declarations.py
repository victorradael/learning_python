#If em Python

if 1 < 2:
  print('Deu Certo')

#identacao define a organizacao.

#if, elif e else

if 1 < 2:
  print('true')

#elif

if 1 > 2:
  print('true')
elif 1 < 3:
  print('true') # ele segue conferindo de acordo com o que vem apos o if no elif

# else

if 1 > 2:
  print('true')
else: 
  print('true')

#for

colection = [1,2,3,4,5,6]

for num in colection:
  print(num)

for num in colection:
  if num % 2 == 0:
    print('Par')
  else:
    print('Impar')

text = 'isso eh uma string'

for char in text:
  print(char)

myDic = {'chave':1.2, 'chave2': 'string'}

for (chave, valor) in myDic.items():
  print(valor)
#=======While=====================
x=0

while x < 10:
  print(x)
  x += 1

#=================================
y = 0
z = 0

while y < 10 and z < 20:
  print(y)
  print(z)
  y += 1
  z += 2
else:
  print('Nao atendeu')

#=================================
i = 1
lista = []
while True:
  lista += [i]
  i += 1

  if i > 10:
    break

print(lista)