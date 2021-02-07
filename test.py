from linked_list import LinkedList, sort_linked_list

l = LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

l.add_front(-99)
l.add_back(99)
l.insert(6, 50)
print(l)
assert list(l) == [-99, 0, 1, 2, 3, 4, 50, 5, 6, 7, 8, 9, 99]

n2 = l.get_i_node(3)
n2.swap_with_prev()
n2.swap_with_prev()
print(l)
assert list(l) == [-99, 2, 0, 1, 3, 4, 50, 5, 6, 7, 8, 9, 99]

n7 = l.get_i_node(9)
n7.swap_with_next()
n7.swap_with_next()
print(l)
assert list(l) == [-99, 2, 0, 1, 3, 4, 50, 5, 6, 8, 9, 7, 99]

n8 = l.get_i_node(10)
n8.swap_with_prev()
print(l)
assert list(l) == [-99, 2, 0, 1, 3, 4, 50, 5, 6, 9, 8, 7, 99]

n3 = l.get_i_node(4)
n3.insert_before(-3)
n3.insert_after(33)
print(l)
assert list(l) == [-99, 2, 0, 1, -3, 3, 33, 4, 50, 5, 6, 9, 8, 7, 99]

n_99 = l.get_i_node(0)
n99 = l.get_i_node(-1)

for i in range(len(l)-1):
    n_99.swap_with_next()
print(l)
assert list(l) == [2, 0, 1, -3, 3, 33, 4, 50, 5, 6, 9, 8, 7, 99, -99]

for i in range(len(l)-2):
    n99.swap_with_prev()
print(l)
assert list(l) == [99, 2, 0, 1, -3, 3, 33, 4, 50, 5, 6, 9, 8, 7, -99]

l.pop_front()
l.pop_back()
print(l)
assert list(l) == [2, 0, 1, -3, 3, 33, 4, 50, 5, 6, 9, 8, 7]

sort_linked_list(l)
print(l)
assert list(l) == [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 33, 50]


n_3 = l.get_i_node(0)
n33 = l.get_i_node(11)
n50 = l.get_i_node(12)

n_3.remove()
n33.remove()
n50.remove()
print(l)
assert list(l) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]