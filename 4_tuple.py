single_tuple = (5,)  # Correct
not_a_tuple = (5)    # Just an integer
print(type(single_tuple))  # <class 'tuple'>
print(type(not_a_tuple))   # <class 'int'>



my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)



t = (10, 20, 30, 40, 50)
print(t[0])     # 10
print(t[-1])    # 50
print(t[1:4])   # (20, 30, 40)



t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # 1 2 3



t = (1, 2, 3, 2, 2)
print(t.count(2))  # 3
print(t.index(3))  # 2




#   When to Use Tuples?
#  ✅ Use a tuple when:
# You want a fixed collection.
# You want to use it as a key in a dictionary (only immutable types can be keys).

