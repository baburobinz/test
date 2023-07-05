from array import*

vals = array('b',[1,2,3])

newArr = array(vals.typecode,(a for a in vals))


print(len(newArr))