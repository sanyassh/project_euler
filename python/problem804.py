ANSWER = 4921370551019052
LIMIT = 10 ** 16


def main():
    result = 2 * (int(LIMIT ** 0.5) + int((LIMIT / 41) ** 0.5))
    limit4 = LIMIT * 4
    for j in range(1, LIMIT):
        d = limit4 - 163 * j * j
        if d < 0:
            break
        d05 = d ** 0.5
        result += 2 * int((d05 + j) / 2)
        result += 2 * int((d05 - j) / 2)
    return result


if __name__ == '__main__':
    print(main())
