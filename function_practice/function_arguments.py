# positional arguments


# def add(x,y):  #argument inside this paranthesis is called formal arguments

#     c = x+y

#     print(c)


# add(4,5) #argument inside this bracket is called actual arguments




#  actual arguments are in 4 types..............................................................


# 1. Position argument


# def person(name,age):

#     print(name)
#     print(age)

# person('babu',26)  #this arguments inside the paranthesis should be same position as the formal arguments



# 2. keyword arguments


# def person(name,age):

#     print(name)
#     print(age)


# person(age=26,name='Babu') # if we don't know the position we can use the keyword to pass the value to appropriate argument





# 3. Default argument


# def person(name,age=18):

#     print(name)
#     print(age)

# person('Babu') # suppose the function takes two arguments and user gives only the default arguments takes value that we provide inthe forma argument





# 4. variable length argument


# def add(a,*b):# here the argument b stores values as tuple

#     c=a

#     print(b)

#     for i in b:

#         c+=i

#     print(c)


# add(1,2,3,4,5,6,7,8,9,10) # here second argument take many values as input




# def add(*a):

#     b =0

#     for i in a:

#         b+=i

#     print(b)


# add(12,13,4,5)
