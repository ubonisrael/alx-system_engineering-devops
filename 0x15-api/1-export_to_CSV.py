#!/usr/bin/python3
"""A script that fetches data with an API and displays it"""
import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    user = get("https://jsonplaceholder.typicode.com/users/{}/".
               format(argv[1])).json()
    tasks = get("https://jsonplaceholder.typicode.com/users/{}/todos".
                format(argv[1])).json()

    no_tasks = len(tasks)
    done_tasks = list(filter(lambda x: x.get("completed") is True, tasks))
    no_done_tasks = len(done_tasks)

    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user.get("id"), user.get("username"),
                             task.get("completed"), task.get("title")])
