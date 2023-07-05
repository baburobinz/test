from array import*

# vals = array('i',[1,2,3,4,5])

# vals2 = array(vals.typecode,(a for a in vals))

# print(vals2)


# user inputs values in to an array


arr = array('i',[])

inp = int(input('Enter Length of array: '))


for i in range(inp):

    val = int(input('Enter Your Value: '))

    arr.append(val)

print(arr)


find = int(input('Find index of: '))

print(arr.index(find))

# ind = 0

# for e in arr:

#     if e == find:

#         print(ind)
#         break

#     else:

#         ind+=1

