def main():
    """Приймаємо рядок від користувача та виводимо на екран"""

    users_input = input()

    edited_text = make_faces(users_input)

    print(edited_text)


def make_faces(text):
    """Приймає текст від користувача та замінює текстові смайли зображеннями"""

    text = text.replace(":)", "🙂")

    text = text.replace(":(", "🙁")

    return (text)


main()
