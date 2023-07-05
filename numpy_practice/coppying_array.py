from numpy import*


# 1.how to add a number to each values of an array

# arr = array([1,2,3,4,5,6])
#
# arr2 = arr+2
#
# print(arr2)

# out_put = [ 6  7  8  9 10 11]


# 2. How to add two arrays each other

# arr = array([1,2,3,4,5,6])
#
# arr2 = array([2,4,6,8,10,12])
#
# arr3 = arr+arr2
#
# print(arr3)

# output = [ 3  6  9 12 15 18]



# 3. concatenation of arrays


# arr = array([1,3,5,7,9])
#
# arr2 = array([2,4,6,8,10])
#
# print(concatenate([arr,arr2]))

# output = [ 1  3  5  7  9  2  4  6  8 10]


# 4. min max sin cos log of array items


# min

# arr = array([1,2,3,4,5])
#
# print(arr.min())

# output = 1


# max

# print(arr.max())

# output = 5


# sin

# print(sin(arr))

# output = [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]

# cos

# print(cos(arr))

# output = [ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]

#
# print(tan(arr))

# output = [ 1.55740772 -2.18503986 -0.14254654  1.15782128 -3.38051501]


# log

# print(log(arr))

# output = [0.         0.69314718 1.09861229 1.38629436 1.60943791]


# .....................................................................................................................................




# copying of array

# 1. alising


# arr = array([1,3,5,7,9])
#
# arr2 = arr
#
# arr[0]=2
#
# print(arr)
# print(arr2)








# shallow coppy


# view() method

# arr = array([1,2,3,4,5])
#
# arr2 = arr.view()
#
# arr[1]=9
#
# print(arr)
# print(id(arr))
#
# print(arr2)
# print(id(arr2))


# deep copy

# using copy() method


# arr = array([1,2,3,4,5])
#
# arr2 = arr.copy()
# arr[1]=20
#
# print(arr)
# print(id(arr))
# print(arr2)
# print(id(arr2))

