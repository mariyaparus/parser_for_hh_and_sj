import json

import requests

from src.working_with_api import Api
from src.working_with_vacancies import Vacancy


class HeadHunterApi(Api):
    """
    Класс для работы с API Head Hanter
    """

    url = 'https://api.hh.ru/vacancies'

    def __init__(self):
        pass

    def get_vacancies(self, job_title):
        """Запрос к API HH и парсинг полученных вакансий"""
        req = requests.get(self.url)
        data = req.content.decode()
        req.close()
        js_obj = json.loads(data)

        all_vacancy = []
        for obj in js_obj['items']:
            salary = obj.get('salary') or {}
            all_vacancy.append(Vacancy(**{
                'title': obj['name'],
                'salary_from': salary.get('from', 0),
                'salary_to': salary.get('to', 0),
                'employer': obj['employer']['name'],
                'url': obj['url'],
                'req': obj['snippet']['requirement']
            }))

        return all_vacancy
