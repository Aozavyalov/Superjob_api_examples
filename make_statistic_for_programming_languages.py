import re
import matplotlib.pyplot as plt
import numpy as np
from edit_data_from_json_file import read_vacancies_from_file

pattern_for_langs_search = {'C\+\+', 'C', 'C#', 'SQL', 'Java', 'xml', 'HTML', 'Visual Basic', 'xsl', 'Delphi', 'Pascal',
                            '1c|1с', 'Javascript', 'Basic', 'Python', 'PHP', 'Perl', 'Haskell', 'MatLab', 'Mathcad',
                            'object-c', 'Go', 'Scala', 'Assembler', 'Parser', 'Groovy', 'Forth', 'Ruby', 'Ada', 'Lisp',
                            'R', 'VB'}


def make_statistic_for_prog_langs(vacancies, prog_langs):
    founded_languages = {}
    statistic = {}
    for vacancy in vacancies:
        edited_profession = re.sub('[^\w\+\#]', ' ', vacancy['profession'])
        edited_candidat = re.sub('[^\w\+\#]', ' ', vacancy['candidat'])
        for language in prog_langs:
            if re.search(language.lower(), edited_profession.lower()) or re.search(language.lower(),
                                                                                   edited_candidat.lower()):
                buffer_list = []
                if vacancy['payment_to'] != None:
                    buffer_list.append(vacancy['payment_to'])
                if vacancy['payment_from'] != None:
                    buffer_list.append(vacancy['payment_from'])
                if vacancy['payment'] != None:
                    buffer_list.append(vacancy['payment'])
                if language in founded_languages:
                    founded_languages[language].append(max(buffer_list))
                else:
                    founded_languages[language] = [max(buffer_list)]
    for language in founded_languages:
        statistic[language] = int(sum(founded_languages[language]) / len(founded_languages[language]))
        if statistic[language] == 0:
            statistic.pop(language)
    return statistic


if __name__ == '__main__':
    path_to_file = 'edited_100_vacancies.json'
    read_vacancies = read_vacancies_from_file(path_to_file)
    if read_vacancies:
        res = make_statistic_for_prog_langs(read_vacancies, pattern_for_langs_search)
        if res != {}:
            payments = []
            for lang in sorted(res):
                print(lang, res[lang])
                payments.append(res[lang])
            plt.bar(np.arange(len(res)), payments, align='center', width=0.9)
            plt.xticks(np.arange(len(res)), sorted(res.keys()))
            plt.ylabel('Payment')
            plt.xlabel('Programming languages')
            plt.title('Programming language payment')
            plt.show()
