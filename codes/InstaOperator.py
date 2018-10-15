from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
import subprocess,os


class InstaOperator:
    def __init__(self,driver):
        self.__driver = driver

    #detect language of pages
    def get_language_from_page(self):
        self.__driver.get("https://www.instagram.com/") ##main page
        WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.ID, "react-root")))
        return self.__driver.find_elements_by_xpath("//html")[0].get_attribute("lang") ##return en or ru 

    def get_element_with_wishing(self,ref, search_class, presence_class):
        self.__driver.get(ref)
        WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, presence_class)))
        elem = self.__driver.find_element_by_class_name(search_class)

        return elem

    def try_to_do_action(self,ref, elem_class, waiting_class, waiting_title, pause):
        for i in range(2):
            elem = self.get_element_with_wishing(ref, elem_class, waiting_class)
            if not (elem.text == waiting_title):
                elem.click()
                sleep(pause)
                if waiting_title == "Подписаться":
                    elem = self.__driver.find_elements_by_xpath("//button[contains(text(), 'Отменить подписку')]")
                if waiting_title == "Follow":
                    elem = self.__driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")

                    if elem:
                        elem[0].click()
                        sleep(pause)
            else:
                break

    def logging_action(self,ref, user_name, password,mail_login,mail_password):
        self.__driver.get(ref)
        elem = self.__driver.find_element_by_class_name("tdiEy") #login button
        elem.click()

        try:
            element = WebDriverWait(self.__driver, 30).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            elem = self.__driver.find_element_by_name("username")
            elem.send_keys(user_name)
            elem = self.__driver.find_element_by_name("password")
            elem.send_keys(password)
            elem = self.__driver.find_elements_by_xpath("//button[contains(@class, 'oF4XW') and contains(./text(),'Log in')]")[0]
            elem.click()
            sleep(3)
            element = WebDriverWait(self.__driver, 30).until(
                 EC.presence_of_element_located((By.CLASS_NAME, "oF4XW")) #perform login button
             )



        except Exception as ex:
            print("Error login without verification" , ex)

            # if verification occured . WE need to read from mail verification code
            elem = self.__driver.find_elements_by_xpath("//button[contains(@class, 'chBAG')]")
            if elem:
                elem[0].click()
                sleep(1)

            print("try find verification")
            element_send_verification_code = WebDriverWait(self.__driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_5f5mN"))
            )
            if element_send_verification_code.text == "Send Security Code":
                element_send_verification_code.click()
                sleep(1)
                subprocess.run(["ruby", "mail_reader.rb", mail_login, mail_password])

            # read file with code from mruby process , that parse last messages from instagram
            if os.path.exists("./file_with_code"):
                with open("./file_with_code", "r") as file_with_code:
                    code = file_with_code.readline()

                    # can't test this logic -> not always appears

                    elem = self.__driver.find_element_by_class_name("_281Ls")
                    ActionChains(self.__driver).move_to_element(elem).perform()

                    for number in code:
                        sleep(1)
                        print("number of code inserted ->", code)
                        elem.send_keys(number)

                    sleep(5)

                    elem = self.__driver.find_element_by_class_name("_5f5mN")
                    ActionChains(self.__driver).move_to_element(elem).perform()
                    elem.click()
                    sleep(5)

            else:
                # exit because no code found in email , but we need to pass verification
                print("exit because no code found in email , but we need to pass verification")
                exit(15)

    #subscribe or unsubscribe depends on arguments
    def perform_action_after_login(self,ref, action, pause):
        try:
            elem = self.get_element_with_wishing(ref, "_5f5mN", "_5f5mN")
            if action == 1:

                if elem.text == "Подписки":
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Подписаться", pause)
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Подписки", pause)

                if elem.text == "Подписаться":
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Подписки", pause)

                # in inglish
                if elem.text == "Following":
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Follow", pause)
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Following", pause)

                if elem.text == "Follow":
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Following", pause)

            elif action == 2:
                elem = self.get_element_with_wishing(ref, "_5f5mN", "_5f5mN")
                if elem.text == "Подписки":
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Подписаться", pause)
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Подписки", pause)

                if elem.text == "Подписаться":
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Подписки", pause)

                # in inglish
                if elem.text == "Following":
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Follow", pause)
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Following", pause)

                if elem.text == "Follow":
                    self.try_to_do_action(ref, "_5f5mN", "_5f5mN", "Following", pause)


        except Exception as ex:
            print(ex)
            print("Error action after logging")

