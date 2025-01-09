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

# Создание функции для обновления данных заметки.
def update_note(note):
    print('Доступные данные для изменения: ', list(note.keys()))
    while True:
        change_func = input('Введите необходимый параметр для его изменения: ')
        if change_func in note:
            break
        else:
            print('Ошибка, введите существующий параметр! ')
    if change_func == 'issue_date':
            while True:
                new_date = input('Введите новую дату в формате (ДД.ММ.ГГГГ): ')
                try:
                    note[change_func] = datetime.strptime(new_date, '%d.%m.%Y').strftime('%d.%m.%Y')
                    break
                except ValueError:
                    print('Ошибка! Введите верный формат даты: ')
    else:
            note[change_func] = input(f'Введите новое значение для {change_func}: ')

    return note

new_note = create_note()
# Вывод созданного словаря с данными заметки
print('Созданная заметка: ', new_note)
print('Заметка обновлена: ', update_note(new_note))