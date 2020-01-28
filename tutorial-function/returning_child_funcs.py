def parent(num):
    def first_child():
        return 'yo i\'m first child'
    def second_child():
        return 'im the smarter second child'
    if num == 1:
        return first_child
    else:
        return second_child

def main(argument):
    return parent(argument)

if __name__ == "__main__":
    main();