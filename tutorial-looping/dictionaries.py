
def main():
    prices = {
        'apple': 0.5,
        'orange': 0.35,
        'banana': 0.25,
    }

    for key in prices.keys():
        prices[key] = round(prices[key] + .1, 2)

    #------------------------------------------------


    all_jedis = {
        "obi-wan": "jedi knight",
        "qui gon jin": "jedi knight",
        "yoda": "jedi master",
        "mace windu": "jedi master",
    }

    jedi_masters_list = [key for key, value in all_jedis.items() if "master" in all_jedis[key]]


    print(jedi_masters_list)










if __name__ == "__main__":
    main()
