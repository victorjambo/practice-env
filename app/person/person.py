class Person(object):
    def __init__(self, name):
        self.name = name

    def allocate_room(self):
        return 'room allocated'


me = Person('victor', 34)
print(me)
