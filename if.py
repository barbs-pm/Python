# -*- coding: utf-8 -*-

vel = input("Digite sua velocidade: ")
if vel > 110:
	multa = (vel - 110) * 5
	print 'Você foi multado em $%5.2lf reais.' %multa
else:
	print 'Velocidade dentro do limite.'