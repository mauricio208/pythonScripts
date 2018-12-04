class Tree:
    def __init__(self, data=None):
        self.__l = None
        self.__r = None
        self.data = data
    
    def add_l(self, data):
      self.__l = Tree(data)
      return self.__l

    def add_r(self, data):
      self.__r = Tree(data)
      return self.__r
    
    def l(self):
      return self.__l
    
    def r(self):
      return self.__r

    def draw(self, nodes=None):
      if not nodes:
        nodes = [self]
      
      str_nodes = []
      new_nodes = []

      for n in nodes:
        
        str_nodes.append(n.data if n else ' ')

        if n:
          new_nodes.append(n.l())
          new_nodes.append(n.r())

      print(' '.join([str(s) for s in str_nodes]))
      
      if new_nodes:
        return self.draw(new_nodes)
      

    def __str__(self):

      l = self.__l.data if self.__l else ''
      r = self.__r.data if self.__r else ''
      return "-> {}   \n {}   {} ".format(self.data, l, r)
    
    def __repr__(self):
      return self.__str__()
        

if __name__ == "__main__":
    t = Tree(0)
    h1l=t.add_l(1)
    h1r=t.add_r(2)
    h2l=h1r.add_l(11)
    h2l.add_l(111)
    h2l.add_r(112)



