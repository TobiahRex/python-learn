"""
    Creational (Car)
        1 Factory
        2 Abstract Factory
        3 Builder
        4 Prototype
        5 Singleton versus Borg
    Structural (Weapon)
        6 MVC (model view cont)
        7 Facade
        8 Proxy
        9 Decorator
        10 Adaptor
    Behavioral
        11 Command
        12 Interpreter
        13 State
        14 Chain of Responsibility
        15 Strategy (OCP)
        16 Observer
        17 Memento
        18 Template
        19 Reactive Design Patterns
    """
def iterator_stuff():
    nums = [1,2,3,4,5]
    loop = nums.__iter__()
    return loop.__next__()

def flat_map():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = [n_row for row in matrix for n_row in row]

    return result

def main():
    result = None

    # result = flat_map()
    result = iterator_stuff()

    return result


if __name__ == '__main__':
    result = main()
    print(f'result = {result}')
