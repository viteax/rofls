import random
import sys
import time

ANSWERS = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно",
]

PROTAGONIST_NAME = "Путник"
STRANGER_NAME = "Незнакомец"


def input_hero() -> str:
    ans = input(f"{PROTAGONIST_NAME}: ")
    print()
    return ans


def print_stranger(text: str, delay=0.5, has_first_delay=False) -> None:
    print(f"{STRANGER_NAME}:", end=" ")
    for word in text.split():
        for c in word:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)

        sys.stdout.write(" ")
        sys.stdout.flush()
        if has_first_delay:
            time.sleep(delay)
            has_first_delay = False
    print()


if __name__ == "__main__":
    print()
    print_stranger("Привет, тебе погадать?", has_first_delay=True)
    ans = input_hero()
    if ans.lower() in ("да", "го", "давай", "было бы славно"):
        print_stranger("Спрашивай, что пожелаешь, малец")
        question = input_hero()
        while question and question != "...":
            print_stranger(random.choice(ANSWERS))
            question = input_hero()
        print_stranger("Надеюсь, теперь твоя жизнь ясна, как никогда прежде")
    else:
        print_stranger("...", delay=1, has_first_delay=True)
        print_stranger("ок.", delay=1.5, has_first_delay=True)
        print_stranger("я обиделся.")
    time.sleep(1)
