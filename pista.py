#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pygame, common
from pygame.locals import *

# Clase Ruta

class Ruta(pygame.sprite.Sprite):

	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.image = common.load_image('ruta.jpg')
		self.rect = self.image.get_rect()
		self.rect.topleft = (posx, posy)
		
	def update(self):
		if common.scroll:
			self.rect.move_ip(0, common.DELTA)
			if self.rect.top >= common.ALTO:
				self.rect.bottom = common.ALTO - self.rect.height
