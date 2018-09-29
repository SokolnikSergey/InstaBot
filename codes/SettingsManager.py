import configparser

class SettingsManager:
    
    def __init__(self,path_to_settings_file = '../infrastructure/settings.ini'):
        self.__config_file = configparser.ConfigParser()
        self.__config_file.read(path_to_settings_file)

        self.__general_settings = {}
        self.__mail_settings = {}

        self.get_general_settings()
        self.get_mail_settings()


    def get_general_settings(self):
        self.__general_settings.update({"timer_between_operations" : int(self.__config_file['DEFAULT']['timer_between_operations'])})
        self.__general_settings.update({"timer_between_sub_unsub" : int(self.__config_file['DEFAULT']['timer_beetwen_refreshing'])})
        self.__general_settings.update({"login" : self.__config_file['DEFAULT']['login']})
        self.__general_settings.update({"password" : self.__config_file['DEFAULT']['password']})
        self.__general_settings.update({"amount_of_repeats" : int(self.__config_file['DEFAULT']['amount_repeats'])})

    def get_mail_settings(self):
        self.__mail_settings.update({"login" : self.__config_file['MAIL']['login']})
        self.__mail_settings.update({"password" : self.__config_file['MAIL']['password']})


    #return settings value by type ( mail / general)
    def get_setting_value(self,type,name_of_parameter):
        settings = None

        if type == 'general':
            settings = self.__general_settings
        elif type == 'mail':
            settings = self.__mail_settings
        return settings[name_of_parameter]
