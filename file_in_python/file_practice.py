#create a multiplication table and store it in to a text file


f = open('multiplication_table.txt','r')

print(f.read())
#
# for i in range(1,11):
#
#     table = f'{i}x{5} = {i*5}\n'
#
#     f.write(table)