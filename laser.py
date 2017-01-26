class Laser(object):
  def __init__(self,x,y,direction,gui):
    self.x = x
    self.y = y
    self.dir = direction
    self.gui = gui
    self.alive = True

  def move(self):
    self.y += self.dir
    if self.y > self.gui.height or self.y < 0:
      self.alive = False

  def render(self):
    self.gui.Rect(self.x - 4,self.y - 12,8,24)
