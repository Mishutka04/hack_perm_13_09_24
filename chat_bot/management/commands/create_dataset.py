import csv
from django.core.management.base import BaseCommand
import requests

from bs4 import BeautifulSoup

from chat_bot.models import QueryAnswer

class Command(BaseCommand):
    help = 'Отображает текущее время'

    #def handle(self, *args, **kwargs):
        #for file_name in ("d1", "d2", "d3", "d4"):
        #    with open(f"{file_name}.csv", encoding='utf-8') as file:
        #        # Создаем объект reader, указываем символ-разделитель ","
        #        file_reader = csv.reader(file, delimiter=",")
        #        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        #        count = 0
        #        # Считывание данных из CSV файла
        #        for row in file_reader:
        #            if count == 0:
        #                # Вывод строки, содержащей заголовки для столбцов
        #                print(f'Файл содержит столбцы: {", ".join(row)}')
        #            else:
        #                # Вывод строк
        #                QueryAnswer.objects.create(answer=row[0])
#
        #            count += 1
        #        print(f'Добавлено {count} строк.')
        #help = 'Отображает текущее время'

    def handle(self, *args, **kwargs):
        # URL страницы FAQ
        url = "https://rutube.ru/api/info/pages/faq/?client=wdp"

        # Отправляем запрос
        response = requests.get(url)

        # Проверяем успешность запроса
        if response.status_code == 200:
            # print(response.json()['content'])
            # Парсинг HTML-кода
            soup = BeautifulSoup(response.json()['content'], 'html.parser')

            # Инициализация переменной для хранения результатов
            faq_data = []

            # Переменные для накопления данных
            current_section = None

            for elem in soup.find_all(['h2', 'p']):
                if elem.name == 'h2':
                    if current_section:  # если уже есть секция, сохраняем её
                        faq_data.append(current_section)
                    current_section = {'title': elem.text.strip(), 'content': ""}
                # elif elem.name == 'h2':
                #     if current_section:
                #         current_section['content'] += f"\n{elem.text.strip()}\n"
                elif elem.name == 'p':
                    if current_section:
                        current_section['content'] += f"{elem.text.strip()} "

            # Добавляем последнюю секцию
            if current_section:
                faq_data.append(current_section)

            # Убираем лишние пробелы
            for section in faq_data:
                section['content'] = section['content'].strip()

            # Печать результата для проверки
            for section in faq_data:
                QueryAnswer.objects.create(query=section['title'], answer=section['content'])
                #print(f"Title: {section['title']}\nContent: {section['content']}\n\n")
            print("Finish")
        else:
            print(f"Ошибка при запросе страницы: {response.status_code}")


