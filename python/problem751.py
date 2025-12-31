ANSWER = '2.223561019313554106173177'
LIMIT = 24


def floor(n, mod):
    return int(mod * (n // mod))


def main():
    modulo = 10 ** LIMIT
    start = 2 * modulo
    while True:
        b = []
        for i in range(1, len(str(start))):
            if i == 1:
                b.append(start)
            else:
                b1 = b[-1]
                fb1 = floor(b1, modulo)
                b.append(fb1 * (b1 - fb1 + modulo) / modulo)
        tmp = ''.join([str(int(n) // modulo) for n in b])[:LIMIT + 1]
        tmp = tmp.ljust(LIMIT + 1, '0')
        new = int(tmp)
        if new == start:
            return tmp[0] + '.' + tmp[1:]
        start = new


if __name__ == '__main__':
    print(main())
