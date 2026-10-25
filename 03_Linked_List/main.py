from linked_list import LinkedList

linked_list = LinkedList()

linked_list.insert_at_front(2)
linked_list.insert_at_front(1)
linked_list.insert_at_end(3)

linked_list.insert_at_anywhere(3, 32)

linked_list.search(1)
linked_list.update(1, 333)
# linked_list.delete_by_position(1)
linked_list.delete_by_value(2)
linked_list.traversal()