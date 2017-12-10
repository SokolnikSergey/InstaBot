from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/mikaa10_10/")
elem = driver.find_element_by_class_name("_qv64e")
elem.click()

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    elem = driver.find_element_by_name("username")
    elem.send_keys("sokol98_98@mail.ru")
    elem = driver.find_element_by_name("password")
    elem.send_keys("0289zteQ")
    elem = driver.find_element_by_class_name("_qv64e")
    elem.click()
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_68sh8"))
    )


except:
    print("Error")

elem = driver.find_element_by_class_name("_qv64e")
elem.click()
# elem = driver.find_element_by_class_name("_qv64e")
# print(elem.text)
#
# elem.click()
#<div class=""><div class="_sjplo"><input class="_ph6vk _o716c" aria-describedby="" aria-label="Имя пользователя" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="30" name="username" placeholder="Имя пользователя" value="" type="text"><div class="_gaby6"></div></div></div>