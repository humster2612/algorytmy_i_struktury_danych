    current = head
    prev = None
    pos = 1

    while current is not None and pos < i:
        prev = current
        current = current.next
        pos += 1

    if current is None:
        return head

    if prev is not None:
        prev.next = current.next
    else:
        head = current.next

    return head


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = usun_wezel(head, 2)

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
