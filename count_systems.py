def to_decimal(number: str, base: int) -> int:
    s = 0
    cnt_from_right = len(number) - 1
    for c in number:
        num = 0
        if not c.isdigit():
            num = ord(c.upper()) - ord("A") + 10
        else:
            num = int(c)

        s += num * base**cnt_from_right
        cnt_from_right -= 1

    return s


def from_decimal_to(number: int, base: int) -> str:
    res = []
    while number:
        num = number % base
        if num > 9:
            num = chr(ord("A") + num - 10)

        res.append(str(num))
        number //= base
    return "".join(res)[::-1]


def from_to(number: str, base_from: int, base_to: int) -> str:
    number = to_decimal(number, base_from)
    return from_decimal_to(number, base_to)


if __name__ == "__main__":
    print(to_decimal("10101", 2))
    print(from_decimal_to(21, 2))
    print(from_to("10101", 2, 11))
