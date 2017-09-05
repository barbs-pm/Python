# -*- coding: utf-8 -*-

n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
n3 = input('Digite o terceiro número: ')

if n1 > n2 and n1 > n3:
	maior = n1

else:
	if n2 > n3:
		maior = n2

	else:
		maior = n3

print '\nO maior dos 3 valores é: ', maior