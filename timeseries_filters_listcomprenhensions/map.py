my_list  = [1,5,10,20,1000]

#square = [i**2 for i in list]

square = list(map(lambda x: x**2, my_list))

print(square)
