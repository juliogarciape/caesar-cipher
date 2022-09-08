#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Cesar():

	def __init__(self,mensaje):
		self.mensaje_entrada = mensaje.lower()
		self.alfabeto_original = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		self.desplazamiento_cesar = 3
		self.mensaje_salida = ""

	def descifrar(self):
		for i in self.mensaje_entrada:
			if i in self.alfabeto_original:
				pos = self.alfabeto_original.index(i)
				self.mensaje_salida += self.alfabeto_original[pos-self.desplazamiento_cesar]
			else:
				self.mensaje_salida += i
		print("> El mensaje de salida es:",self.mensaje_salida)

	def cifrar(self):
		for i in self.mensaje_entrada:
			if i in self.alfabeto_original:
				pos = self.alfabeto_original.index(i)
				self.mensaje_salida += self.alfabeto_original[pos+self.desplazamiento_cesar]
			else:
				self.mensaje_salida += i
		print("> El mensaje de salida es:",self.mensaje_salida)


def main():
	try:
		flag = sys.argv[1]
		message = sys.argv[2]
		cifrado = Cesar(message)
		
		if flag == "-c":
			cifrado.cifrar()
		elif flag == "-d":
			cifrado.descifrar()
		else:
			print("> %s no es valido"%(flag))
	except:
		print("> Argumentos no validos")


if __name__ == "__main__":
	main()