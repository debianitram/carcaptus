#!/usr/bin/python
#-*- encoding: utf-8 -*-

# import
import pygame
import common
import random
from pygame.locals import *
from auto import CarPlayer, CarEnemy
from balas import DisparoPlayer, DisparoEnemy
import ImageDraw
from PIL import ImageEnhance
from plantas import Planta
from pista import Ruta
from bomba import Boom

pygame.init()
screen = pygame.display.set_mode((common.ANCHO, common.ALTO))
pygame.display.set_caption(common.titulo)

# Objetos
ruta1 = Ruta(0,0)
ruta2 = Ruta(0, -ruta1.rect.height)
autoJugador = CarPlayer()


# Objetos Sonidos.
sonido_jugador = common.load_sound("piu.ogg")
sonido_enemigo = common.load_sound("scup.ogg")
sonido_explosion = common.load_sound("kboom.ogg")



# Grupos
fondo_grupo = pygame.sprite.RenderUpdates(ruta1, ruta2)

jugador_grupo = pygame.sprite.RenderUpdates(autoJugador)
enemigos_grupo = pygame.sprite.RenderUpdates()

disparos_grupo = pygame.sprite.RenderUpdates()
disparos_enemigos_grupo = pygame.sprite.RenderUpdates()

objVarios_grupo = pygame.sprite.RenderUpdates()

# Contadores.
enemigos = 0
plantas = 0

# Reloj
reloj = pygame.time.Clock()

# Estado del bucle y objetos.
estado = True
common.scroll = False


screen.blit(ruta1.image, ruta1.rect)

ref = (common.ANCHO, common.ALTO)
brightness = 1.0
contrast = 1.0

while estado:
	
	reloj.tick(60)

	
	for event in pygame.event.get():
		if event.type == QUIT:
			estado = False
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				estado = False
			elif event.key == K_SPACE:
				common.scroll = True
			elif event.key == K_UP:
				disparos_grupo.add(DisparoPlayer(autoJugador.rect.midtop))
				sonido_jugador.play()
		elif event.type == KEYUP and event.key == K_SPACE:
				common.scroll = False
		
	
	# Manejadores de autoJugador.
	teclas = pygame.key.get_pressed()
	if teclas[K_LEFT]:
		autoJugador.giro += common.DELTA
	if teclas[K_RIGHT]:
		autoJugador.giro -= common.DELTA

		
	
	# Creación de las plantas al juego.	
	plantas += 1
	if plantas >= 15 and common.scroll:
		objVarios_grupo.add(Planta())
		plantas = 0
		
	
	# Creación de los enemigos al juego.
	enemigos += 1
	if enemigos >= 100:
		enemigo_nuevo = CarEnemy(random.randint(220, 590), random.randint(0, 4),
								 disparos_enemigos_grupo, DisparoEnemy, sonido_enemigo)
		enemigos_grupo.add(enemigo_nuevo)
		enemigos = 0
		
	# Chequeamos las colisiones.
	for u in pygame.sprite.groupcollide(enemigos_grupo, disparos_grupo, 1, 1):
		(x, y) = u.rect.center
		objVarios_grupo.add(Boom(x,y))
		sonido_explosion.play()
		
	for u in pygame.sprite.groupcollide(jugador_grupo, disparos_enemigos_grupo, 1, 1):
		(ps, py) = u.rect.center
		objVarios_grupo.add(Boom(ps, py))
		sonido_explosion.play()
		#jugador_grupo.add(autoJugador)
	
	fondo_grupo.update()
	jugador_grupo.update()
	enemigos_grupo.update()
	disparos_grupo.update()
	disparos_enemigos_grupo.update()
	objVarios_grupo.update()
	
	
	fondo_grupo.draw(screen)
		    
	jugador_grupo.draw(screen)
	enemigos_grupo.draw(screen)
	disparos_grupo.draw(screen)
	disparos_enemigos_grupo.draw(screen)
	objVarios_grupo.draw(screen)
	
	pygame.display.update()
	
