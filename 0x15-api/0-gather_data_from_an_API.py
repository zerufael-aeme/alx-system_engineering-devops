#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(sys.argv[1])
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    todos = requests.get(url_todos)
    users = requests.get(url_users)

    if todos.status_code == 200 and users.status_code == 200:
        todo = todos.json()
        user = users.json()

        comp_tasks = [item for item in todo if item["completed"]]
        print("Employee {} is done with tasks ({}/{})".format(user['name'], len(todo), len(comp_tasks)))

        for item in comp_tasks:
            print(item['title'])
