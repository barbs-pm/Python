#  -*- coding: utf-8 -*-

min = input("Digite quantos minutos foram usados: ")
if min < 200:
	conta = min * 0.20

else:
	if min <= 400:
		conta = min * 0.18
	
	else:
		conta = min * 0.15	

print 'Sua conta é de R$ %.2lf reais' %conta