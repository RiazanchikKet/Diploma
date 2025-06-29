import configparser

global_config = configparser.ConfigParser()
global_config.read('test_config.ini')


class ConfigProvaider:

    def __init__(self):
        self.config = global_config

    def get(self, section: str, prop: str):
        return self.config[section].get(prop)
