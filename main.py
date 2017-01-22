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

  enemy = Enemy(gui.width/2,10,gui)

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
          laser.append(Laser(player.x,player.y,-10,gui))
      except:
        laser.append(Laser(player.x,player.y,-10,gui))
    if gui.keysDown(pygame.K_ESCAPE):
      done = True

    enemy.move()
    for i in laser:
      i.move()
      if i.life < 0:
        laser.remove(i)

    gui.page.fill((0,0,0))

    enemy.render()
    player.render()
    for i in laser:
      i.render()

    gui.flip(30)

mainLoop()
