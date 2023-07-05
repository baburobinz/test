count = int(input('Enter Length of List: '))

lst = []

for i in range(count):

    inp = int(input('Enter numbers: '))

    lst.append(inp)


def count_odd_and_even(lst):

    odd = 0

    even = 0

    for i in lst:

        if i%2 == 0:

            even+=1
        else:
            odd+=1

    return even,odd

even, odd = count_odd_and_even(lst)

print("Count of odd: {}\n Count of Even: {}".format(odd,even))