# A class method receives the class as implicit first argument, just like an instance method receives the instance
#Converts a method into a class method

# class student:
#     marks=0

#     def classmethod(self, obtained_marks):
#         marks=obtained_marks
#         print('Obtained_Marks', marks)

#     Student.print_marks = classmethod(student.compute_marks)
#     Student.print_marks(88)


class person:
    age=26

    def Printage(cls):
        print('The age is:', cls.age)
person.Printage = classmethod(person.Printage)
person.Printage() 



