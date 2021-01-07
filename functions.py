text = 'Hi!'

def primeira_funcao(text):
  """
  Printa um texto
  """
  print(text)
  pass

primeira_funcao(text)

def soma(num1, num2):
  return num1 + num2

print(soma(1,2))

def primo(num):
  """
  Metodo para checar se eh primo
  """

  for n in range(2, num):
    if num % n == 0:
      print('Nao eh primo')
      break
    else:
      print('Primo')
      break

primo(11)
primo(120)