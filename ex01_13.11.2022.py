'''Módulo 3 - Introdução à Data Science e Machine Learning
Fuctura

1- Import o Numpy
2 - Utilize a função range do python para criar automaticamente uma lista de
números variando de 0 até 15.
3 - Converta a lista criada para um objeto do tipo numpy array.
4 - Crie um novo array equivalente ao anterior utilizando diretamente os recursos do numpy.
5 - Crie um array de 10 zeros
6 - Crie um array de 10 números "um".
7 - Crie um array de 10 números "5"
8 - Crie um array de inteiros de 10 até 50
9 - Crie uma matriz identidade 3x3'''

#1- Import o Numpy
import numpy as np

#2 - Utilize a função range do python para criar automaticamente uma lista de números variando de 0 até 15.

sequencia15 = list(range(0,16))
print(sequencia15)

print("-"*40)
#3 - Converta a lista criada para um objeto do tipo numpy array.

convertArrayNp = np.array(sequencia15)
print(type(convertArrayNp))
print(convertArrayNp)

print("-"*40)
#4 - Crie um novo array equivalente ao anterior utilizando diretamente os recursos do numpy.

NovaSequencia15 = np.arange(16)
print(NovaSequencia15)

print("-"*40)
#5 - Crie um array de 10 zeros

NovaSequenciaZeros = np.arange(10)*0
print(NovaSequenciaZeros)

print("-"*40)
#6 - Crie um array de 10 números "um".

NovaSequenciaZeros = np.arange(10)*0+1
print(NovaSequenciaZeros)

print("-"*40)
#7 - Crie um array de 10 números "5"

NovaSequenciaZeros = np.arange(10)*0+5
print(NovaSequenciaZeros)

print("-"*40)
#8 - Crie um array de inteiros de 10 até 50

NovaSequenciaAte_50 = np.arange(10,51)
print(NovaSequenciaAte_50)

print("-"*40)
#9 - Crie uma matriz identidade 3x3

MatrizIdentidade =np.eye(3)
print(MatrizIdentidade)

print("-"*40)