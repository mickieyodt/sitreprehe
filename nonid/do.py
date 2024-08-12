my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
my_list = [x for i, x in enumerate(my_list) if x not in my_list[:i]]
print(my_list)  # [1, 2, 3, 4, 5, 6]
