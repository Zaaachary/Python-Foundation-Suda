
class Person(object):
    def __init__(self, name='', age=20, sex='man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if not isinstance(name, str):
            print('name must be string.')
            return
        else:
            self.__name = name

    def setAge(self, age):
        if not isinstance(age, int):
            print('age must be integer.')
            return
        else:
            self.__age = age

    def setSex(self, sex):
        if sex not in ('man', 'woman'):
            print('sex must be "man" or "woman".')
            return
        else:
            self.__sex = sex

    def show(self):
        print('Name:', self.__name)
        print('Age:', self.__age)
        print('Sex:', self.__sex)


class Student(Person):
    def __init__(self, name='', age=20, sex='man', department='CS'):
        super().__init__(name=name, age=age, sex=sex)
        # 或 Person.__init__(self, name, age, sex)
        self.setDept(department)
    
    def setDept(self, department):
        if isinstance(department, str):
            self.__department = department
        else:
            print("department must be string.")
            return
    
    def show(self):
        super(Student, self).show()
        print('Department:', self.__department)
        

if __name__ == "__main__":
    print('Person'.center(20, '='))
    Z = Person('zhang', 19, 'man')
    Z.show()
    
    print('Student'.center(20, '='))
    L = Student('Li', 21, 'man', 'CS')
    L.setAge(22)
    L.show()