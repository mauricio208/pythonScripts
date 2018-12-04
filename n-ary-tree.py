class Tree:
    def __init__(self, data=None):
        self.__childs = [] #leafs
        self.data = data
    
    def add_childs(self, *node_values):
      """
        Add n leafs to actual tre been n = node_values
        return a list with all leaf added
      """
      for v in node_values:
        self.__childs.append(Tree(v))
      return self.__childs
    
    def childs(self):
      """
        return childs of this node
      """
      return self.__childs

    def draw(self, nodes=None):
      if not nodes:
        nodes = [self]
      
      str_nodes = []
      new_nodes = []

      for n in nodes:
        
        str_nodes.append(n.data if n else ' ')

        if n:
          for cn in n.childs():
            new_nodes.append(cn)

      print(' '.join([str(s) for s in str_nodes]))
      
      if new_nodes:
        return self.draw(new_nodes)
      

    def __str__(self):

      return "-> {}   \n {} ".format(self.data, ' '.join([str(c.data) for c in self.childs()]))
    
    def __repr__(self):
      return self.__str__()
        

if __name__ == "__main__":
    t = Tree(1)
    c1 = t.add_childs(11,12,13,14)
    c11 = c1[0].add_childs(111,112,113)
    c14 = c1[3].add_childs(141, 142)
