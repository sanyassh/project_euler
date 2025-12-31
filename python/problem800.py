import euler


ANSWER = 1412403576
NUMBER = 800800
POWER = 800800


def greater(p, q):
    return (p ** (q / POWER)) * (q ** (p / POWER)) > NUMBER


def main():
    lst = euler.prime_list(NUMBER * 20)
    result = 0
    i = 0
    j = len(lst) - 1
    while not greater(lst[i], lst[i]):
        while greater(lst[i], lst[j]):
            j -= 1
        result += j - i
        i += 1
    return result


if __name__ == '__main__':
    print(main())
