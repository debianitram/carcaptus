#!/usr/bin/python
# -*- encoding: utf-8 -*-

""" Módulo para implementar el manejo de gráficos y superficies """

# Módulos
import pygame, os

################# Variables y constantes. #################
"""Configuración general de Carcaptus """
titulo = "Carcaptus"

# Resolución
ANCHO = 800
ALTO = 600

# Movimiento de la pantalla
scroll = False

# CONSTANTE VELOCIDAD
DELTA = 5

# Directorios
sprites = "data/imagen/"
audio = "data/sonido/"
fuente = "data/fuente/"


################# Funciones #################
# Carga una imagen 
def load_image(filename, transparent=False, pixel=(0,0)):
	
	path = os.path.join(sprites, filename)
	try: image = pygame.image.load(path)
	except pygame.error, message:
		raise SystemExit, message
	image = image.convert()
	if transparent:
		color = image.get_at(pixel)
		image.set_colorkey(color, pygame.RLEACCEL)
	return image
	

# Carga un sonido

def load_sound(filename):
	class noSound:
		def play(self):
			pass
			
	if not pygame.mixer or not pygame.mixer.get_init():
		return noSound()
	
	path = os.path.join(audio, filename)
	
	try:
		sound = pygame.mixer.Sound(path)
	except pygame.error, message:
		print "No se puede cargar el sonido:", lugar
		raise SystemExit, message
	
	return sound
	

