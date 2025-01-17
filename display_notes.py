#Создаю список для сохранения заметок
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

#Функция проверки списка на наличие в нем сохраненных заметок
def display_notes(notes):
    if not notes:
        print('У вас нет сохраненных заметок!')
        return notes

#Вывод данных списка если в нем введены какие-либо параметры
print('\nВаши заметки:')
print('-' * 30)
for i, note in enumerate(notes, start=1):
        print(f"Заметка №{i}:")
        print(f"Имя пользователя: {note.get('username', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указано')}")
        print(f"Описание: {note.get('content', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указано')}")
        print(f"Дата создания: {note.get('created_date', 'Не указано')}")
        print(f"Дедлайн: {note.get('issue_date', 'Не указано')}")
        print("-" * 30)

#Вызов функции
display_notes(notes)