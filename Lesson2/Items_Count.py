import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
driver.get("https://www.saucedemo.com/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(3)
Username = driver.find_element_by_id("user-name")
Password = driver.find_element_by_id("password")
Username.send_keys("standard_user")
Password.send_keys("secret_sauce")
Login_btn = driver.find_element_by_id("login-button")
Login_btn.click()
Add_btn1 = driver.find_element_by_id("add-to-cart-sauce-labs-bike-light")
Add_btn2 = driver.find_element_by_id("add-to-cart-sauce-labs-bolt-t-shirt")
Add_btn3 = driver.find_element_by_id("add-to-cart-sauce-labs-onesie")
time.sleep(1)
Add_btn1.click()
time.sleep(1)
Add_btn2.click()
time.sleep(1)
Add_btn3.click()
time.sleep(1)
Cart = driver.find_element_by_css_selector("a.shopping_cart_link")
Cart.click()

items_count = driver.find_elements_by_css_selector("div.inventory_item_name")  # находим список всех элементов в корзине
# проверка что в корзине действительно 3 товара (добавьте в конец теста)
if len(items_count) == 3:  # после 1-го урока можем теперь создать небольшую конструкцию для проверки кол-ва товаров
    print("В корзине 3 товара")  # len здесь посчитает количество элементов, найденных при помощи find_elements
else:
    print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))
