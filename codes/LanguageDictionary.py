class LanguageDictionary(object):

    EN_aliases = {
        "subscribe":"Follow",
        "unsubscribe":"Following",
        "unsubscribe_confirmation":"Unfollow",
        "login":"Log in",
        "enter":"Log in",
        "send_security_code":"Send Security Code"
    }
    RU_aliases = {

    }

    def __init__(self,lang = "en"):
        self.__active_language = lang

    def __getattr__(self, item):
        if self.__active_language == "en":
            return LanguageDictionary.EN_aliases[item]
        elif self.__active_language == "ru":
            return LanguageDictionary.RU_aliases[item]
        else:
            return object.__getattribute__(self, item)