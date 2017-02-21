import requests
import time


def get_json_from_superjob(request, auth_data):
    try:
        response = requests.get('https://api.superjob.ru/2.0/%s' % request, headers=auth_data)
        return response.json()
    except ConnectionError:
        print('Connection error!')
    except requests.HTTPError:
        print('HTTP error')
    except TimeoutError:
        print('Timeout error')
    return {}


def sleep_if_max_requests_in_time(time_from_first_request, num_of_recent_request, max_requests, time_of_max_requests):
    if num_of_recent_request == max_requests and time_from_first_request % time_of_max_requests != 0:
        time.sleep(time_of_max_requests - time_from_first_request)
        return time.time()
    else:
        return time_from_first_request


def get_api_key_from_file(path_to_read_file):
    my_api_key = ''
    try:
        with open(path_to_read_file, 'r') as f:
            my_api_key = f.read()
    except FileNotFoundError:
        print()
    return {'X-Api-App-Id': my_api_key}


def generate_request_for_vacancies_by_parameters(parameters):
    result = 'vacancies/?'
    arrays = {'ids', 'keywords', 'm', 't', 'o', 'c', 'driving_licence', 'catalogues'}
    for key in parameters:
        if key not in arrays:
            result += '%s=%s&' % (key, parameters[key])
        elif key == 'catalogues':
            result += 'catalogues='
            for catalogue in parameters[key]:
                result += '%d,' % catalogue
            result += '%s&' % result[:-1]
        elif key == 'driving_licence':
            for num_of_category, category in enumerate(parameters[key]):
                result += 'driving_licence[%d]=%s&' % (num_of_category, category)
        elif key == 'keywords':
            for num_of_keyword, keyword in enumerate(parameters[key]):
                result += '%s[%d][%s]&' % (key, num_of_keyword, keyword)
    return result[:-1]


if __name__ == '__main__':
    params = {'town': 'Москва', 'keywords': ['программист', 'разработчик'],
              'catalogues': [56, 52, 51, 48, 47, 604, 42, 41, 40, 546, 503, 37, 36], 'count': 2}
    my_auth_data = get_api_key_from_file('api_key.txt')
    req = generate_request_for_vacancies_by_parameters(params)
    print('Testing of generate_request_by_parameters: %s' % req)
    print('Testing of get_json_from_superjob:',
          *get_json_from_superjob(generate_request_for_vacancies_by_parameters(params), my_auth_data)['objects'],
          sep='\n', end='\n')
