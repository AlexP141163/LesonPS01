from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Импортируем 'Keys' Модуль, используемый для отправки специальных клавиш, таких как Enter.
from selenium.webdriver.common.by import By  # Импортируем 'By' для использования в локаторах
import time # Импортируем 'time' для работы с временем, в частности, функция sleep используется для ожидания загрузки страницы.

def search_wikipedia(): #Создаёт новый экземпляр браузера Firefox.
    browser = webdriver.Firefox()
    browser.get("https://www.wikipedia.org/") # Переходит на главную страницу Википедии.

    search_query = input("Введите ваш запрос: ") #Запрашивает у пользователя ввод текста запроса.
    search_box = browser.find_element(By.NAME, "search") #Находит поле для поиска на странице по его атрибуту 'name'.
    search_box.send_keys(search_query + Keys.RETURN) #Вводит текст запроса пользователя в поле поиска и нажимает Enter для отправки запроса.

    time.sleep(2)  # Время для загрузки страницы

    # Бесконечный цикл, в котором предлагаются действия с текущей страницей:
    # просмотреть параграфы, перейти на связанную страницу или выйти.
    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Просмотреть параграфы статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Выберите опцию (1, 2 или 3): ")

        if choice == '1':
            paragraphs = browser.find_elements(By.CSS_SELECTOR, "p")
            for i, paragraph in enumerate(paragraphs):
                print(f"Параграф {i + 1}: {paragraph.text}\n")
        elif choice == '2':
            links = browser.find_elements(By.CSS_SELECTOR, "p a")
            for i, link in enumerate(links):
                print(f"Ссылка {i + 1}: {link.get_attribute('href')} - {link.text}")

            link_choice = int(input(f"Выберите ссылку для перехода (1-{len(links)}): ")) - 1
            links[link_choice].click()
            time.sleep(2)  # Дать время для загрузки новой страницы
        elif choice == '3':
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

    browser.quit()

search_wikipedia()