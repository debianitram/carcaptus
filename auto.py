#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pygame
import common
import random

# Clase Carplayer

class CarPlayer(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen_base = common.load_image('auto.png', True)
		self.image = self.imagen_base
		self.rect = self.image.get_rect()
		self.giro = 0
		self.rect.center = (400, 500)
		
	def update(self):
		if self.giro >= 45:
			self.giro = 45
		elif self.giro <= -45:
			self.giro = -45
		else:
			x, y = self.rect.center
			self.image = pygame.transform.rotate(self.imagen_base, self.giro)
			self.rect = self.image.get_rect()
			self.rect.center = x, y
			
		if self.giro and common.scroll:
			self.rect.move_ip(-self.giro/10, 0)
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right >= common.ANCHO:
				self.rect.right = common.ANCHO
				
# Clase CarEnemy

class CarEnemy(pygame.sprite.Sprite):
	""" imag es el valor de la imagen que pondra para el enemigo """
	def __init__(self, posx, imag, objGroupDisparo, objDisparo, objSonido):
		pygame.sprite.Sprite.__init__(self)
		
		self.objGroupDisparo = objGroupDisparo
		self.objDisparo = objDisparo
		self.objSonido = objSonido
		
		self.image = common.load_image('auto%d.png' % imag, True)
		self.rect = self.image.get_rect()
		self.rect.center = (posx, -30)
		self.dy = random.randint(5, 10)
		
	def update(self):
		self.rect.move_ip((0, self.dy))
		if self.rect.top > common.ALTO:
			self.kill()
		self.disparar(random.randint(0, 60))
			
	
	def disparar(self, bala):
		""" bala = randint(0, 60), group = grupoBala """
		
		if bala == 0:
			self.objGroupDisparo.add(self.objDisparo(self.rect.midbottom, self.dy))
			self.objSonido.play()
