"""
hw
"""

import json
import os
import requests

def write_json_file(file_name, data, mode):
    """
    записываем словарь в json файл
    """
    with open(file_name, mode, encoding='utf-8') as file:
        json.dump(data, file, indent=2)

def read_json_file(file_name: str) -> list:
    """
    читает json файл
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_data_from_api(url):
    """
    извлекает данные
    """
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    FILE_NAME = "task_1_all_data.json"

    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

    RESPONSE_URL = "https://jsonplaceholder.typicode.com/todos/"

    RANGE_API = 10
    DATA_LIST = []

    try:
        for i in range(1, RANGE_API + 1):
            data = get_data_from_api(f"{RESPONSE_URL}{i}")
            DATA_LIST.append(data)

        write_json_file(FILE_NAME, DATA_LIST)
    except requests.exceptions.RequestException as e:
        print(e)
