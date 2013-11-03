from vector2 import Vector2
#import pygame
#from pygame.locals import *

class Wind(object):
	
	def __init__(self,velocity):
		self.velocity=velocity
		self.direction=Vector2((0,0))
	def get_dir(self,leaf,pos):
		self.direction=Vector2.from_points(pos,leaf)
		self.magnitude=self.direction.get_magnitude()
		self.direction.normalize()
		#print self.direction	

