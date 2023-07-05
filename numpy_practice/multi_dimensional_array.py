from numpy import *

# create a multi dimensional array

# m_array = array([
#
#     [1,2,3,4,5,6,7,8,9,10,],
#     [11,12,13,14,15,16,17,18,19,20]
#
# ])




#  make new arraya from the 2d array the should be in 1d


# arr2 = m_array.flatten()
# print(arr2)


#  create a 2d array


# _2d_array = m_array.reshape(6,2)
# print(_2d_array)


# create a 3d array


# _3d_array = m_array.reshape(2,2,5)
#
# print(_3d_array)


#  create a matrix using matrix function......................................................................... useful to perform more operations


# first method
# arr = array([
#
#     [1,2,3,4,5],
#     [6,7,8,9,10]
#
# ])
#
#
# m = matrix(arr)
# print(m)





# second method if u dont have a n array we can create matrix directly


m = matrix('1 2 3;'
           '4 5 6;'
           '7 8 9 ')

m1 = matrix('10 11 12; '
            '13 14 15; '
            '16 17 18')




# print diagonal elements


# print(diagonal(m))
# print(m.min())
# print(m.max())
# print(m+m1)
# print(m*m1)

print(m*m)