# What would we want in a text editor?
# Copy/Paste, Append Text, Delete Text.

# What Data Structure should we use as the basis fpr our text buffer.
# Linked List and Array

# Linked List Copy/

from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    #int gives us the option to initialize some text int the buffer off the bat
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        # check if an init string is provided
        # if so, put the contents of the init string in self.contents
        if init:
            for char in init:
                self.contents.add_to_tail(char)
    
    def __str__(self):
        # needs to return a string to print
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s
        
    def append(self, string_to_add):
        for char in string_to_add:
            self.contents.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in string_to_add[::-1]:
            self.contents.add_to_head(char)

    def delete_front(self,chars_to_remove):
        for _ in range(chars_to_remove):
            self.contents.remove_from_head()

    def delete_back(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.contents.remove_from_tail()

    """
    Joins other buffer to self
    The input buffer gets concatenated to the end of this buffer
    The tail of the concatenated buffer will be the tail of the other buffer
    The head of the concatenated buffer will be the head of this buffer
    """
    def join(self, other_buffer):
        # we might want tot check that other_buffer is indeed a text buffer
        # set self list's tail next_node to be head of other_buffer
        self.contents.tail.next = other_buffer.contents.head
        # set other_buffer head's prev node to be the tail of this buffer
        other_buffer.contents.head.prev = self.contents.tail
        other_buffer.contents.head = self.contents.head
        self.contents.tail = other_buffer.contents.tail

    # If we get fed a string instead ofa text buffer instance,
    # Initialize a new text buffer with this string and then
    # call the join method.
    def join_string(self, string_to_join):
        new_buffer = TextBuffer(string_to_join)
        self.join(new_buffer)

    

if __name__ == '__main__':
    text = TextBuffer("Super")
    print(text)

