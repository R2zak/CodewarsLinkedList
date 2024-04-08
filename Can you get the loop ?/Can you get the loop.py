def loop_size(node):
    slow=node.next
    fast=node.next.next
    while slow!=fast:
        slow = slow.next
        fast = fast.next.next
    ln = 1
    fast = fast.next
    while slow != fast:
        ln += 1
        fast = fast.next
    return ln
