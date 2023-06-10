import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]


def hangman():
    word = random.choice(words)
    attempts = 6
    guessed_letters = []

    print("Гра Віселиця")
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


hangman()
