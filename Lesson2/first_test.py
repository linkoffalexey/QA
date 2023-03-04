from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("file:///C:/Users/%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9/Desktop/example.html") # это обычно что-то наподобие: file:///C:/Users/.....
elementByLinkText = driver.find_element_by_link_text("Перейти к содержимому")
elementByPartialLinkText = driver.find_element_by_partial_link_text("Пере")
driver.quit()