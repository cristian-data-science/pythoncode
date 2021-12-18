from functools import reduce

my_list = [2, 2, 2, 2, 2, 2]

funcc = reduce(lambda x, y : x*y, my_list )

# multi = 1
# for i in my_list:
#     multi = multi * i

print(funcc)