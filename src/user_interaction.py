from src.working_with_api_hh import HeadHunterApi
from src.working_with_api_sj import SuperJobApi
from src.working_with_files import JsonWorkingWithFile


def user_interaction():
    """
    Взаимодействие с пользователем
    """

    platforms = ['1', '2']

    user_input = input('Выберите платформу для поиска вакансий: 1 - HeadHunter , 2 - SuperJob \n')

    if user_input == platforms[0]:
        client = HeadHunterApi()

        search_query = input('Вы выбрали Head Hunter.\nВведите поисковый запрос: \n')
        hh_vacancy = client.get_vacancies(search_query)
        JsonWorkingWithFile().add_vacancy(hh_vacancy)
        print('Сформирован список вакансий \n')

        user_ch = input('Введите ключевое слово для фильтрации вакансий: \n')
        JsonWorkingWithFile().get_info(user_ch)

        user_pick = input('Хотите отсортировать вакансии по зарплате? \n')

        if user_pick == 'да' or 'yes':
            JsonWorkingWithFile().top_salary_vacancy(hh_vacancy)
        else:
            quit()

    elif user_input == platforms[1]:
        client = SuperJobApi()
        search_query = input("Вы выбрали Super Job.\nВведите поисковый запрос: \n")
        sj_vacancy = client.get_vacancies(search_query)
        JsonWorkingWithFile().add_vacancy(sj_vacancy)
        print('Сформирован список вакансий \n')

        user_ch = input('Введите ключевое слово для фильтрации вакансий: \n')
        JsonWorkingWithFile().get_info(user_ch)

        user_pick = input('Хотите отсортировать вакансии по зарплате? \n')

        if user_pick == 'да' or 'yes':
            JsonWorkingWithFile().top_salary_vacancy(sj_vacancy)
        elif user_pick == 'нет' or 'no':
            print('Программа завершена')

    elif user_input not in platforms:
        print('Такой платформы нет в списке')
