#!/usr/bin/python3
"""A script that fetches data with an API and exports it to JSON"""
import json
from requests import get

if __name__ == "__main__":
    users = get("https://jsonplaceholder.typicode.com/users/").json()
    json_dict = {}

    for user in users:
        tasks_list = []
        tasks = get("https://jsonplaceholder.typicode.com/users/{}/todos".
                    format(user.get('id'))).json()
        for task in tasks:
            tasks_list.append({'username': user.get('username'),
                               'task': task.get('title'),
                               'completed': task.get('completed')})
            json_dict[user.get('id')] = tasks_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(json_dict, f)
