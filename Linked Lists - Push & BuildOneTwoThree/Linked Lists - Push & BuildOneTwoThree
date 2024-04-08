from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    new=Node(data)
    new.next=head
    return new
def build_one_two_three():
    head=None
    for i in range(3,0,-1):
        nod=Node(i)
        nod.next=head
        head=nod
    return nod
