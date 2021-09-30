from selenium import webdriver as wd
import os
import time

# Запускаем браузер
browser = wd.Chrome()
browser.get('https://sbis.ru/')

# Переход к странице с ссылками, поочередное ожидание подгрузки элементов страницы
browser.implicitly_wait(20)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div[5]/div[5]').click()

browser.implicitly_wait(20)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[4]/a').click()

browser.implicitly_wait(20)
# Скролим до кнопки, которая в центре страницы
hidden_button = browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[3]/div/div/div[2]/div/div[3]/a')
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