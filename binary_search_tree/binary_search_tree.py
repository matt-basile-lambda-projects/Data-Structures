class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check is the new node's value is less than the our current node's value
    if value < self.value:
      # check if there is no left child
      if not self.left:
        #park the new_node here
        self.left = BinarySearchTree(value)
      else:
        #otherwise keep traversing down
        self.left.insert(value)
    # do the same on the right side if the node's value >= the current node's value
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target is self.value:
      return True
    elif target < self.value:
      if self.left is None:
        return False
      else:
        return self.left.contains(target)
    else:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)
    

  def get_max(self):
    max = self
    while max.right:
      max = max.right
    return max.value


  def for_each(self, cb):
    # while index > 0:
    self.value = cb(self.value)
    if self.left:
        self.left.for_each(cb)
    if self.right:
        self.right.for_each(cb)

      
