from datetime import datetime
# Создаю функцию create_note() с содержанием основного кода.
def create_note():
    note = {}
    # Ввожу содержимое словаря note через input.
    note['name'] = input('Введите ваше имя: ')
    note['content'] = input('Введите описание вашей заметки: ')
    note['title'] = input('Введите заголовок вашей заметки: ')
    note['status'] = input('Введите статус вашей заметки (новая, в процессе, отложено): ')

    # Создаю переменную которая будет указывать сегодняшнюю дату, сразу форматирую ее в необходимый формат.
    note['create_date'] = datetime.now().strftime('%d-%m-%Y')

    # Цикл для проверки введенного формата даты.
    while True:
        issue_date = input('Введите дату окончания действия заметки в формате ДД.ММ.ГГГГ: ')
        try:
            note['issue_date'] = datetime.strptime(issue_date, '%d.%m.%Y').strftime('%d.%m.%Y')
            break
        except ValueError:
            print('Ошибка! Пожалуйста введите верный формат даты (ДД.ММ.ГГГГ)!')
    return note

new_note = create_note()
# Вывод созданного словаря с данными заметки
print('Созданная заметка: ', new_note)