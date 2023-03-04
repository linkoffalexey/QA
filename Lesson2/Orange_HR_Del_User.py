import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(3) # ставим ожидание 3 секунды, чтобы страница успела прогрузиться
login = driver.find_element_by_name("username") # объявляем переменную login, задаём ей значение селектора поля логин
login.send_keys("Admin") # команда send_keys("значение") – нужна для ввода информации в поле
password = driver.find_element_by_name("password") # объявляем переменную password, задаём ей значение селектора поля пароль
password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find.... .send_keys(..))
login_btn = driver.find_element_by_class_name("oxd-button") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
login_btn.click() # команда click() – нужна для нажатия(клика) на элемент
time.sleep(3)
PIM_btn = driver.find_element_by_link_text("PIM")
PIM_btn.click()
time.sleep(3)
Employer_ID = driver.find_element_by_css_selector(".oxd-input:nth-child(1)")
Employer_ID.send_keys("0262VV")
Search_btn = driver.find_element_by_css_selector(".oxd-form-actions>button:nth-child(2)")
Search_btn.click()
time.sleep(3)
Delete_btn = driver.find_element_by_css_selector(".bi-trash")
Delete_btn.click()
time.sleep(3)
Yes_btn = driver.find_element_by_css_selector(".orangehrm-modal-footer>button:nth-child(2)")
Yes_btn.click()
time.sleep(3)
driver.quit()
