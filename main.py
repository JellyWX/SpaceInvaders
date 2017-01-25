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
  global im

  gui = GUI(1200,700,'PyInvaders')
  player = Player(3,gui)

  im = pygame.image.load('spaceinvader1.png')
  im = pygame.transform.scale(im,(36,28))

  enemy_loc = [36,81,126,171,216]
  enemy = []
  emeny_laser = Laser(0,0,0,gui)

  for x in range(0,4):
    for y in range(0,10):
      enemy.append(Enemy(gui.width*(y*0.05+0.25),enemy_loc[x],gui,im))

  laser = Laser(0,0,0,gui)
  laser.alive = False

  done = False

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
    for b in enemy:
      b.move()
      if not b.alive:
        enemy.remove(b)

    gui.page.fill(0x000000)

    for b in enemy:
      b.render()
    player.render()
    if laser.alive:
      laser.render()

    gui.flip(30)

mainLoop()
