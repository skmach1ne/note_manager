from datetime import datetime
# Создаем словарь для хранения информации о заметке

notes = []
current_id = 100
while True:
    note = {}
# Создание ID
    note['ID'] = current_id
    current_id += 1

# Сбор данных от пользователя
    note['Имя'] = input('\nВведите ваше имя: ')
    note['Описание_заметки'] = input('Введите описание вашей заметки: ')
    current_date = datetime.now()
    created_date = input('Введите дату создания вашей заметки (в формате ДД.ММ.ГГГГ.): ')
    issude_date = input('Введите дату создания вашей заметки (в формате ДД.ММ.ГГГГ.): ')
    note['Дата_создания'] = datetime.strptime(created_date, "%d.%m.%Y")
    note['Дата_истечения'] = datetime.strptime(issude_date, "%d.%m.%Y")
    note['Текущая_дата'] = current_date
    date_difference = (note['Дата_истечения'] - note['Текущая_дата']).days
    date_difference = date_difference + 1

    # Добавляем бесконечный цикл заголовков в список внутри словаря
    note['Заголовки'] = []
    while True:
        title = input('Введите название заголовков (или оставьте поле пустым для пропуска): ')
        if title == '':
            break
        note['Заголовки'].append(title)

# Добавляем выбор статуса заметки
    note['Статус'] = []
    while True:
        status = input('Введите статус заметки (цифру): \n1. Выполнена \n2. В процессе \n3. Отложено \n')
        status_1 = 'Выполнена'
        status_2 = 'В процессе'
        status_3 = 'Отложено'

        # Преобразую ввод из типа строка в число
        try:
            status = int(status)

            #Создаю уведомление для пользователя о неверно введенном формате.
        except ValueError:
            print('Вы ввели неверный формат, пожалуйста введите число! \n')
            continue
        if status == 1:
            note['Статус'].append(status_1)
        elif status == 2:
            note['Статус'].append(status_2)
        elif status == 3:
            note['Статус'].append(status_3)
        else:
            print('Введите цифру из предложенных!')
            continue
        break

# Выводим собранные данные
    print('Собранные данные о заметке: \n')
    print(f'Введенное имя: {note['Имя']}')
    print(f'Описание заметки: {note['Описание_заметки']}')

    # Выводим Дату с корректировкой по формату
    print(f'Текущая дата: {note['Текущая_дата'].strftime('%d.%m.%Y')}')
    print(f'Дата создания заметки: {note['Дата_создания'].strftime('%d.%m.%Y')}')
    print(f'Дата истечения заметки: {note['Дата_истечения'].strftime('%d.%m.%Y')}')
    print(f'Заголовки заметки: {', '.join(note['Заголовки'])}')
    print(f'Статус: {', ' .join(note['Статус'])}')

# Форматируем вывод для прошедших дедлайнов:
    if date_difference < 0:
        if date_difference == 1:
            day_word = 'день'
        elif 2 <= date_difference <= 4:
            day_word = 'дня'
        else:
            day_word = 'дней'
            print(f'Дедлайн истек {note['Дата_истечения'].strftime('%d.%m.%Y')}, {date_difference * -1} {day_word} назад' )
            note['Дедлайн'] = f'Дедлайн истек {note['Дата_истечения'].strftime('%d.%m.%Y')}, {date_difference * -1} {day_word} назад '

# Форматируем вывод для будущих дедлайнов:
    if date_difference > 0:
        if date_difference == 1:
            day_word = 'день'
        elif 2 <= date_difference <= 4:
            day_word = 'дня'
        else:
            day_word = 'дней'
            print(f'Дедлайн истекает {note['Дата_истечения'].strftime('%d.%m.%Y')}, через {date_difference} {day_word}')
            note['Дедлайн'] = f'Дедлайн истекает {note['Дата_истечения'].strftime('%d.%m.%Y')}, через {date_difference} {day_word}  '
    notes.append(note)

# Спрашиваем пользователя, хочет ли он создать еще одну заметку
    return_word = input('Вы хотите создать еще одну заметку? Да/Нет: ').strip().lower()
    if return_word != 'да':
        break

# Вывод всех заметок
while True:
    print('\nВаши заметки:')
    for i, note in enumerate(notes, 1):
        print(f'\nЗаметка {i}. ID: {note['ID']}')
        print(f'Имя: {note['Имя']}')
        print(f'Описание заметки: {note['Описание_заметки']}')
        print(f'Текущая дата: {note['Текущая_дата'].strftime('%d.%m.%Y')}')
        print(f'Дата создания заметки: {note['Дата_создания'].strftime('%d.%m.%Y')}')
        #print(f'Дата истечения заметки: {note['Дата_истечения'].strftime('%d.%m.%Y')}')
        print(f'Заголовки заметки: {', '.join(note['Заголовки'])}')
        print(f'Статус заметки: {', '.join(note['Статус'])}')
        print(f'{(note['Дедлайн'])}')

# Запрос на редактирование списка заметок.
    choice = input('\nВы хотите отредактировать список заметок? Да/нет: ').strip().lower()
    if choice != 'да':
        break

# Ввод данных для удаления заметки.
    delete_function = input('\nВведите ID, Номер заметки, Описание или Заголовок заметки для ее удаления: ').strip()

# Проверяем поиск заметки исходя из введенных данных
    find_note = None
    for note in notes:
        if delete_function.isdigit() and int(delete_function) == note['ID'] or \
        delete_function.isdigit() and notes.index(note) + 1 == int(delete_function) or \
        delete_function in note['Описание_заметки'] or \
        delete_function in note['Заголовки']:
            find_note = note
            break

# Удаляем найденную заметку:
    if find_note:
        notes.remove(find_note)
        print('\nЗаметка успешно удалена!')
    else:
        print('\nОшибка, не удалось найти заметку!')

print('\nВаши заметки:')
for i, note in enumerate(notes, 1):
        print(f'\nЗаметка {i}. ID: {note['ID']}')
        print(f'Имя: {note['Имя']}')
        print(f'Описание заметки: {note['Описание_заметки']}')
        print(f'Текущая дата: {note['Текущая_дата'].strftime('%d.%m.%Y')}')
        print(f'Дата создания заметки: {note['Дата_создания'].strftime('%d.%m.%Y')}')
        #print(f'Дата истечения заметки: {note['Дата_истечения'].strftime('%d.%m.%Y')}')
        print(f'Заголовки заметки: {', '.join(note['Заголовки'])}')
        print(f'Статус заметки: {', '.join(note['Статус'])}')
        print(f'{(note['Дедлайн'])}')