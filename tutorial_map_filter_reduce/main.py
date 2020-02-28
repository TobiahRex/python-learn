from functools import reduce

def main():
    l = [1, 2, 3]
    return reduce(lambda x, y: x + y, l)


if __name__ == "__main__":
    print(main())