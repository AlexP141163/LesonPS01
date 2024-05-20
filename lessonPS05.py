# Импортируем необходимые библиотеки.
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер Firefox:
driver = webdriver.Firefox()

# Присваиваем переменной 'url' URL нужной страницы:
url = "https://www.divan.ru/category/svet"

# Открываем данную страницу:
driver.get(url)

# Задаем время ожидания на открытие страницы:
time.sleep(3)

# Создаем переменную 'lights' и ищем все карточки в директории "Свет" сайта "Диван.ру",
# и сохраняем весь список в переменную 'date':
lights = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
data = []
for light in lights:
    try:
        name = light.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = light.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = light.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        data.append({
            'name': name,
            'price': price,
            'url': url
        })
    except:
        print("Произошла ошибка при парсинге")
        continue  # В случае ошибки продолжаем работу:

# Выводим результат парсинга в файл 'output.csv':
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['name', 'price', 'url']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

# Закрываем драйвер Firefox:
driver.quit()

print("Все данные выведены в файл 'output.csv'")