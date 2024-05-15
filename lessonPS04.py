# Этот код использует библиотеку wikipediaapi для взаимодействия с Википедией.
# 'wikipediaapi:' - Python-библиотека для доступа к данным Википедии через их API.
# Позволяет извлекать информацию о страницах, категориях, ссылках и другом.

import wikipediaapi

def print_paragraphs(page):
    paragraphs = page.text.split('\n') # Получает текст страницы и разделяет его на абзацы по переносам строк.
    for i, paragraph in enumerate(paragraphs, start=1): # Итерирует по абзацам, начиная с 1.
        if paragraph:   #Проверяет, не пуст ли абзац.
            print(f"{i}. {paragraph}\n")
            input("Нажмите Enter для продолжения...") # Приостанавливает вывод параграфов,
                                                      # пока не будет нажмат Enter.

def choose_linked_page(page):
    links = list(page.links.values()) # Получает все внутренние ссылки на странице (объекты страниц Википедии) и преобразует их в список.
    for index, link in enumerate(links[:10], start=1): # Ограничивает вывод до первых 10 связанных страниц.
        print(f"{index}. {link.title}")

    choice = int(input("Выберите страницу (1-10): ")) - 1 # Запрашивает выбор страницы.
    if 0 <= choice < len(links):
        return links[choice] # Возвращает выбранную страницу или None при неверном выборе.
    else:
        print("Неверный выбор.")
        return None

def main():
    # Создание объекта Wikipedia, с указанием языка, формата извлечения и пользовательского агента
    wiki_wiki = wikipediaapi.Wikipedia(
        language='ru',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent="MyCoolResearchApp/1.0 (myemail@example.com)"
    )
    # Запрашиваем поисковый запрос.
    query = input("Введите запрос для поиска на Википедии: ")
    page = wiki_wiki.page(query) # Проверяет, существует ли страница по заданному запросу.

    if not page.exists():
        print("Страница не найдена.")
        return
# Бесконечный цикл позволяет выбирать действия:
# При выборе связанной страницы (action == '2'), переменная page обновляется,
# что позволяет просматривать новую страницу в последующих итерациях.
    while True:
        print(f"Вы на странице: {page.title}")
        print("1. Просмотреть параграфы статьи")
        print("2. Перейти на связанную страницу")
        print("3. Выйти из программы")
        action = input("Выберите действие (1-3): ")

        if action == '1':
            print_paragraphs(page)
        elif action == '2':
            new_page = choose_linked_page(page)
            if new_page:
                page = new_page
        elif action == '3':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()