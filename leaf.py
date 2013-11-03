import pygame
from pygame.locals import *
import math
from vector2 import Vector2
from wind import Wind


class Leaf(object):

	def __init__(self,x,y,velocity,picture):
		self.x=x
		self.surface_collision=False
		self.side_collision=False
		self.y=y
		self.velocity=velocity
		self.lvel=0
		self.rvel=0
		self.picture=picture
		self.image=pygame.image.load(self.picture).convert_alpha()
		self.w,self.h=self.image.get_width(),self.image.get_height()
		
		
		
		
	def render(self,surface):
		
		surface.blit(self.image,(self.x-self.w/2,self.y-self.h/2))
		#pygame.draw.rect(surface,(255,0,0,50),(self.x-25,self.y-25,50,50))
		
	def get_pos(self):
		return (self.x,self.y)
	
		
	def fall(self):
		self.x=self.x+self.velocity.x
		self.y=self.y+self.velocity.y
	def wind_affect(self,wind):
		self.velocity+=wind.direction*(10./wind.magnitude)
	def collision_check(self,hurdle):
		
		if self.x+25>hurdle.x and self.x-25<hurdle.x and self.y+25>hurdle.y and self.y-25<hurdle.y:
			print "collision detected"
			angle=math.acos(self.velocity.y/self.velocity.get_magnitude())
			print "incident angle : ",angle*(180/3.14)
			if self.x+22>hurdle.x:	#This stuff works!!!!	see glitches.txt		
				self.velocity.y*=-1
				
			else:
				
				self.velocity.x*=-1
		elif self.x+25>hurdle.x and self.x-25<hurdle.x and self.y+25>hurdle.y+20 and self.y-25<hurdle.y+20:
			print "collision detected"
			angle=math.acos(self.velocity.y/self.velocity.get_magnitude())
			print "incident angle : ",angle*(180/3.14)
			if self.x+22>hurdle.x:
				self.velocity.y*=-1
			else:
				self.velocity.x*=-1
		elif self.x-25<hurdle.x+100 and self.x+25>hurdle.x+100 and self.y+25>hurdle.y and self.y-25<hurdle.y:
			print "collision detected"
			angle=math.acos(self.velocity.y/self.velocity.get_magnitude())
			print "incident angle : ",angle*(180/3.14)
			if self.x-22<hurdle.x+100:
				self.velocity.y*=-1
			else:				
				self.velocity.x*=-1
		elif self.x-25<hurdle.x+100 and self.x+25>hurdle.x+100 and self.y+25>hurdle.y+20 and self.y-25<hurdle.y+20:
			print "collision detected"
			angle=math.acos(self.velocity.y/self.velocity.get_magnitude())
			print "incident angle : ",angle*(180/3.14)
			if self.x-22<hurdle.x+100:
				self.velocity.y*=-1
			else:
				self.velocity.x*=-1
		
		elif self.x+25<hurdle.x+100 and self.x-25>hurdle.x and self.y+25>hurdle.y and self.y+25<hurdle.y+20:
			self.velocity.y*=-1
		elif self.x+25<hurdle.x+100 and self.x-25>hurdle.x and self.y+25>hurdle.y+20 and self.y-25<hurdle.y+20:
			self.velocity.y*=-1
		if self.x-25<0 or self.x+25>640:
			self.velocity.x*=-1
		if self.y+25>480:
			self.velocity.y*=-1
	def simple_collision_check(self):
		if self.x-25<0 or self.x+25>640:
			self.velocity.x*=-1
		if self.y+25>480:
			self.velocity.y*=-1

