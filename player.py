class Player(object):
  def __init__(self,l,gui):
    self.lives = l
    self.gui = gui
    self.x = self.gui.width/2
    self.y = self.gui.height - 70

  def LEFT(self):
    self.x -= 6

  def RIGHT(self):
    self.x += 6

  def render(self):
    self.gui.Color('eeeeee')
    self.gui.Rect(self.x - 45,self.y,90,45)
    self.gui.Rect(self.x - 5,self.y - 10,10,55)
