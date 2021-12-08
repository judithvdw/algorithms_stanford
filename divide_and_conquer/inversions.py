def sort_and_count(a):
    if len(a) == 1:
        return a, 0
    else:
        b, x = sort_and_count(a[:len(a) // 2])
        c, y = sort_and_count(a[len(a) // 2:])

        d = []
        i = 0
        j = 0
        z = 0
        while i < len(b) and j < len(c):
            if b[i] < c[j]:
                d.append(b[i])
                i += 1
            else:
                z += len(b) - i
                d.append(c[j])
                j += 1

        # end cases:
        if i < len(b):
            d.extend(b[i:])
        if j < len(c):
            d.extend(c[j:])

    return d, x + y + z


if __name__ == '__main__':
    with open('ints.txt') as f:
        raw = f.readlines()
        ints = [int(i) for i in raw]

    print(sort_and_count(ints)[1])
