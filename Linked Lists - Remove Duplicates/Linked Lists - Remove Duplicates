class Node(object):
    def __init__(self, data,next=None):
        self.data = data
        self.next = next
def reverse(head):
    new=None
    link=None
    while head!=None:
        new=Node(head.data,link)
        link=new
        head=head.next
    return new
def remove_duplicates(head):
    link=None
    reve=reverse(head)
    new=None
    while reve!=None:
        if reve.next==None or reve.data!=reve.next.data:
            new=Node(reve.data,link)
            link=new
        reve=reve.next
    return new
