class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
def reverse(head):
    new=None
    link=None
    while head!=None:
        new=Node(head.data,link)
        link=new
        head=head.next
    return new
def alternating_split(head):
    rev=reverse(head)
    one=rev
    two=rev.next
    link=None
    while one!=None:
        frst=Node(one.data,link)
        link=frst
        one=one.next
        if one==None:
            break
        one=one.next
    link=None
    while two!=None:
        scnd=Node(two.data,link)
        link=scnd
        two=two.next
        if two==None:
            break
        two=two.next
    if frst.data==head.data:
        return Context(frst,scnd)
    else:
        return Context(scnd,frst)
