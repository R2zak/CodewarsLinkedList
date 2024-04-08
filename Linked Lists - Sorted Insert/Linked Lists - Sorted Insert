""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head==None or head.data>data:
        new=Node(data)
        new.next=head
        return new
    nn=head
    while nn.next!=None and nn.next.data<data:
        nn=nn.next
    new=Node(data)
    new.next=nn.next
    nn.next=new
    return head
