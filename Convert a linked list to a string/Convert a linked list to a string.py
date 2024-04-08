def stringify(node):
    st=""
    head=node
    while head!=None:
        st+=str(head.data)+" -> "
        head=head.next
    return st+"None"
