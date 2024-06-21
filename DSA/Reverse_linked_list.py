# it is program to reverse the Linked list 
# Input : 1 -> 2 -> 3 -> 4 -> 5
# Output : 5 -> 4 -> 3 -> 2 -> 1

class LinkedList:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
    
def reverse_linked_list(head):
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev

lst = [1,2,3,4,5]
node = LinkedList(lst[0])
cur = node
for i in range(1,len(lst)):
    cur.next = LinkedList(lst[i])
    cur = cur.next

rev = reverse_linked_list(node)
ans = []
while rev:
    ans.append(rev.val)
    rev = rev.next
print(ans)