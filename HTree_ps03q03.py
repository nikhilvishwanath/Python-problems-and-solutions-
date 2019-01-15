from Tree import *
class HTree(Tree):

  def  __init__(self,v=None,l=None,r=None):
    if v == None:
      self.value = None
      self.left = None
      self.right = None
      self.height = 0
      self.count = -1
    else:
      if l == None:
        l = HTree()
      if r == None:
        r = HTree()
      self.left = l
      self.right = r
      self.value = v
      self.fixheight()

  def fixheight(self):
    if self.isempty():
      self.height = 0
    else:
     self.height = 1 + max(self.left.height,self.right.height)


  def __str__(self):
    if self.isempty():
      return ("E")
    return("( "+"["+str(self.value)+","+str(self.height)+","+str(self.count)+"]"+" "+str(self.left)+" "+str(self.right)+" )")

  def rotateright(self):
    if self.left.isempty():
      return
    tmp = self.left
    self.left = tmp.left
    self.value,tmp.value = tmp.value,self.value
    tmp.left = tmp.right
    tmp.right = self.right
    self.right = tmp
    self.right.fixheight()
    self.fixheight()

  def rotateleft(self):
    if self.right.isempty():
      return
    tmp = self.right
    self.right = tmp.right
    self.value,tmp.value = tmp.value,self.value
    tmp.right = tmp.left
    tmp.left = self.left
    self.left= tmp
    self.left.fixheight()
    self.fixheight()

  def slope(self):
    return self.left.height - self.right.height

  def rebalance(self):
    if self.isempty():
      return
    if (self.slope() == 2):
      if self.left.slope() >= 0:
        self.rotateright()
      else:
        self.left.rotateleft()
        self.fixheight()
        self.rotateright()
    elif (self.slope() == -2):
      if self.right.slope() <= 0:
        self.rotateleft()
      else:
        self.right.rotateright()
        self.fixheight()
        self.rotateleft()
