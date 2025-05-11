import random

STAGES = [
    # финальное состояние: голова, торс, обе руки, обе ноги
    """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            """,
    # голова, торс, обе руки, одна нога
    """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
            """,
    # голова, торс, обе руки
    """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
            """,
    # голова, торс и одна рука
    """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
            """,
    # голова и торс
    """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
            """,
    # голова
    """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
            """,
    # начальное состояние
    """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
            """,
]
MAX_TRIES = len(STAGES) - 1
WORDS = [
    "молекула",
    "гном",
    "ангел",
    "падение",
    "ракета",
    "агрегат",
    "язык",
    "планета",
    "волосы",
    "стрижка",
    "птичка",
]


def display_hangman(tries) -> None:
    print(STAGES[tries])


def display_info(tries: int, word: str, msg="") -> None:
    display_hangman(tries)
    if msg:
        print("-" * 10)
        print(msg)
        print("-" * 10)
        msg = ""
    print(f"Количество попыток: {tries}")
    print(f"Пока ты собрал слово: {word}")


def update_word(word: str, guess: str, ans: str) -> str:
    res = []
    for word_c, c in zip(word, ans):
        if guess == c:
            res.append(c.upper())
        else:
            res.append(word_c)

    return "".join(res)


if __name__ == "__main__":
    print()
    print("Сегодня поиграем в игру угадай слово")
    print("Правила просты, я загадываю, ты пытаешься отгадать")
    print("Можешь по буквам, а если уверен можешь сразу слово")
    print("Но я бы на твоем месте не спешил,")
    print(f"т.к. от виселицы тебя отделяет лишь {MAX_TRIES} попыток")
    print("Будь внимателен... муа-ха-ха-ха-ха")

    ans = random.choice(WORDS)

    has_won = False
    tries = MAX_TRIES
    guessed = set()
    guessed_right = 0
    word = "_" * len(ans)
    msg = ""

    while tries > 0:
        display_info(tries, word, msg=msg)

        guess = input("Что думаешь: ")
        if guess in guessed:
            msg = "уже было"
            continue
        guessed.add(guess)

        if len(guess) > 1:
            if guess.lower() == ans:
                has_won = True
                break
        elif len(guess) == 1:
            matches = ans.count(guess)
            if matches > 0:
                word = update_word(word, guess, ans)
                guessed_right += matches
                if guessed_right == len(ans):
                    has_won = True
                    break
                continue
        else:
            msg = "Ты ничего не ввел"
            continue

        tries -= 1

    print()
    if has_won:
        print("Ты победил!")
    else:
        display_hangman(tries)
        print("Повисим")
