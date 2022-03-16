from Arrays.arrays import Array
from linked_lists.singly_list import SinglyLinkedList as SLL


def run():
    array = Array(10)
    list = SLL()
    array.rand_fill(20, 1000)
    for i in array:
        list.append(i)
    print('Array\n', array)
    print('Lista\n', list)


if __name__ == '__main__':
    run()
