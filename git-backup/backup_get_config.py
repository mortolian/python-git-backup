import json


class GetJsonConfig:
    """
    Class to read a JSON configuration file and return it
    """

    def __init__(self, file_src):
        self.file_src = file_src
        self.config_json = self.__get_config_file_content()

    def __get_config_file_content(self):
        """
        Opens a file, reads the json content and returns the json file content.
        """
        try:
            # Read the config
            file = open(self.file_src, "r")
            config_json_string = file.read()
            config_json_obj = json.loads(config_json_string)
            file.close()
            return config_json_obj
        except IOError:
            print('Could not successfully read the config file: ', self.file_src)

    def get_content(self):
        return self.config_json
