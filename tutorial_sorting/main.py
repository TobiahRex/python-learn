def sorting_iterators():
    numbers = [6, 3, 1, 3]
    tuples = (3, 2, 0, 8)
    nums_set = {4, 2, 0, 8, 1, 1}
    return sorted(tuples)

def sorting_string():
    nums_string = '23955124'
    char_string = 'b1 bb d e z a X Z A B'
    asdf_string = 'asdfasd asdf asdf a asdfasdfasfasdfa'
    # data = sorted(char_string.split())
    # data = sorted(char_string.split(), reverse=True)
    # ----------------------------------------
    # ['asdfasdfasfasdfa', 'asdfasd', 'asdf', 'asdf', 'a']
    data = sorted(asdf_string.split(), reverse=True)
    # ----------------------------------------
    # ['a', 'asdf', 'asdf', 'asdfasd', 'asdfasdfasfasdfa']
    data = sorted(asdf_string.split())
    # ----------------------------------------
    # 
    words = ['apple', 'banana', 'pina-colada', 'bob', 'the builder']
    # ['bob', 'apple', 'banana', 'pina-colada', 'the builder']
    data = sorted(words, key=len)
    # [5, 6, 11, 3, 11]
    #print([len(word) for word in words])
    
    # ----------------------------------------
    nums = [5, 2, 1, -1]
    def sum(*args):
        last = -1
        def cb(next_num):
            if last <= next_num:
                return next_num
            else:
                return last

        return cb
    get_sum = sum()

    data = sorted(nums, key=get_sum)

    # ----------------------------------------
    nums = [
        {
            'prices': { 'open': 900 },
        },
        {
            'prices': { 'open': 150 },
        },
        {
            'prices': { 'open': 200 },
        },
        {
            'prices': { 'open': 300 },
        },
    ]
    
    return sorted(nums, key=lambda asset: asset.get('prices').get('open'), reverse=True)








def main():
    # result = sorting_iterators()
    result = sorting_string()
    return result

if __name__ == '__main__':
    result = main()
    print(f'result: {result}')
