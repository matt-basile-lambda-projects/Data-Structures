class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    if len(self.storage) is 1:
      return self.storage.pop()
    root = self.storage[0]
    self.storage[0] = self.storage.pop()
    self._sift_down(0)
    return root

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  # The Index is the index of the node whereever it is in the array/ 
  def _bubble_up(self, index):
    # loop until either the element reaches the top of the array 
    # or we'll break the loop when we realize the element's priority is not
    # not larger than its parent's value
    while index > 0:
      # the value at index fetches the index of its parent
      parent  = (index - 1) // 2
      # chec if the element at index has higher priority than the element at the parent in parent index
      if self.storage[index] > self.storage[parent]:
        #then we need to swap
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        # we also need to update the index
        index = parent
      else:
        # otherwise our element has reached a spot in the heap where its parent
        # element has higher priority: stop climbing
        break

  def _sift_down(self, index):
    # Make use of the left and right formulas^^
    base_array = self.storage
    ci = 2*index + 1
    if ci >len(base_array)-1:
      return
    if ci+1 <= len(base_array)-1 and base_array [ci+1] > base_array [ci]:
      ci += 1
    if base_array[index] < base_array[ci]:
      base_array[index], base_array[ci] = base_array[ci],base_array[index]
      self._sift_down(ci)
    else:
      return
