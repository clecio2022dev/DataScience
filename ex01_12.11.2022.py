"""Desafio de Classe

    1- Criar um array unidimensional usando arange com 20 elementos;

    2- "Varrer" o array para obter os pares;

    3- "Varrer" o array para obter os ímpares;

    4- Obtera média, a soma, o produto, a variância e odesvio padrão do array

    5- saber se os valores são maiores que 5;

    6- Obter os valores maiores que 5"""

import numpy as np

# 1- Criar um array unidimensional usando arange com 20 elementos;

criandoArray = np.arange(20)
print(criandoArray)

print('-'*30)

# 2- "Varrer" o array para obter os pares;

paresArray = []
for i in criandoArray:
    if i % 2 == 0:
        paresArray.append(i)
print(paresArray)

print('-'*30)

# 3- "Varrer" o array para obter os ímpares;

imparesArray = []
for i in criandoArray:
    if i % 2 == 1:
        imparesArray.append(i)
print(imparesArray)

print('-'*30)

# 4- Obtera média, a soma, o produto, a variância e odesvio padrão do array

print(np.mean(criandoArray)) #média

print(np.sum(criandoArray)) #soma

print(np.prod(criandoArray)) #produto

print(np.var(criandoArray)) #variância

print(np.std(criandoArray)) #desvio padrão

print('-'*30)

# 5- saber se os valores são maiores que 5;

for i in criandoArray:
  if i > 5:
    print('{} é maior que 5'.format(i))
  else:
    print('{} não é maior que 5'.format(i))


print('-'*30)


# 6- Obter os valores maiores que 5

maioresQue5 = []
for i in criandoArray:
  if i > 5:
    maioresQue5.append(i)
print(maioresQue5)

