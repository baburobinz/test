# # parent class

# class person :

#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def display(self):

#         print(self.name)
#         print(self.id)

#     def details(self):

#         print("My name is {}".format(self.name))

#         print("id is {}".format(self.id))

# # child class

# class employee(person):

#     def __init__(self,name,id,salary,post):

#         self.salary = salary

#         self.post = post

#         person.__init__(self,name,id)



#     def details(self):

#         print('My name is {}'.format(self.name))
#         print('My id is {}'.format(self.id))
#         print('My post is {}'.format(self.post))
#         print('My salary is {}'.format(self.salary))

# obj = employee('babu',200,20000,'intern')

# obj.details()



# different type of inheritence


# singlre inheritence - it inherits only single class hence there will be only one child and parent 


# class A:

#     def feature1(self):

        

#         print('feature 1 is working')

       

# class B(A):

#     def feature2(self,num):

#         self.num = num

#         print('feature 2 is working')

#         print(self.num)

        


# obj = B()
# obj.feature1()
# obj.feature2(1)



# class person:

#     def __init__(self,name):

#         self.name = name

        


# class Employee(person):

#     def showEmployeeDetails(self,id,post): 

#         self.id = id
#         self.post = post

#         print(self.name)
#         print(self.id)
#         print(self.post)


# obj = Employee('babu')

# obj.showEmployeeDetails(200,'intern')


from hi import show_name

show_name('babu')








        











