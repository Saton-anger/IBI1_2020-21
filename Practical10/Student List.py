class Student:
    first_name = ''
    last_name = ''
    course = ''
    def __init__(self, f, l, c):
        self.first_name = f
        self.last_name = l
        self.course = c
    def speak(self):
        print(self.first_name, self.last_name, self.course)

# practice
p = Student("Zhoutong", "Xu", "BMI")
p.speak()

