class Laser(object):
  def __init__(self,x,y,direction,gui):
    self.x = x
    self.y = y
    self.dir = direction
    self.gui = gui
    self.life = 80

  def move(self):
    self.y += self.dir
    self.life -= 1

  def render(self):
    self.gui.Rect(self.x - 3,self.y - 6,6,12)
