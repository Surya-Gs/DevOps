class person:
    def __init__(self, name, id):
        self.name = name
        self.id=id
    
    def display(self):
        print(self.name)
        print(self.id)
    
    def display(self):

        print("My name is {}".format(self.name))
        print("My id is: {}".format(self.id))

class Employee(person):
    def __init__(self, name, id, post):
        self.name =name
        self.id=id
        self.post=post
        
        person.__init__(self, name, id)

    def details(self):
        print("My name is {}".format(self.name))
        print("My id is {}". format(self.id))
        print("post:{}".format(self.post)) 

a = Employee('Rahul', 498908, "Associate")

a.display()
a.details()

        