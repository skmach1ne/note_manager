from datetime import datetime
notes = [
    {
        'username': input('Введите имя пользователя: '),
        'title': input('Введите заголовок вашей заметки: '),
        'content': input('Введите описание  заметки: '),
        'status': input('Введите статус  заметки: '),
        'created_date': input('Введите дату создания вашей заметки: '),
        'issue_date': input('Введите дату истечения вашей заметки: ')
    },
    {
        'username': input('Введите имя пользователя: '),
        'title': input('Введите заголовок вашей заметки: '),
        'content': input('Введите описание  заметки: '),
        'status': input('Введите статус  заметки: '),
        'created_date': input('Введите дату создания вашей заметки: '),
        'issue_date': input('Введите дату истечения вашей заметки: ')
    }
]
# Функции для работы с заметками

def search_notes():
    if not notes:
        print('У вас нет сохранённых заметок!')
        return

    keyword = input('Введите ключевое слово для поиска: ').lower()
    status = input('Введите статус для фильтрации (оставьте пустым для пропуска): ').lower()

    filtered_notes = []
    for note in notes:
        matches_keyword = (
            keyword in note['content'].lower() or
            keyword in note['title'].lower() or
            keyword in note['username'].lower()  # Исправлено с 'name' на 'username'
        )
        matches_status = status in note['status'].lower() if status else True
        if matches_keyword and matches_status:
            filtered_notes.append(note)

    if filtered_notes:
        print("\nНайдены заметки:")
        print("-" * 30)
        for i, note in enumerate(filtered_notes, start=1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note.get('username', 'Не указано')}")  # Исправлено с 'name' на 'username'
            print(f"Заголовок: {note.get('title', 'Не указано')}")
            print(f"Описание: {note.get('content', 'Не указано')}")
            print(f"Статус: {note.get('status', 'Не указано')}")
            print(f"Дата создания: {note.get('created_date', 'Не указано')}")  # Исправлено с 'create_date' на 'created_date'
            print(f"Дедлайн: {note.get('issue_date', 'Не указано')}")
            print("-" * 30)
    else:
        print("Заметки не найдены.")
search_notes()