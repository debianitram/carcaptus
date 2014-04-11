#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pygame
import common
import random

# Clase plantas.

class Planta(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		if random.randint(0, 1):
			self.image = common.load_image('arbol.png', True)
		else:
			self.image = common.load_image('flor.png', True)
		self.rect = self.image.get_rect()
		self.rect.center = self.posicionPlanta()


	def update(self):
		if common.scroll:
			self.rect.move_ip(0, common.DELTA)
		if self.rect.top > common.ALTO:
			self.kill()
			
	def posicionPlanta(self):
		if random.randint(0, 1) == 0:
			return (random.randint(0,180), -50)
		else:
			return (random.randint(620, 780), -50)
