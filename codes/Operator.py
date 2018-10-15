from codes.RefManager import RefManager
from codes.SettingsManager import SettingsManager
from codes.InstaOperator import InstaOperator

import os,inspect
from random import randint
from time import sleep
from selenium import webdriver

class Operator:
    def __init__(self):
        self.__ref_manager = RefManager()
        self.__settings_manager = SettingsManager()

        self.__driver = self.initialize_driver()
        self.__insta_operator = InstaOperator(self.__driver)

        self.__refs =  self.__ref_manager.get_refs()


    def initialize_driver(self):
        current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))

        chromedriver = os.path.join(current_folder, "../infrastructure/chromedriver")
        driver = webdriver.Chrome(executable_path=chromedriver)
        driver.implicitly_wait(10)
        return driver

    def calculate_random_timer(self,timer):
        if timer < 5:
            return (2, 5)
        else:
            min_range = timer - int(timer / 2)
            max_range = timer + int(timer / 2)

            return (min_range, max_range)

    def check_amount_of_repeats(self,amount):
        if amount <= 0:
            return 1000000
        return amount

    def start_subscribing(self):
        print("start subscribing")
        for ref in self.__refs:
            self.__insta_operator.perform_action_after_login(ref,1,randint(*self.calculate_random_timer(self.__settings_manager.get_setting_value('general','timer_between_operations'))))

    def refresh_subscription(self):
        for i in range(self.check_amount_of_repeats( self.__settings_manager.get_setting_value('general','amount_repeats'))):
            for ref in self.__refs:
                pause = randint(*self.calculate_random_timer(self.__settings_manager.get_setting_value('general','timer_between_operations')))
                self.__insta_operator.perform_action_after_login(ref, 2, pause)

            print("sleep before sub unsub")

            sleep(self.__settings_manager.get_setting_value('general','timer_beetwen_refreshing'))

    def start_work(self):

        user_name = self.__settings_manager.get_setting_value('general','login')
        password = self.__settings_manager.get_setting_value('general','password')
        mail_user_name = self.__settings_manager.get_setting_value('mail','login')
        mail_password = self.__settings_manager.get_setting_value('mail','password')
        #print(self.__insta_operator.get_language_from_page())
        self.__insta_operator.logging_action(self.__refs[0],user_name,password,mail_user_name,mail_password)
        self.start_subscribing()
        self.refresh_subscription()

o = Operator()
o.start_work()


    
