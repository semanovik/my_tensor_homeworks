from selenium import webdriver as wd
import os
import time

# Запускаем браузер
browser = wd.Chrome()
try:
    browser.get('https://sbis.ru/')
    browser.find_element_by_css_selector('[href="/support"]').click()

    # Скролим до кнопки, которая в центре страницы
    hidden_button = browser.find_element_by_css_selector('[href="/download"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", hidden_button)
    hidden_button.click()

    # Список параметров для поиска эелементов
    links_text = ['Полная версия (294.40 MB)', 'Обновление (229.75 MB)', 'Полная версия (66.53 MB)',
                  'Скачать (6.4 МБ)', 'Скачать (47.5 МБ)']

    # Поиск элементов с последующей записью значений их атрибутов
    file = open(r'C:\Users\su.novikov\Desktop\links.txt', 'w', encoding='utf-8')
    for i in range(0, 5):
        file.write(browser.find_element_by_link_text(links_text[i]).get_attribute('href') + '\n')
        file.close()
finally:
    browser.close()
