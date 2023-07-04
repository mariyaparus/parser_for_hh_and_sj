from abc import ABC, abstractmethod


class Api(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self, job_title):
        pass
