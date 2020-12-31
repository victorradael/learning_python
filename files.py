my_file = open('text.txt')

print(my_file)
print(my_file.read())

my_file.seek(0) #Posicionar o cursor de leitura no inicio
print(my_file.readline())