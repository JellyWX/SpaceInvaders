class Enemy(object):
  def __init__(self,x,y,gui):
    self.alive = True
    self.x = x
    self.y = y
    self.gui = gui
    self.disx = 0
    self.dir = 2
    self.desc = False

  def move(self):
    if self.disx > 90 or self.desc:
      self.desc = True
      self.y += 5
      self.dir *= -1
      self.disx -= 15
      if self.disx < 0:
        self.desc = False
    else:
      self.x += self.dir
      self.disx += 1

  def render(self):
    self.gui.Rect(self.x - 10,self.y - 10,20,20)
