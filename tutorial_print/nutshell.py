import os

def main():
    some_string = "hello world"
    print('strip spaces: ', some_string.rstrip())
    print('split on spaces: ', some_string.rsplit(' '))
    print(f'Hello, {os.getlogin()}! How are you?')



if __name__ == "__main__":
    main();