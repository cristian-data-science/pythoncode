list2 = [1,2,5,6,7,9,11,12,15,20,33,40,50,60,70]


#impar = [i for i in list if i % 2 != 0]

impar = list(filter(lambda x: x%2 != 0, list2))

print(impar)

