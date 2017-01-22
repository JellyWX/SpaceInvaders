class Enemy(object):
  def __init__(self,x,y,gui,im,dire=2):
    self.alive = True
    self.x = x
    self.y = y
    self.gui = gui
    self.disx = 0
    self.dir = dire
    self.desc = False
    self.im = im

  def move(self):
    if self.disx > 100 or self.desc:
      self.desc = True
      self.y += 4
      self.dir *= -1
      self.disx -= 15
      if self.disx < 0:
        self.desc = False
    else:
      self.x += self.dir
      self.disx += 1

  def render(self):
    if self.alive:
      self.gui.page.blit(self.im,(self.x - 14,self.y - 14))
