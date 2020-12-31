myList = [1, 2, 3]
print(myList[1])

myDic = {'chave':1.2, 'chave2': 'string'}
print(myDic)
print(myDic['chave2'])
print(myDic['chave2'].upper()) 

# Depois e tudo normal como uma string comum
# Muito similiar ao objeto ou JSON

myDic['chave2'] = 'mudei'
print(myDic)

# Metodos

print(myDic.keys())
print(myDic.keys()[0])

print(myDic.values())
print(myDic.values()[0])

print(myDic.items())
print(myDic.items()[0])
