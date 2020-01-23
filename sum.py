def add(a, b):
    return int(a) + int(b)

input1 = input('Enter a value for a: ')
input2 = input('Enter a value for b: ')

sum = add(input1, input2)

print(f'{input1} + {input2} = {sum}')