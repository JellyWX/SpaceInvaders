import pygame
from gui import GUI
from player import Player

def mainLoop():
  global gui
  global player

  gui = GUI(1200,700,'SpaceInvaders')
  player = Player(3,gui)

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
    if gui.keysDown(pygame.K_ESCAPE):
      done = True

    gui.page.fill((0,0,0))

    player.render()

    gui.flip(30)

mainLoop()
