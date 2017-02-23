import get_data_from_superjob
import json


def get_vacancies(parameters, api_key, path_to_write_file=None):
    request = get_data_from_superjob.generate_request_for_vacancies_by_parameters(parameters)
    vacancies = get_data_from_superjob.get_json_from_superjob(request, api_key)
    if path_to_write_file:
        with open(path_to_write_file, 'w') as wf:
            wf.write(json.dumps(vacancies))
    return vacancies


if __name__ == '__main__':
    auth_data = get_data_from_superjob.get_api_key_from_file('api_key.txt')
    params = {'town': 'Москва', 'keywords': ['программист', 'разработчик'],
              'catalogues': [48], 'count': 100}
    path_to_file_with_vacancies = '100_vacancies.json'
    # testing of vacancies
    vacancies = get_vacancies(params, auth_data, path_to_file_with_vacancies)['objects']
    for vacancy in vacancies:
        print(vacancy['profession'], vacancy['town']['title'], sep='\t')
