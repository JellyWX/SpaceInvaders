import pygame
from gui import GUI
from player import Player
from enemy import Enemy
from laser import Laser

def mainLoop():
  global gui
  global player
  global enemy
  global laser

  gui = GUI(1200,700,'SpaceInvaders')
  player = Player(3,gui)

  enemy = [
    Enemy(gui.width*0.2,10,gui),
    Enemy(gui.width*0.3,10,gui),
    Enemy(gui.width*0.4,10,gui),
    Enemy(gui.width*0.5,10,gui),
    Enemy(gui.width*0.6,10,gui),
    Enemy(gui.width*0.7,10,gui),
    Enemy(gui.width*0.8,10,gui)
    ]

  laser = [Laser(0,0,0,gui)]
  laser[0].life = 0

  done = False

  while not done:
    for e in gui.event():
      if e.type == pygame.QUIT:
        done = True
        break

    if gui.keysDown(pygame.K_LEFT):
      player.LEFT()
    if gui.keysDown(pygame.K_RIGHT):
      player.RIGHT()
    if gui.keysDown(pygame.K_UP):
      try:
        if laser[-1].life < 60:
          laser.append(Laser(player.x,player.y - 16,-12,gui))
      except:
        laser.append(Laser(player.x,player.y,-16,gui))
    if gui.keysDown(pygame.K_ESCAPE):
      done = True

    for i in laser:
      i.move()
      if i.life < 0:
        laser.remove(i)
      for b in enemy:
        if b.x - 10 < i.x < b.x + 10:
          if b.y < i.y < b.y+20:
            b.alive = False
            i.life = 0
    for b in enemy:
      b.move()
      if not b.alive:
        enemy.remove(b)

    gui.page.fill((0,0,0))

    for b in enemy:
      b.render()
    player.render()
    for i in laser:
      i.render()

    gui.flip(30)

mainLoop()
