#!/usr/bin/python3
"""A script that fetches data with an API and exports it to JSON"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    user = get("https://jsonplaceholder.typicode.com/users/{}/".
               format(argv[1])).json()
    tasks = get("https://jsonplaceholder.typicode.com/users/{}/todos".
                format(argv[1])).json()
    tasks_list = []
    for task in tasks:
        tasks_list.append({'task': task.get('title'),
                           'completed': task.get('completed'),
                           'username': user.get('username')})
    json_dict = {argv[1]: tasks_list}

    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(json_dict, f)
