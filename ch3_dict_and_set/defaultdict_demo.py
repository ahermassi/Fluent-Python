from collections import defaultdict

if __name__ == '__main__':

    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d1 = defaultdict(list)  # for each key, a list of corresponding values is constructed
    for k, v in s:
        d1[k].append(v)
    print(list(d1.items()))

    # The previous code is equivalent to

    d2 = {}
    for k, v in s:
        d2.setdefault(k, []).append(v)
    print(list(d2.items()))

    d3 = defaultdict(int)
    for k, v in s:
        d3[k] += v
    print(list(d3.items()))  # for each key, keep a count (add) for the corresponding values

    s = 'mississippi'
    d4 = defaultdict(int)
    for k in s:
        d4[k] += 1
    print(list(d4.items()))
