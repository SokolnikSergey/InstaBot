from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from time import sleep
import os, sys, inspect
import configparser
import subprocess


config = configparser.ConfigParser()
config.read('settings.ini')

timer_between_operations = int(config['DEFAULT']['timer_between_oeprations'])
timeer_beetwen_sub_unsub = int(config['DEFAULT']['timer_beetwen_refreshing'])
user_name = config['DEFAULT']['login']
password = config['DEFAULT']['password']
amount_of_repeats = int(config['DEFAULT']['amount_repeats'])
mail_login = config['MAIL']['login']
mail_password = config['MAIL']['password']

current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))

# timer_between_operations = int(input("Timer between oeprations(sec):\n"))
# timeer_beetwen_sub_unsub = int(input("Timer beetwet_refreshing(sec):\n"))
#
# user_name = input("Enter your login:\n")
# password = input("Enter your password:\n")
# amount_of_repeats = int(input("Input amount of repeats (or amount around infinity 0 or less ):\n"))

str_list_refs = open('./refs.txt', 'r').read()


def calculate_random_timer(timer):
    if timer < 5:
        return (2, 5)
    else:
        min_range = timer - int(timer / 2)
        max_range = timer + int(timer / 2)

        return (min_range, max_range)


def parse_str_refs(str_refs):
    if str_refs:
        list_of_refs = str_refs.split(",")
        if not list_of_refs:
            return []
        else:
            return [element.strip() for element in list_of_refs if element and element.count("instagram.com") == 1]  #
    else:
        return []


def start_subscribing(list_of_refs, user_name, password, min_pause, max_pause):

    logging_action(list_of_refs[0], user_name, password)

    for ref in list_of_refs:
        print(ref)
        pause = randint(min_pause, max_pause)
        aсtion_after_loging(ref, 1, pause)


def check_amount_of_repeats(amount):
    if amount <= 0:
        return 1000000
    return amount


def refresh_subscription(list_of_refs, amount_of_repeats, timeout_sub_unsub, min_pause, max_pause):
    for i in range(check_amount_of_repeats(amount_of_repeats)):
        for ref in list_of_refs:
            pause = randint(min_pause, max_pause)
            aсtion_after_loging(ref, 2, pause)

        print("sleep before sub unsub")

        sleep(timeout_sub_unsub)


def get_element_with_wishing(ref, search_class, presence_class):
    driver.get(ref)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, presence_class)))
    elem = driver.find_element_by_class_name(search_class)

    return elem


def try_to_do_action(ref,elem_class,waiting_class,waiting_title,pause):
    for i in range(2):
        elem = get_element_with_wishing(ref, elem_class, waiting_class)
        if not (elem.text == waiting_title):
            elem.click()
            sleep(pause)
            if waiting_title == "Подписаться":
                elem = driver.find_elements_by_xpath("//button[contains(text(), 'Отменить подписку')]")
            if waiting_title == "Follow":
                elem = driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")
                
                if elem:
                    elem[0].click()
                    sleep(pause)
        else:
            break

def aсtion_after_loging(ref, action, pause):
    try:
        elem = get_element_with_wishing(ref, "oF4XW", "oF4XW")
        if action == 1:
            
            if elem.text == "Подписки" :
                try_to_do_action(ref,"oF4XW","oF4XW","Подписаться",pause)
                try_to_do_action(ref, "oF4XW", "oF4XW", "Подписки", pause)

            
            if elem.text == "Подписаться":
                try_to_do_action(ref, "oF4XW", "oF4XW", "Подписки", pause)


            # in inglish 
            if elem.text == "Following" :
                try_to_do_action(ref,"oF4XW","oF4XW","Follow",pause)
                try_to_do_action(ref, "oF4XW", "oF4XW", "Following", pause)


            if elem.text == "Follow":
                try_to_do_action(ref, "oF4XW", "oF4XW", "Following", pause)

        elif action == 2:
            elem = get_element_with_wishing(ref, "oF4XW", "oF4XW")
            if elem.text == "Подписки":
                try_to_do_action(ref, "oF4XW", "oF4XW", "Подписаться", pause)
                try_to_do_action(ref, "oF4XW", "oF4XW", "Подписки", pause)

            if elem.text == "Подписаться":
                try_to_do_action(ref, "oF4XW", "oF4XW", "Подписки", pause)

            #in inglish 
            if elem.text == "Following":
                try_to_do_action(ref, "oF4XW", "oF4XW", "Follow", pause)
                try_to_do_action(ref, "oF4XW", "oF4XW", "Following", pause)

            if elem.text == "Follow":
                try_to_do_action(ref, "oF4XW", "oF4XW", "Following", pause)


    except Exception as ex:
        print(ex)
        print("Error action after logging")



def get_verification_code():
    pass


def logging_action(ref, user_name, password):
    driver.get(ref)
    elem = driver.find_element_by_class_name("tdiEy")
    elem.click()

    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        elem = driver.find_element_by_name("username")
        elem.send_keys(user_name)
        elem = driver.find_element_by_name("password")
        elem.send_keys(password)
        elem = driver.find_element_by_class_name("oF4XW")
        elem.click()
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "XrOey"))
        )
        elem = driver.find_elements_by_xpath("//button[contains(@class, 'chBAG')]")

        if elem:
            elem[0].click()
            sleep(1)
        
      
        elem = driver.find_elements_by_xpath("//button[contains(@class, 'chBAG')]")
        if elem:
            elem[0].click()
            sleep(1)



    except:
        print("Error")

        #if verification occured . WE need to read from mail verification code 
        elem = driver.find_elements_by_xpath("//button[contains(@class, 'chBAG')]")
        if elem:
            elem[0].click()
            sleep(1)
        
        print("try find verification")
        element_send_verification_code = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oF4XW"))
        )
        if element_send_verification_code.text == "Send Security Code":
            element_send_verification_code.click()
            sleep(1)
            subprocess.run(["ruby", "mail_reader.rb",mail_login,mail_password])

        #read file with code from mruby process , that parse last messages from instagram 
        if os.path.exists("./file_with_code"):
            with open("./file_with_code","r") as file_with_code:
                code = file_with_code.readline()

                #can't test this logic -> not always appears
                
                elem = driver.find_element_by_class_name("_281Ls")
                ActionChains(driver).move_to_element(elem).perform()
                
                for number in code :
                    sleep(1)
                    print("number of code inserted ->" , code)
                    elem.send_keys(number)

                sleep(5)
                
                elem = driver.find_element_by_class_name("oF4XW")
                ActionChains(driver).move_to_element(elem).perform()         
                elem.click()
                sleep(5)
                    
        else:
            #exit because no code found in email , but we need to pass verification 
            print("exit because no code found in email , but we need to pass verification")
            exit(15)
                

        



def init_driver():
    chromedriver = os.path.join(current_folder, "./chromedriver")
    driver = webdriver.Chrome(executable_path=chromedriver)
    return driver


driver = init_driver()

driver.implicitly_wait(10)
list_refs = parse_str_refs(str_list_refs)
print(list_refs)
operations_timeout_range = calculate_random_timer(timer_between_operations)
print(operations_timeout_range)
start_subscribing(list_refs, user_name, password, *operations_timeout_range)
sleep(timeer_beetwen_sub_unsub)
refresh_subscription(list_refs, amount_of_repeats, timeer_beetwen_sub_unsub, *operations_timeout_range)


