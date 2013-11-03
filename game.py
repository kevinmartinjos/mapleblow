import pygame
from world import Hurdle
from vector2 import Vector2
from pygame.locals import *
from sys import exit
from leaf import Leaf
from wind import Wind
import wx
start=False
def run_game(run_is_pressed):
	pygame.init()
	clock=pygame.time.Clock()
	screen=pygame.display.set_mode((640,480))
	picture='leaf.png'
	blocks=[]
	i=0
	while i<5:
		#blocks.append(Hurdle())
		i=i+1
	SCREEN_SIZE=(screen.get_width(),screen.get_height())
	leaf_velocity=Vector2((0,0.5))
	maple=Leaf(SCREEN_SIZE[0]/2,0,leaf_velocity,picture)
	print maple.w,maple.h
	gale=Wind(0)
	while True:
		for event in pygame.event.get():
			if event.type==QUIT:
				exit()
			elif pygame.mouse.get_pressed()[0]:
			
				pos=pygame.mouse.get_pos()
			
				gale.get_dir(maple.get_pos(),pos)
				maple.wind_affect(gale)
			elif pygame.mouse.get_pressed()[2]:
				maple.x=SCREEN_SIZE[0]/2
				maple.y=0
				maple.velocity=Vector2((0,0.2))
		
		clock.tick(60)	
		screen.fill((255,255,255))	
		maple.render(screen)
		i=0
		#while(i<5):
			#blocks[i].render(screen)
		maple.simple_collision_check()
		#	i=i+1
		maple.fall()
		pygame.display.update()
def show_help(info_pressed):
	wx.MessageBox('Welcome to Maple Blow. Maple Blow is a simple program which lets you control a maple leaf floating in the air. Click anywhere inside the playing area and an imaginary wind (yeah, Imaginary) will blow from that point to the centre of the leaf.The closer you click to the leaf, the stronger the wind that blows. As of now, there is no particular \'objective\' associated with the program (that\' why i call it a program and not a game :D). In case the leaf go out of bounds, right click anywhere to reset','Help')
app=wx.App()
frame=wx.Frame(None,-1,'Leaves',size=(640,480))
def about_show(about_pressed):
	about_text=""" Maple Blow V 0.0001
		       Developer : Kevin Martin Jose
		       License:Freeware/Open Source
		       webpage:www.kevinkoder.tk"""
	wx.MessageBox(about_text,'About')

panel=wx.Panel(frame,-1)
run=wx.Button(panel,-1,'RUN',(280,220))
info=wx.Button(panel,0,'HELP',(280,180))
about=wx.Button(panel,1,'ABOUT',(280,260))
panel.Bind(wx.EVT_BUTTON,run_game,id=run.GetId())
panel.Bind(wx.EVT_BUTTON,about_show,id=about.GetId())
panel.Bind(wx.EVT_BUTTON,show_help,id=info.GetId())
frame.Show()
app.MainLoop()		
