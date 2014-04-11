#!/usr/bin/python
#-*- encoding: utf-8 -*-

import pygame
import common
import random

# Clase disparoPlayer.
class DisparoPlayer(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.contador = 0
		self.frames = []
		
		for i in range(2):
			self.frames.append(common.load_image('pac%d.png' % i, True))
			
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.center = pos
		
	def update(self):
		if self.rect.bottom <= 0:
			self.kill()
		else:
			self.rect.move_ip((0, -4))
			self.animacion()
	

	def animacion(self):
		self.contador += 1
		self.image = self.frames[self.contador % 2]
				


# Clase disparo Enemy.
class DisparoEnemy(pygame.sprite.Sprite):
	def __init__(self, pos, velocDisparo):
		pygame.sprite.Sprite.__init__(self)
		self.dyDisparo = velocDisparo
		self.image = common.load_image('fantasma.bmp', True)
		self.rect = self.image.get_rect()
		self.rect.midtop = pos
		
	def update(self):
		if self.rect.top >= common.ALTO:
			self.kill()
		else:
			self.rect.move_ip((0, 2 + self.dyDisparo ))
