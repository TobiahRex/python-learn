def main():
    s = set([1,3,8])
    s2 = set([2,4,6,8,1])

    is_subset = s <= s2
    is_superset = s >= s2
    diff_s_s2 = s - s2
    diff_s2_s = s2 - s

    return [
        f"is_subset: {is_subset}",
        f"is_superset: {is_superset}",
        f"diff_s_s2: {diff_s_s2}",
        f"diff_s2_s: {diff_s2_s}"
    ]

if __name__ == '__main__':
    result = main()
    print('\n'.join(result))