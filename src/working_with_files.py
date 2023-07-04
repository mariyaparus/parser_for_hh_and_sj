from abc import ABC, abstractmethod
import json


class WorkingWithFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @staticmethod
    def add_vacancy(obj):
        pass

    @staticmethod
    def remove_vacancy(vacancy_del):
        pass

    @staticmethod
    def top_salary_vacancy(obj):
        pass


class JsonWorkingWithFile(WorkingWithFile):
    """Класс для работы с JSON-файлами"""

    @staticmethod
    def add_vacancy(obj):
        file = open('vacancy.json', mode='w', encoding='utf8')
        my_list = [v.to_dict() for v in obj]
        file.write(json.dumps(my_list, ensure_ascii=False, indent=2))
        file.close()

    @staticmethod
    def remove_vacancy(vacancy_del):

        with open('vacancy.json', mode='r', encoding='utf8') as file:
            obj = json.load(file)
            for v in obj:
                if v['Профессия'] == vacancy_del:
                    obj.remove(v)
            with open('vacancy.json', mode='w', encoding='utf8') as out_file:
                json.dump(obj, out_file, ensure_ascii=False, indent=2)
            out_file.close()

    @staticmethod
    def get_info(vacancy):
        with open('vacancy.json', mode='r', encoding='utf8') as file:
            obj = json.load(file)
            for v in obj:
                try:
                    if vacancy in v['Профессия']:
                        print(v)
                except Exception:
                    raise Exception("Извините вакансия не найдена =(")

    @staticmethod
    def top_salary_vacancy(obj):
        with open('vacancy.json', mode='r', encoding='utf8') as file:
            obj = json.load(file)
            object_ = sorted(obj, key=lambda salary: salary['З/п от'])
            print(object_)

    # def read_file(self, file_name):
    #     """
    #     Чтение json-файла
    #     """
    #     with open(file_name, 'r', encoding='utf-8') as file:
    #         data = json.load(file)
    #         return data
    #
    # def write_file(self, file_name, data):
    #     """
    #     Запись в json-файл
    #     """
    #     with open(file_name, 'w', encoding='utf-8') as file:
    #         json.dump(data, file)
    #
    # def delete(self, file_name):
    #     """Удаление json-файла"""
    #     if os.path.exists(file_name):
    #         os.remove(file_name)
