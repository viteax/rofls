def encode_text(text: str, k: int, lang="en") -> str:
    start = "a"
    alph_power = 26
    if lang == "ru":
        start = "а"
        alph_power = 32

    res = []
    for symb in text:
        if not symb.isalpha():
            res.append(symb)
            continue

        new_symb = chr(ord(start) + (ord(symb.lower()) - ord(start) + k) % alph_power)
        if symb.isupper():
            new_symb = new_symb.upper()
        res.append(new_symb)
    return "".join(res)


def decode_text(text: str, k: int, lang="en") -> str:
    return encode_text(text, -k, lang)


if __name__ == "__main__":
    text = input("Введите текст: ")
    k = input("Сдвиг: ")
    if k:
        k = int(k)

    mode_decode = int(input("Закодировать или расшифровать (0, 1): "))
    lang = input("Русский: ")
    if lang:
        lang = "ru"

    if mode_decode:
        print(decode_text(text, k, lang))
    else:
        print(encode_text(text, k, lang))
