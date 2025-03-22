from linkedlist import LinkedList

def main():
    ll = LinkedList()
    ll.insert_at_start(50)
    ll.insert_at_end(20)
    ll.insert_at_end(40)
    ll.display()
    ll.insert_at_location(40,100)
    ll.display()

    ll.delete_value(20)
    ll.display()

    ll.update_first(90)
    ll.display()

    ll.update_at_location(40,200)
    ll.display()

    ll.isempty()
    ll.total_elements()


if __name__ == '__main__':
    main()