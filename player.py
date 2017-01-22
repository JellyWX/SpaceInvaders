class Player(object):
  def __init__(self,l,gui):
    self.lives = l
    self.gui = gui
    self.x = self.gui.width/2
    self.y = self.gui.height - 70

  def LEFT(self):
    if self.x < 0:
      pass
    else:
      self.x -= 6

  def RIGHT(self):
    if self.x > self.gui.width:
      pass
    else:
      self.x += 6

  def render(self):
    self.gui.Color('ffffff')
    self.gui.Rect(self.x - 40,self.y,80,45)
    self.gui.Rect(self.x - 5,self.y - 10,10,55)
