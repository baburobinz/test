a = 15 #global variable

b = 100

c = 1000


# def something():
#
#     a = 20 #local variable
#
#     print('it is a function',a)
#
#
# something()
#
# print('it is outside function',a)


# to use global vraible


# def something():
#
#     print(a)
#
# something()


#.................................................................................


# to change global variable value using a function


# def something():
#
#
#
#
#     global a
#
#     a=20
#
#     print('local', a)
#
#
#
#
#
# something()
#
#
# print('global',a)


# if we want to use both global and local variable inside a function with same name

def something():

    x = globals()['a']

    a = 200

    print('global',x)
    print('local',a)






something()



