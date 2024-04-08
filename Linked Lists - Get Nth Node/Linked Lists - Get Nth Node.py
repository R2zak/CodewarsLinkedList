from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if not isinstance(node,Node):
        raise LinkedError
    nn=node
    count=0
    while count!=index and nn.next!=None:
        nn=nn.next
        count+=1
    if count<index or index<0:
        raise ValueError
    return nn
  
