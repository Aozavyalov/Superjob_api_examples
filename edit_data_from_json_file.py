import json


def edit_data_from_json_file(path_to_input_file, path_to_output_file, required_data):
    data_from_json, edited_data = [], []
    try:
        with open(path_to_input_file, 'r') as in_file:
            data_from_json = json.loads(in_file.read())['objects']
    except FileNotFoundError:
        print('There is no such file!')
        return {}
    for vacancy in data_from_json:
        buffer_dict = {}
        for key in vacancy:
            if key in required_data:
                buffer_dict[key] = vacancy[key]
        edited_data.append(buffer_dict)
    edited_json_data = {'objects': edited_data}
    with open(path_to_output_file, 'w') as out_file:
        out_file.write(json.dumps(edited_json_data))
    return edited_json_data


if __name__ == '__main__':
    required_data = {'profession', 'payment', 'payment_from', 'payment_to', 'education', 'experience', 'maritalstatus', 'children', 'languages',
                     'driving_licence', 'town', 'age_from', 'age_to', 'gender'}
    print(*edit_data_from_json_file('100_vacancies.json', 'edited_100_vacancies.json', required_data)['objects'], sep='\n')
