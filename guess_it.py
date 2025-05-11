import math
import random

START = 1
STOP = 100
DIVIDE_LINE = "-" * 22


def print_tries(tries: int):
    print()
    print(f"У тебя осталось {tries}", end=" ")
    if tries > 4:
        print("попыток")
    elif tries > 1:
        print("попытки")
    else:
        print("попытка")


def print_res(text: str) -> None:
    print(DIVIDE_LINE)
    print(text.center(len(DIVIDE_LINE)))
    print(DIVIDE_LINE)


if __name__ == "__main__":
    ans = random.randint(START, STOP)
    tries = math.ceil(math.log2(STOP - START + 2))

    print()
    print(f"Привет, я загадал число от {START} до {STOP}, угадай")
    print(f"(Псс, если что у тебя всего {tries} попыток)")

    is_playing = True
    has_won = False

    while is_playing:
        print_tries(tries)
        guess = input("Думаю что это число: ")
        if not guess.isdigit():
            print("Это не число, давай по новой")
            continue

        guess = int(guess)
        if guess < ans:
            print_res("Больше")
        elif guess > ans:
            print_res("Меньше")
        else:
            is_playing = False
            has_won = True
            break

        tries -= 1
        if tries == 0:
            is_playing = False

    print()
    if has_won:
        print("Поздравляю с победой!")
        print(f"Загаданное число было {ans}")
    else:
        print("К сожалению, ты проиграл(")
