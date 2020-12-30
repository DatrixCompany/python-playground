class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.myFunc()


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def mySchool(self):
        print("Hello my name is " + self.name +
              " and my school is " + self.school)


s1 = Student("Michael", 44, "AlibabaSchool")
s1.mySchool()
s1.myFunc()
