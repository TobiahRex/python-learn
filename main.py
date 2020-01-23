def main():
    a = [1, 2, 3]
    b = ['one', 'two', 'three']

    c = dict(zip(b, a))

    stringNums = iter(c)

    while(True):
        val = next(stringNums)
        print('val: ', val)
        if (val):
            print(val)
        else:
            raise StopIteration

    # d = { 'one': 1, 'two': 2, 'three': 3}
    # for i in d:
    #     print(d[i])

if __name__ == '__main__':
    main()
