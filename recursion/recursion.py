# Recursion is basically a function call itself following are the example, recursion normally runs up to 1000 times we can customis ethe value


# to customise we use sys

import sys

sys.setrecursionlimit(104)

print(sys.getrecursionlimit())
i = 0
def greet():


    global i

    i+=1

    print('Hello',i)

    greet()


greet()


