import requests


def get_json_from_superjob(request, auth_data):
    try:
        responce = requests.get('https://api.superjob.ru/2.0/%s' % request, headers=auth_data)
        return responce.json()
    except ConnectionError:
        print('Connection error!')
    except requests.HTTPError:
        print('HTTP error')
    except TimeoutError:
        print('Timeout error')
    return {}

if __name__ == '__main__':
    my_api_key = str()
    with open('api_key.txt', 'r') as f:
        my_api_key = f.read()
    my_auth_data = {'X-Api-App-Id': my_api_key}
    print(get_json_from_superjob('vacancies/?t=4&count=100', my_auth_data))
