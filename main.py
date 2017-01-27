import pygame
import threading
import time
from random import random
from gui import GUI
from player import Player
from enemy import Enemy
from laser import Laser

gui = GUI(1200,700,'PyInvaders')
player = Player(2,gui)

im = pygame.image.load('spaceinvader1.png')
im = pygame.transform.scale(im,(36,28))

enemy_loc = [36,81,126,171,216]
enemy = []
enemy_laser = Laser(0,0,0,gui)
enemy_laser.alive = False

for x in range(0,4):
  for y in range(0,10):
    enemy.append(Enemy(gui.width*(y*0.05+0.25),enemy_loc[x],gui,im))

laser = Laser(0,0,0,gui)
laser.alive = False

done = False
rep = 0

def process_loop(delay):
  global enemy
  global enemy_laser
  global gui
  global player
  global laser
  global rep
  global done

  while not done:
    for e in gui.event():
      if e.type == pygame.QUIT:
        done = True
        break
      if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 4:
          player.LEFT()
        if e.button == 5:
          player.RIGHT()

    if gui.keysDown(pygame.K_LEFT):
      player.LEFT()
    if gui.keysDown(pygame.K_RIGHT):
      player.RIGHT()
    if gui.keysDown(pygame.K_UP) or gui.keysDown(pygame.K_SPACE):
      if not laser.alive:
        laser = (Laser(player.x,player.y - 16,-12,gui))
    if gui.keysDown(pygame.K_ESCAPE):
      done = True

    if laser.alive:
      laser.move()
      for b in enemy:
        if b.x - 18 < laser.x < b.x + 18:
          if b.y < laser.y < b.y + 20:
            b.alive = False
            laser.alive = False
    if enemy_laser.alive:
      enemy_laser.move()
      if player.x - 40 < enemy_laser.x < player.x + 40:
        if enemy_laser.y > gui.height - 70:
          player.life()
          enemy_laser.alive = False
    for b in enemy:
      b.move()
      if not b.alive:
        enemy.remove(b)
        continue
      r = random()
      if r > 0.9995 - rep*0.00001 and not enemy_laser.alive:
        enemy_laser = Laser(b.x,b.y,14,gui)

    if player.lives < 0:
      done = True
      gameover()

    rep += 1
    time.sleep(1/delay)

def gameover():
  global gui
  global done

  end = False

  while done and not end:
    for e in gui.event():
      if e.type == pygame.QUIT:
        end = True

    gui.page.fill(0x000000)

    text = gui.Text('GAMEOVER',120,True)
    gui.showText(gui.width/2 - gui.f.get_width()/2,gui.height/2 - 60)

    gui.flip(20)

def render_loop(delay):
  global enemy
  global enemy_laser
  global gui
  global player
  global laser
  global rep
  global done
  while not done:
    gui.page.fill(0x000000)
    for b in enemy:
      b.render()
    player.render()
    if laser.alive:
      laser.render()
    if enemy_laser.alive:
      enemy_laser.render()

    gui.flip(delay)


class main(threading.Thread):
  def __init__(self,threadID,func,delay):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.func = func
    self.delay = delay
  def run(self):
    self.func(self.delay)


thread1 = main(1,process_loop,30)
thread2 = main(2,render_loop,300)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
