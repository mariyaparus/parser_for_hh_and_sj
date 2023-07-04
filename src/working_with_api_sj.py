import json
import os

import requests

from src.working_with_api import Api
from src.working_with_vacancies import Vacancy


class SuperJobApi(Api):
    """
    Класс для работы с API Super Job
    """

    # API_KEY = {'X-Api-App-Id': os.getenv('SJ_API_KEY')}
    # api_key: str = os.getenv("SJ_API_KEY")
    # headers = {'X-Api-App-Id': api_key}
    # url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        pass

    def get_vacancies(self, job_title):
        params = {'count': 50,
                  'keyword': job_title
                  }
        api_key: str = os.getenv("SJ_API_KEY")
        headers = {'X-Api-App-Id': api_key}
        req = requests.get('https://api.superjob.ru/2.0/%s' % 'vacancies/', params, headers=headers)
        data = req.content.decode()
        req.close()
        js_obj = json.loads(data)

        all_vacancy = []
        for obj in js_obj['objects']:
            all_vacancy.append(Vacancy(**{
                'title': obj['profession'],
                'salary_from': obj['payment_from'],
                'salary_to': obj['payment_to'],
                'employer': obj['firm_name'],
                'url': obj['link'],
                'req': obj['candidat']
            }))
        return all_vacancy
