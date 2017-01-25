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

  enemy = [
    Enemy(gui.width*0.35,enemy_loc[0],gui,im),
    Enemy(gui.width*0.4,enemy_loc[0],gui,im),
    Enemy(gui.width*0.45,enemy_loc[0],gui,im),
    Enemy(gui.width*0.5,enemy_loc[0],gui,im),
    Enemy(gui.width*0.55,enemy_loc[0],gui,im),
    Enemy(gui.width*0.6,enemy_loc[0],gui,im),
    Enemy(gui.width*0.65,enemy_loc[0],gui,im),

    Enemy(gui.width*0.35,enemy_loc[1],gui,im),
    Enemy(gui.width*0.4,enemy_loc[1],gui,im),
    Enemy(gui.width*0.45,enemy_loc[1],gui,im),
    Enemy(gui.width*0.5,enemy_loc[1],gui,im),
    Enemy(gui.width*0.55,enemy_loc[1],gui,im),
    Enemy(gui.width*0.6,enemy_loc[1],gui,im),
    Enemy(gui.width*0.65,enemy_loc[1],gui,im),

    Enemy(gui.width*0.35,enemy_loc[2],gui,im),
    Enemy(gui.width*0.4,enemy_loc[2],gui,im),
    Enemy(gui.width*0.45,enemy_loc[2],gui,im),
    Enemy(gui.width*0.5,enemy_loc[2],gui,im),
    Enemy(gui.width*0.55,enemy_loc[2],gui,im),
    Enemy(gui.width*0.6,enemy_loc[2],gui,im),
    Enemy(gui.width*0.65,enemy_loc[2],gui,im),

    Enemy(gui.width*0.35,enemy_loc[3],gui,im),
    Enemy(gui.width*0.4,enemy_loc[3],gui,im),
    Enemy(gui.width*0.45,enemy_loc[3],gui,im),
    Enemy(gui.width*0.5,enemy_loc[3],gui,im),
    Enemy(gui.width*0.55,enemy_loc[3],gui,im),
    Enemy(gui.width*0.6,enemy_loc[3],gui,im),
    Enemy(gui.width*0.65,enemy_loc[3],gui,im),

    Enemy(gui.width*0.35,enemy_loc[4],gui,im),
    Enemy(gui.width*0.4,enemy_loc[4],gui,im),
    Enemy(gui.width*0.45,enemy_loc[4],gui,im),
    Enemy(gui.width*0.5,enemy_loc[4],gui,im),
    Enemy(gui.width*0.55,enemy_loc[4],gui,im),
    Enemy(gui.width*0.6,enemy_loc[4],gui,im),
    Enemy(gui.width*0.65,enemy_loc[4],gui,im)
    ]


  laser = []

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
    if gui.keysDown(pygame.K_UP) or gui.keysDown(pygame.K_SPACE):
      if len(laser) == 0:
        laser.append(Laser(player.x,player.y - 16,-12,gui))
    if gui.keysDown(pygame.K_ESCAPE):
      done = True

    for i in laser:
      i.move()
      if i.y < 0:
        laser.remove(i)
      if i.life < 0:
        laser.remove(i)
      for b in enemy:
        if b.x - 18 < i.x < b.x + 18:
          if b.y < i.y < b.y + 20:
            b.alive = False
            i.life = 0
    for b in enemy:
      b.move()
      if not b.alive:
        enemy.remove(b)

    gui.page.fill(0x000000)

    for b in enemy:
      b.render()
    player.render()
    for i in laser:
      i.render()

    gui.flip(30)

mainLoop()
