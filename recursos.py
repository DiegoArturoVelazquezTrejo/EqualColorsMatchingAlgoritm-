import random 

def generarCadena():
  strg = 'Equals-'
  for i in range(0,4):
    strg = strg + random.choice('1234567890ABCDEFGHIJK')
  return strg
