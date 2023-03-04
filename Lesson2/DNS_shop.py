from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window() # раскрываем окно браузера на весь экран
driver.get("https://dns-shop.ru") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
logo = driver.find_element_by_id("header-logo") # укажем путь к логотипу (можно было написать и без части "logo=", почему так лучше, разберём в дальнейшем)
driver.get("https://wiktionary.org")
driver.find_element(By.ID, "searchInput")
driver.quit() # закроем драйвер в конце теста