import random

DIGITS = list("0123456789")
LOWERCASE_LETTERS = list("abcdefghijklmnopqrstuvwxyz")
UPPERCASE_LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
PUNCTUATION = list("!#$%&*+-=?@^_")


if __name__ == "__main__":
    print()
    print("Привет, давай сгенерим мощнейший пароль")
    print()

    passwords_cnt = 0
    password_len = 0
    legal_chars = []

    print("Сколько паролей сгенерить?")
    passwords_cnt = int(input())

    print("Какую длину оформить?")
    password_len = int(input())

    print("Цифры используем?")
    if input().lower() == "да":
        legal_chars.extend(DIGITS)

    print("Буквы в нижнем регистре?")
    if input().lower() == "да":
        legal_chars.extend(LOWERCASE_LETTERS)

    print("Буквы в верхнем регистре?")
    if input().lower() == "да":
        legal_chars.extend(UPPERCASE_LETTERS)

    print("Знаки пунктуации?")
    if input().lower() == "да":
        legal_chars.extend(PUNCTUATION)

    print()
    print("Поехали...")

    passwords = [
        "".join(random.choices(legal_chars, k=password_len))
        for _ in range(passwords_cnt)
    ]

    print("Пароли готовы:")
    print(*passwords, sep="\n")
