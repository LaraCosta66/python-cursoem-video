res = input('Digite Algo:')
print(' o Tipo primitivo é', type(res))
print('e um alfanumerico?',res.isalnum())
print('e um alfabetico?',res.isalpha())
print('é um numero?', res.isnumeric())
print('Esta em maiusculas?', res.isupper())
print('Esta em minusculas?', res.islower())
print('Esta capitalizada?', res.istitle())