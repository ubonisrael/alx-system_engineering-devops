#!/usr/bin/python3
"""A script that fetches data with an API and displays it"""
from sys import argv
from requests import get

if __name__ == "__main__":
    user = get("https://jsonplaceholder.typicode.com/users/{}/".
               format(argv[1])).json()
    tasks = get("https://jsonplaceholder.typicode.com/users/{}/todos".
                format(argv[1])).json()
    
    no_tasks = len(tasks)
    done_tasks = list(filter(lambda x: x.get("completed") is True, tasks))
    no_done_tasks = len(done_tasks)
    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), no_done_tasks, no_tasks))
    for task in done_tasks:
        print("\t {}".format(task['title']))
