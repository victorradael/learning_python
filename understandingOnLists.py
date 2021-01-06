lista = [i for i in range(0,30)]

print(lista)

lista2 = [i for i in range(0,30) if i % 2 == 0]

print(lista2)

# converter temperaturas

celsius = [ 0, 10 ,15, 20, 30, 50 ,100]

fahrenheit = [temp * (9/5) + 32 for temp in celsius]

print(fahrenheit)