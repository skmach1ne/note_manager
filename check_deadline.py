from datetime import datetime
# Создаем словарь для хранения информации о заметке
note = {}


# Сбор данных от пользователя
note["Имя"] = input("Введите имя пользователя: ")
note["Описание"] = input("Введите описание заметки: ")
created_date = input("Введите дату создания заметкив формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
current_date = datetime.now()
note["Дата_создания"] = datetime.strptime(created_date, "%d-%m-%Y")
note["Дата_истечения"] = datetime.strptime(issue_date, "%d-%m-%Y")
note ["Текущая_дата"] = current_date
date_difference = (note['Текущая_дата'] - note['Дата_истечения']).days
date_difference_plus = (note['Дата_истечения'] - note['Текущая_дата']).days

# Добавляем бесконечный цикл заголовков в список внутри словаря
note["Заголовки"] = []
while True:
    title = input("Введите название заголовка (или оставьте строку пустой для завершения): ")
    if title == '':
        break
    note["Заголовки"].append(title)

# Добавляем выбор статуса заметки
note["Статус"] = []
while True:
    status = input("Для изменения статуса введите цифру: \n1. Выполнено \n2. В процессе \n3. Отложено \n")
    status_1 = "Выполнено"
    status_2 = "В процессе"
    status_3 = "Отложено"
    try:
        status = int(status) #Преобразую ввод из типа строка в число
    except ValueError:
        print("Ошибка: введите Число из предложенных!") #Создаю уведомления для пользователя, чтобы он вводил только цифру из предложенных.
        continue

    if status == 1:
        note["Статус"].append(status_1)
    elif status == 2:
     note["Статус"].append(status_2)
    elif status == 3:
     note["Статус"].append(status_3)
    else:
        print('Введите цифру из предложенных!')
        continue
    break

# Выводим собранные данные
print("\nСобранная информация о заметке:")
print(f"Имя: {note['Имя']}")
print(f"Описание: {note['Описание']}")
print(f"Статус: {note['Статус']}")

#Выводим Дату с корректировкой по формату
print(f"Текущая дата: {note['Текущая_дата'].strftime('%d-%m-%Y')}")
print(f"Дата создания: {note['Дата_создания'].strftime('%d-%m-%Y')}")
print(f"Дата истечения: {note['Дата_истечения'].strftime('%d-%m-%Y')}")

while True:
    if date_difference > 0:
        # Форматируем вывод для прошедших дедлайнов
        date_difference = abs(date_difference)
        if date_difference == 1:
            day_word = "День"
        elif 2 <= date_difference <= 4:
            day_word = "Дня"
        else:
            day_word = "Дней"
        print(f"Дедлайн истек {date_difference} {day_word} назад.")
        break
    elif date_difference < 0:
        # Форматируем вывод для будущих дедлайнов
        if date_difference == 1:
            day_word = "День"
        elif 2 <= date_difference <= 4:
            day_word = "Дня"
        else:
            day_word = "Дней"
        print(f"Дедлайн истекает через {date_difference_plus} {day_word}.")
        break
    else:
        print("Дедлайн сегодня!")
        break

#Выводим заголовки заметки
print(f'Заголовки вашей заметки: {note["Заголовки"]}')

