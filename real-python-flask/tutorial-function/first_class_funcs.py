def say_hi(argument):
    return f"Hello {argument}"

def call_func(some_func, argument):
    return some_func(argument)

def main(argument):
    """docstring"""
    return call_func(say_hi, argument)

if __name__ == "__main__":
    print(main(1))