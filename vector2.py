import math

class Vector2(object):
	def __init__(self,(x,y)):
		self.x=x
		self.y=y
	def __str__(self):
		return "(%s,%s)"%(self.x,self.y)
	@staticmethod
	def from_points(p1,p2):
		return Vector2((p2[0]-p1[0],p2[1]-p1[1]))
	def get_magnitude(self):
		return math.sqrt(self.x**2+self.y**2)
	def normalize(self):
		magnitude=self.get_magnitude()
		self.x/=magnitude
		self.y/=magnitude
	def __add__(self,rhs):
		return Vector2((self.x+rhs.x,self.y+rhs.y))
	def __sub__(self,rhs):
		return Vector2((self.x-rhs.x,self.y-rhs.y))
	def __mul__(self,scalar):
		return Vector2((self.x*scalar,self.y*scalar))

