
def main():
    prices = {
        'apple': 0.5,
        'orange': 0.35,
        'banana': 0.25,
    }

    for key in prices.keys():
        prices[key] = round(prices[key] + .1, 2)
    print(prices)
    #------------------------------------------------

    all_jedis = {
        "obi-wan": "jedi knight",
        "qui gon jin": "jedi knight",
        "yoda": "jedi master",
        "mace windu": "jedi master",
    }

    jedi_masters_list = [key for key, value in all_jedis.items() if "master" in all_jedis[key]]


    print(jedi_masters_list)
    #------------------------------------------------
    # dictionary comprehension
    jedi_classes = ["jedi knight", "jedi knight", "jedi master", "jedi master"]
    jedis = ["obi wan", "qui-gon jin", "yoda", "mace windu"]
    jedis_dict = { key: value for key, value in zip(jedi_classes, jedis) }

    print(jedis_dict)

    new_dict = { value: key for key, value in jedis_dict.items() }
    print(new_dict)

    odd_dict = { i: 2*i + 1 for i in range(20) }
    even_dict = { i: 2*i + 2 for i in range(20) }

    all_nums = [list(value for value in odd_dict.values())]

    # print(even_dict)
    # print(odd_dict)
    print(all_nums)



if __name__ == "__main__":
    main()
