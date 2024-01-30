
import requests


def extract_data():
    # извлекает данные из html и возвращает список

    # results = []
    #response = requests.get('http://127.0.0.1:8899/')
    #contents = response.text
    #print(response)
    #print(contents)

    data = {'user': 'user', 'text': 'text'}
    response = requests.get('http://127.0.0.1:8899/', params=data)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
        extract_data()