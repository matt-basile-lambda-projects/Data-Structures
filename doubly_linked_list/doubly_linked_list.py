"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next
  # def __str__(self):
  #   return f"Value: {self.value}, Prev: {self.prev}, Next: {self.next}"
  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0
  # def __str__(self):
  #   return f"Head:{self.head.value}, Tail:{self.tail.value}"
  def __len__(self):
    return self.length

  def add_to_head(self, value):
    current = self.head
    if current is None:
      self.head = ListNode(value)
    else:
      self.head.insert_before(value)
      self.head = current.prev
      
    
  def remove_from_head(self):
    if self.head is None:
      return None
    else:
      current = self.head
      self.head.delete()
      return current.value

  def add_to_tail(self, value):
    current = self.tail
    if self.head is None:
      added = ListNode(value)
      self.tail = added
      self.head = added
    else: 
      current.insert_after(value)
      self.tail = current.next

  def remove_from_tail(self):
    if self.tail is None:
      return None
    if self.head == self.tail:
      tail = self.tail
      self.head = None
      self.tail = None 
      return tail.value
    else:
      tail = self.tail
      self.tail.delete()
      self.tail = self.tail.prev
      return tail.value

  def move_to_front(self, node):
    if self.head is not None:
      current_head = self.head
      self.head = node
      node.next = current_head
      current_head.prev = node

  def move_to_end(self, node):
    if self.tail is not None:
      current_tail = self.tail
      self.tail = node
      node.prev = current_tail
      current_tail.prev = node

  def delete(self, node):
    if self.head is None and self.tail is None:
      return None
    if self.head == self.tail:
      self.head = None
      self.tail = None
    if self.head == node:
      self.head = node.next
      node.delete()
    if self.tail == node:
      self.tail = node.prev
      node.delete()
    else:
      node.delete()
    
  def get_max(self):
    max = 0
    current = self.head
    if self.head == None:
      return None
    if self.head == self.tail:
      return self.head.value
    while current:
      if current.value > max:
        max = current.value
      current = current.next
    return max

ln = ListNode(1)
dll = DoublyLinkedList(ln)
# print('Node:', ln)
print('DLL:', dll)
dll.remove_from_tail()
print('DLL_Head:', dll.head, 'DLL_Tail:', dll.tail, 'length:', len(dll))

