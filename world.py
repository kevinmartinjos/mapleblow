import pygame
from random import randint
from pygame.locals import *
from sys import exit

class World(object):
		def __init__(self,screen):
			screen.fill((255,255,255))
		

class Hurdle(object):
	def __init__(self):
		self.x=randint(100,600)
		self.y=randint(20,440)
	def render(self,screen):
		pygame.draw.rect(screen,(118,19,27),(self.x,self.y,100,20))

		
		 
		                                                            
