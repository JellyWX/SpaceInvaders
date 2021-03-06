import struct
from sys import exit
import pygame
from time import sleep

class GUI(object):
  def __init__(self,w,h,title):
    self.width = w
    self.height = h
    self.title = title
    self.color = (0,0,0)

    pygame.init()
    self.display = pygame.display
    self.page = self.display.set_mode((self.width,self.height))
    self.display.set_caption(self.title)

    self.f = None

  def Color(self,hexa):
    if type(hexa) is str:
      self.color = struct.unpack('BBB',bytes.fromhex(hexa))
    elif type(hexa) is tuple:
      self.color = hexa
    else:
      exit('ValueError: GUI.color only accepts str and tuple as inputs')

  def Text(self,t,s,anti=False):
    self.f = pygame.font.SysFont('ariel', s).render(t,anti,self.color)

  def Rect(self,x,y,w,h):
    pygame.draw.rect(self.page, self.color, pygame.Rect(x,y,w,h))

  def Circle(self,x,y,r):
    pygame.draw.circle(self.page, self.color, (x,y), r)

  def showText(self,x,y):
    self.page.blit(self.f, (x,y))

  def flip(self,t):
    self.display.flip()
    sleep(1/t)

  def event(self):
    return pygame.event.get()

  def keysDown(self,k=None):
    if k != None:
      return pygame.key.get_pressed()[k]
    else:
      return pygame.key.get_pressed()

  def mouseAction(self,k=None):
    if k != None:
      return pygame.mouse.get_pressed()[k]
    else:
      return pygame.mouse.get_pressed()
