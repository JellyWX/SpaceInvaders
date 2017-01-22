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

  gui = GUI(1200,700,'SpaceInvaders')
  player = Player(3,gui)

  im = pygame.image.load('spaceinvader1.png')
  im = pygame.transform.scale(im,(28,22))
  enemy = [
    Enemy(gui.width*0.2,24,gui,im),
    Enemy(gui.width*0.3,24,gui,im),
    Enemy(gui.width*0.4,24,gui,im),
    Enemy(gui.width*0.5,24,gui,im),
    Enemy(gui.width*0.6,24,gui,im),
    Enemy(gui.width*0.7,24,gui,im),
    Enemy(gui.width*0.8,24,gui,im),

    Enemy(gui.width*0.25,58,gui,im,-2),
    Enemy(gui.width*0.35,58,gui,im,-2),
    Enemy(gui.width*0.45,58,gui,im,-2),
    Enemy(gui.width*0.55,58,gui,im,-2),
    Enemy(gui.width*0.65,58,gui,im,-2),
    Enemy(gui.width*0.75,58,gui,im,-2),
    Enemy(gui.width*0.85,58,gui,im,-2),

    Enemy(gui.width*0.2,92,gui,im),
    Enemy(gui.width*0.3,92,gui,im),
    Enemy(gui.width*0.4,92,gui,im),
    Enemy(gui.width*0.5,92,gui,im),
    Enemy(gui.width*0.6,92,gui,im),
    Enemy(gui.width*0.7,92,gui,im),
    Enemy(gui.width*0.8,92,gui,im)
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
        if laser[-1].life < 65:
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
        if b.x - 14 < i.x < b.x + 14:
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
