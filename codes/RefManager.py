class RefManager:
    def __init__(self,path_to_file_with_refs = "../infrastructure/refs.txt" ):
        self.__file_with_refs = open(path_to_file_with_refs, 'r')
        self.read_file_with_refs()

    def read_file_with_refs(self):
        str_file_with_refs = self.__file_with_refs.read()
        self.__refs = self.parse_str_refs(str_file_with_refs)
        print("{size} refs that were read from file {list_of_refs}".format(size = len(self.__refs),list_of_refs = self.__refs))


    def parse_str_refs(self,str_refs):
        if str_refs:
            list_of_refs = str_refs.split(",")
            if not list_of_refs:
                return []
            else:
                return [element.strip() for element in list_of_refs if
                        element and element.count("instagram.com") == 1]  #
        else:
            return []

    def get_refs(self):
        return self.__refs