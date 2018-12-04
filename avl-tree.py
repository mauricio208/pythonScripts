class Node:
  '''
    Class that represents the node of a binary tree
  '''
  def __init__(self, parent=None, data=None):
    self.parent = parent
    self.l = None
    self.r = None
    self.data = data
    self.h = 0
    
  def add_l(self, data):
    self.l = Node(('l',self), data)
    return self.l

  def add_r(self, data):
    self.r = Node(('r',self), data)
    return self.r

  def balance(self):
    lh = self.l.h if self.l else -1
    rh = self.r.h if self.r else -1
    return rh - lh
  
  def update_height(self):
    lh = self.l.h if self.l else -1
    rh = self.r.h if self.r else -1
    self.h = max(lh, rh)+1

  def __str__(self):

    l = self.l.data if self.l else ''
    r = self.r.data if self.r else ''
    return "-> {}   \n {}   {} ".format(self.data, l, r)
  
  def __repr__(self):
    return self.__str__()

class AVLTree:
  def __init__(self, order_f, data):
      self.__root = Node(data=data)
      self.__order_f = order_f
  
  def get(self, data, actual_node=None):
    actual_node = self.__root if not actual_node else actual_node
    if data == actual_node.data:
      return actual_node
    order = self.__order_f(actual_node.data, data)
    if order: # __order_f of actual node and new node is True : new node added on right leave
      next_node = actual_node.r
      if not next_node:
        return None
    else: # if __order_f is False : new node added on left leave
      next_node = actual_node.l
      if not next_node:
        return None
    
    return self.get(data, next_node)


  def add_node(self, data, actual_node=None):
    '''
      Traverse the tree structure until the correct place for the node is found, using __order_f to check the order of the new node
    '''
    actual_node = self.__root if not actual_node else actual_node
    order = self.__order_f(actual_node.data, data)
    if order: # __order_f of actual node and new node is True : new node added on right leave
      next_node = actual_node.r
      if not next_node:
        actual_node.add_r(data)
    else: # if __order_f is False : new node added on left leave
      next_node = actual_node.l
      if not next_node:
        actual_node.add_l(data)
    
    if not next_node:
      self.__height_update_balancing(order, actual_node)
      return actual_node
    
    added_node = self.add_node(data, next_node)
    self.__height_update_balancing(order, actual_node)
    return added_node


  def __height_update_balancing(self, order, actual_node):
    
    temporary_balance = actual_node.balance()

    if temporary_balance < -1:
      if actual_node.l.balance() <= 0:
        self.__ll_balance(actual_node)
      else:
        self.__lr_balance(actual_node)
    elif temporary_balance > 1:
      if actual_node.r.balance() >= 0:
        self.__rr_balance(actual_node)
      else:
        self.__rl_balance(actual_node)

    lh = actual_node.l.h if actual_node.l else -1
    rh = actual_node.r.h if actual_node.r else -1
    actual_node.h = max(lh, rh) + 1      


  def __ll_balance(self, actual_node):
    '''Left child left-heavy unbalance case, rotation to right for balance'''
    self.__rotate_right(actual_node)


  def __rr_balance(self, actual_node):
    '''Right child right-heavy unbalance case, rotation to left for balance'''
    self.__rotate_left(actual_node)


  def __lr_balance():
    pass


  def __rl_balance():
    pass


  def __rotate_left(self, parent_node):
    '''AVL rotation to left from parent_node'''

    new_parent = parent_node.r #right child of unbalanced node will bee subtree's root
    new_right_child = new_parent.l #left child of new subtree's root node will be transfered to old root

    new_parent.l = parent_node #unbalanced node transfered to be left child of new subtree's root node
    new_parent.l.r = new_right_child #assigning old left child of subtree's root node to be right child of unbalanced node

    #updating parent reference
    if new_right_child:
      new_right_child.parent = ('r', new_parent.l) 
    grandfather_node = parent_node.parent
    parent_node.parent = ('l',new_parent)
    self.__assign_to_grandfather(grandfather_node, new_parent)

    #updating height of nodes of interest
    parent_node.update_height()
    new_parent.update_height()
    
  
  def __rotate_right(self, parent_node):
    '''AVL rotation to right from parent_node'''

    new_parent = parent_node.l #left child of unbalanced node will bee subtree's root
    new_left_child = new_parent.r #right child of new subtree's root node will be transfered to old root

    new_parent.r = parent_node #unbalanced node transfered to be right child of new subtree's root node
    new_parent.r.l = new_left_child #assigning old right child of subtree's root node to be left child of unbalanced node

    #updating parent reference
    if new_left_child:
      new_left_child.parent = ('l', new_parent.r)
    grandfather_node = parent_node.parent
    parent_node.parent = ('r',new_parent)
    self.__assign_to_grandfather(grandfather_node, new_parent)

    #updating height of nodes of interest
    parent_node.update_height()
    new_parent.update_height()


  def __assign_to_grandfather(self, grandfather_node, new_parent):
    '''grandfather_node will be assigned to new_parent.parent'''

    if not grandfather_node:
      new_parent.parent = None
      self.__root = new_parent
    else:
      if grandfather_node[0] == 'l':
        new_parent.parent = ('l', grandfather_node)
        grandfather_node[1].l=new_parent
      else:
        new_parent.parent = ('r', grandfather_node)
        grandfather_node[1].r=new_parent


  def draw(self, height=False, balance=False, nodes=None,):
    if not nodes:
      nodes = [self.__root]
    
    str_nodes = []
    new_nodes = []

    for n in nodes:
      if height:
        str_nodes.append(n.height if n else '-')
      elif balance:
        if n:
          str_nodes.append(n.balance())
        else:
          str_nodes.append('-')
      else:
        str_nodes.append(n.data if n else '-')


      if n:
        new_nodes.append(n.l)
        new_nodes.append(n.r)

    print(' '.join([str(s) for s in str_nodes]))
    
    if new_nodes:
      return self.draw(height, balance, new_nodes)
    

        

if __name__ == "__main__":
    
    t = AVLTree((lambda a,b: b>a),100)
    # t.add_node(1)
    # t.add_node(200)
    # t.add_node(11)
    # t.add_node(111)
    # t.add_node(112)
    t.add_node(101)
