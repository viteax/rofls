def encode_word(word: str) -> str:
    alpha_cnt = sum(c.isalpha() for c in word)
    res = []
    for c in word:
        new_c = c
        if c.isalpha():
            new_c = chr(ord("a") + (ord(c.lower()) - ord("a") + alpha_cnt) % 26)
            if c.isupper():
                new_c = new_c.upper()
        res.append(new_c)
    return "".join(res)


def process_text(text: str) -> str:
    words = text.split()
    res = [encode_word(word) for word in words]
    return " ".join(res)


text = input()
print(process_text(text))
