# Superjob_api_examples
Example of using SuperJob API

  get_data_from_superjob.py contains functions for reading api key from file, sendind request with key to api.superjob.ru, sleeping if it is too much request in time and creating a request with parameters. Useful functions for other tasks.
  
  100_vacancies_for_developers_in_moscow.py	contains function for getting vacancies with specific parameters and writing them to a file. Uses get_data_from_superjob.py

  edit_data_from_json_file.py gets file, made in previous task and write edited data(only needed for us) to another file.

  make_statistic_for_programming_languages.py	contains a dictionary with proggramming languages. It searchs them in the edited data from previous task and generate a statistic about programming language payment and make a graph.
