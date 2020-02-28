import functools

def main():

    exp_filter = {"exposureFilters": []}

    data = {
        "filters": [
            [exp_filter],
            [exp_filter, exp_filter],
            [exp_filter, exp_filter],
        ]
    }

    groups = [group for group in data.get("filters")]

    assets_1 = [
        { "pid": 'A' },
        { "pid": 'B' }
        ]
    assets_2 = [
        { "pid": 'C' }
        ]
    assets_3 = [
        { "pid": 'C' },
        { "pid": 'D' }
        ]

    assets_per_group = [assets_1, assets_2, assets_3]

    all_assets = {
        'A': { "open": 100 },
        'B': { "open": 200 },
        'C': { "open": 300 },
        'D': { "open": 400 },
    }

    cond1 = 0
    cond2 = False
    cond3 = set()
    cond4 = dict()
    cond5 = ''
    cond6 = []

    result = None
    if all([cond5, len(cond6)]) is False:
    # if all([cond1, cond2, cond3, cond4, cond5, len(cond6)]) is False:
        result = True
    
    return result

if __name__ == "__main__":
    result = main()
    print(result)
