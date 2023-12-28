def ask_question(prompt, correct_answer):
    while True:
        user_answer = input(prompt)
        if user_answer.lower() == correct_answer.lower():
            print(f"Ответ {user_answer} верный")
            return True
        else:
            print('Ответ не правильный')
            return False

def main():
    questions = [
        {"prompt": "Как называется интерактивная среда для разработки, работающая в браузере? ", "correct_answer": "Jupyter"},
        {"prompt": "Какое ключевое слово используется для определения функции? ", "correct_answer": "def"},
        {"prompt": "В каком году закончилась поддержка Python 2? ", "correct_answer": "2020"},
        {"prompt": "Каким символом можно комментировать код в Python? ", "correct_answer": "#"},
        {"prompt": "Какой командой принять ввод от пользователя в Python? ", "correct_answer": "input"},
        {"prompt": "Как получить длину списка или строки? ", "correct_answer": "len()"},
        {"prompt": "Какой командой преобразовать строку в число с плавающей запятой? ", "correct_answer": "float"},
        {"prompt": "Какой оператор используется для логического И? ", "correct_answer": "and"},
        {"prompt": "Напиши какими скобочками можно создать пустой словарь? ", "correct_answer": "{}"},
        {"prompt": "Как завершить программу в Python? ", "correct_answer": "exit()"}
    ]


    correct_count = 0
    total_questions = len(questions)
    current_question = 0

    while current_question < total_questions:
        question = questions[current_question]
        attempts = 0
        while not ask_question(question["prompt"], question["correct_answer"]):
            attempts += 1
            if attempts >= 2:
                break
        if attempts == 0:
            correct_count += 1
        current_question += 1

    print(f"Вопросы закончены, вы дали правильных {correct_count} ответов из {total_questions} вопросов")

if __name__ == "__main__":
    main()