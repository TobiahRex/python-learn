def do_mutate():
    global arg
    arg = {
        'name': 'bob'
    }

def main():
    d = {
        'name': 'toby'
    }
    do_mutate(d)
    print(d)

if __name__ == "__main__":
    main()