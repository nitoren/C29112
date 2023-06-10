import random


def choose_game():
    print("Виберіть тип гри:")
    print("1. Математичні рівняння")
    print("2. Вгадування слів")

    choice = input("Ваш вибір (1 або 2): ")

    if choice == '1':
        play_math_game()
    elif choice == '2':
        play_word_game()
    else:
        print("Невірний вибір. Спробуйте ще раз.")
        choose_game()


def play_math_game():
    print("Гра Математичні рівняння")
    print("Спробуйте вирішити рівняння.")

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    else:
        solution = num1 * num2

    equation = f"{num1} {operator} {num2} = ?"

    while True:
        print(equation)
        guess = input("Введіть відповідь: ")

        if guess.isdigit():
            if int(guess) == solution:
                print("Ви вирішили рівняння! Вітаємо!")
                break
            else:
                print("Невірна відповідь. Спробуйте ще раз.")
        else:
            print("Невірний формат відповіді. Введіть число.")


def play_word_game():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    word = random.choice(words)
    attempts = 6
    guessed_letters = []

    print("Гра Вгадування слів")
    print("Спробуйте вгадати загадане слово.")

    while True:
        masked_word = ""
        for letter in word:
            if letter in guessed_letters:
                masked_word += letter
            else:
                masked_word += "_"
        print(masked_word)

        guess = input("Введіть букву: ").lower()

        if len(guess) != 1:
            print("Введіть лише одну букву!")
            continue

        if guess in guessed_letters:
            print("Ця буква вже вгадана!")
            continue

        guessed_letters.append(guess)

        if set(word) == set(guessed_letters):
            print("Ви вгадали слово! Вітаємо!")
            break

        if guess not in word:
            attempts -= 1
            print("Цієї букви немає у слові.")
            print("Залишилося спроб:", attempts)
            draw_hangman(attempts)

        if attempts == 0:
            print("Ви програли! Загадане слово:", word)
            break


def draw_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        """,
        """
           --------
           |      |
           |      O
           |     \\
           |      
           |     
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      
           |     
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      
           |     
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """
    ]
    print(stages[6 - attempts])


choose_game()
