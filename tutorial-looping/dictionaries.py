
def main():
    prices = {
        'apple': 0.5,
        'orange': 0.35,
        'banana': 0.25,
    }

    for key in prices.keys():
        prices[key] = round(prices[key] + .1, 2)

    print(prices)












if __name__ == "__main__":
    main()
