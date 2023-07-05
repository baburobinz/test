from calc import*


while True:

    print('1.Add\n2.Substract\n3.Division\n4.Multiplication')

    ch = int(input('Enter Choice: '))

    if ch <=0 or ch>4:
        print('\nEnter Valid Choice...!\n')

    else:

        a = int(input('Enter First Number: '))
        b = int(input('Enter Second Number:'))

    if ch == 1:

        result = add(a,b)
        print('\nAnswer: ',result,'\n')

    elif ch == 2:

        result = sub(a,b)
        print('\nAnswer: ',result,'\n')


    elif ch == 3:

        result = div(a,b)
        print('\nAnswer: ',result,'\n')

    elif ch == 4:

        result = mul(a,b)
        print('\nAnswer: ',result,'\n')






