from functools import reduce


l = [1,2,3,4,5]

doubles = list(map(lambda n : n*2,l))

print(doubles)



sum = reduce(lambda a,b,: a+b,doubles)


print(sum)