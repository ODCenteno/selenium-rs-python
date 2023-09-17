class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f'My name is {self.name}')

class Runner(Person):
    num = 100

    def __init__(self, name, age, obj):
        super().__init__(name, age)
        self.obj = obj

    def marathon(self):
        Person.print_name(self)
        print("I'm a super runner person")
        return self.num

    def printer(self):
        print(self.obj, self.num)


class ParentCls(object):
    def __init__(self):
        print('Clase Padre')
    def foo(self):
        print("call parent")

class ChildCls(ParentCls):
    def __init__(self):
        super().foo()

    def foo(self):
        print("call child")


if __name__ == '__main__':
    new_obj = Runner('Daniel', 37, 'Object')
    new_obj.marathon()

    p = ParentCls()
    c = ChildCls()
    p.foo()
    c.foo()
