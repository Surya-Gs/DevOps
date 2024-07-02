# Create a list of student with info

class student:

    def __init__(self,  name, roll_num):
        self.name = name
        self.roll_num = roll_num

    def roll_updae(self):
        self.roll_num += 1

student_info = student('Saknkdf', 3445)
student_info.roll_updae()


print(student_info.name)
print(student_info.roll_num)



