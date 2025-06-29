import json

my_file = open('test_data.json')
global_data = json.load(my_file)


class DataProvaider:

    def __init__(self):
        """
        Обращается к файлу 'test_data.json' и вычитывает его.
        """
        self.data = global_data

    def get(self, prop: str) -> str:
        """
        Возвращает из файла 'test_data.json' значение,
        соответствующее ключу, указанному при вызове метода.
        """
        return self.data.get(prop)
