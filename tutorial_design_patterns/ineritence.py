class Pet(object):
    """Base class for a persons pets"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def get_name(self):
        return self.name
    
    @classmethod
    def get_species(cls):
        return cls.species

    def __str__(self):
        return f'{self.name} is a {self.species}'

class Dog(Pet):
    """Dog is a subclass of Pet"""
    
    def __init__(self, name, chases_cats=True):
        super().__init__(name, "Dog")
        self.chases_cats = chases_cats

    def does_chase_cats(self):
        return self.chases_cats
    
    def __str__(self):
        dog_info = ' who chases cats' if self.chases_cats else ''
        return super().__str__() + dog_info

class A(object):
    def __init__(self):
        print('A')
    
    @staticmethod
    def foo():
        print('foo')

class B(object):
    def __init__(self):
        print('B')
    
    @staticmethod
    def bar():
        print('bar')

def main():
    my_pet = Pet('Rex', 'Wolf')
    my_dog = Dog('Max')
    my_other_dog = Dog('Bark', False)

    

    return Pet.get_species(my_other_dog)



if __name__ == '__main__':
    result = main()
    print(f'results = {result}')