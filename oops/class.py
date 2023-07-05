# create an empty class

class dog():
    pass



class dog():

    attr1 = "mammal"

    def __init__(self,name):

        self.name = name


rodger = dog("Rodger")


print("My dog is {}".format(rodger.attr1))




# create a class employee and make object of the class and print name and id of the employee


class Employee:

    def __init__(self,name,id):

        self.name = name

        self.id = id

    def showEmployee(self):

        print(f"Employee Name: {self.name} and id is {self.id}")


class programmer(Employee):

    def show_language(self):

        print('default language is python')


# obj1 = Employee('Babu',400)

# obj1.showEmployee()

# obj2 = Employee('Rohan',401)

# obj2.showEmployee()

obj3 = programmer('Anas',403)

obj3.showEmployee()
obj3.show_language()


