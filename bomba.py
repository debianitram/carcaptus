#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pygame
import common

# Clase que representa una explosión
class Boom(pygame.sprite.Sprite):
    """Representa una explosion de alguna nave."""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._load_images()
        self.step = 0
        self.delay = 2
        self.image = common.load_image('boom/1.png', True)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def _load_images(self):
        """Carga la lista 'self.frames' con todos los cuadros de animacion"""

        self.frames = []

        for n in range(1, 8):
            path = 'boom/%d.png'
            new_image = common.load_image(path % n, True)
            self.frames.append(new_image)

    def update(self):
        self.image = self.frames[self.step]

        if self.delay < 0:
            self.delay = 2
            self.step += 1

            if self.step > 6:
                self.kill()
        else:
            self.delay -= 1
