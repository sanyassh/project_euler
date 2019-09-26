from sympy import integer_nthroot

import euler


ANSWER = None
LIMIT = 10 ** 10
PRIME_LIST = euler.prime_list(int(LIMIT ** 0.5))
SQUARES = [pow(n, 2) for n in PRIME_LIST]
SLOW = True


def solve(lst, n, fi_n2):
    result = 0
    items = [(lst, n, fi_n2, 0)]
    length = len(lst)
    while items:
        lst, n, fi_n2, index = items.pop()
        if integer_nthroot(fi_n2, 3)[1]:
            result += n
        for i in range(index, length):
            new_n = n * PRIME_LIST[i]
            if new_n >= LIMIT:
                continue
            new_lst, new_fi_n2 = lst.copy(), fi_n2
            new_lst[i] += 1
            if new_lst[i] == 1:
                new_fi_n2 *= PRIME_LIST[i] * (PRIME_LIST[i] - 1)
            else:
                new_fi_n2 *= SQUARES[i]
            items.append((new_lst, new_n, new_fi_n2, i))
    return result


def main():
    total = 0
    for i, prime in enumerate(PRIME_LIST):
        lst = [0 for _ in range(i + 1)]
        lst[-1] = 2
        n = prime ** 2
        fi_n2 = prime ** 3 * (prime - 1)
        total += solve(lst, n, fi_n2)
    return total


if __name__ == '__main__':
    print(main())
