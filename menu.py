from datetime import datetime

# Список для хранения заметок
notes = []


# Функции для работы с заметками
def create_note():
    note = {}
    note['name'] = input('Введите ваше имя: ')
    note['content'] = input('Введите описание вашей заметки: ')
    note['title'] = input('Введите заголовок вашей заметки: ')
    note['status'] = input('Введите статус вашей заметки (новая, в процессе, отложено): ')
    note['create_date'] = datetime.now().strftime('%d-%m-%Y')

    while True:
        issue_date = input('Введите дату окончания действия заметки в формате ДД.ММ.ГГГГ: ')
        try:
            note['issue_date'] = datetime.strptime(issue_date, '%d.%m.%Y').strftime('%d.%m.%Y')
            break
        except ValueError:
            print('Ошибка! Пожалуйста введите верный формат даты (ДД.ММ.ГГГГ)!')

    notes.append(note)
    print('Заметка успешно создана!')


def display_notes():
    if not notes:
        print('У вас нет сохранённых заметок!')
        return

    print('\nВаши заметки:')
    print('-' * 30)
    for i, note in enumerate(notes, start=1):
        print(f"Заметка №{i}:")
        print(f"Имя пользователя: {note.get('name', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указано')}")
        print(f"Описание: {note.get('content', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указано')}")
        print(f"Дата создания: {note.get('create_date', 'Не указано')}")
        print(f"Дедлайн: {note.get('issue_date', 'Не указано')}")
        print("-" * 30)


def update_note():
    if not notes:
        print('У вас нет сохранённых заметок!')
        return

    display_notes()
    try:
        note_index = int(input('Введите номер заметки для редактирования: ')) - 1
        if 0 <= note_index < len(notes):
            note = notes[note_index]
            print('Доступные поля для редактирования:', list(note.keys()))
            field = input('Введите поле для редактирования: ')
            if field in note:
                if field == 'issue_date':
                    while True:
                        new_date = input('Введите новую дату (ДД.ММ.ГГГГ): ')
                        try:
                            note[field] = datetime.strptime(new_date, '%d.%m.%Y').strftime('%d.%m.%Y')
                            break
                        except ValueError:
                            print('Ошибка! Неверный формат даты.')
                else:
                    note[field] = input(f'Введите новое значение для {field}: ')
                print('Заметка успешно обновлена!')
            else:
                print('Ошибка: Неверное поле.')
        else:
            print('Ошибка: Неверный номер заметки.')
    except ValueError:
        print('Ошибка: Введите корректный номер.')


def delete_note():
    if not notes:
        print('У вас нет сохранённых заметок!')
        return

    display_notes()
    try:
        note_index = int(input('Введите номер заметки для удаления: ')) - 1
        if 0 <= note_index < len(notes):
            del notes[note_index]
            print('Заметка успешно удалена!')
        else:
            print('Ошибка: Неверный номер заметки.')
    except ValueError:
        print('Ошибка: Введите корректный номер.')


def search_notes():
    if not notes:
        print('У вас нет сохранённых заметок!')
        return

    keyword = input('Введите ключевое слово для поиска: ').lower()
    status = input('Введите статус для фильтрации (оставьте пустым для пропуска): ').lower()

    filtered_notes = []
    for note in notes:
        matches_keyword = keyword in note['content'].lower() or keyword in note['title'].lower() or keyword in note[
            'name'].lower()
        matches_status = status in note['status'].lower() if status else True
        if matches_keyword and matches_status:
            filtered_notes.append(note)

    if filtered_notes:
        print("\nНайдены заметки:")
        print("-" * 30)
        for i, note in enumerate(filtered_notes, start=1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note.get('name', 'Не указано')}")
            print(f"Заголовок: {note.get('title', 'Не указано')}")
            print(f"Описание: {note.get('content', 'Не указано')}")
            print(f"Статус: {note.get('status', 'Не указано')}")
            print(f"Дата создания: {note.get('create_date', 'Не указано')}")
            print(f"Дедлайн: {note.get('issue_date', 'Не указано')}")
            print("-" * 30)
    else:
        print("Заметки не найдены.")


# Главное меню
def main_menu():
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")
        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            create_note()
        elif choice == "2":
            display_notes()
        elif choice == "3":
            update_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            search_notes()
        elif choice == "6":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Ошибка: Недопустимый выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()