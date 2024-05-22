#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    # Construct URLs for todos and users
    user_id = sys.argv[1]
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    url_users = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Fetch data from API
    todos = requests.get(url_todos)
    users = requests.get(url_users)

    # Check if requests are successful
    if todos.status_code == 200 and users.status_code == 200:
        # Parse JSON responses
        todo = todos.json()
        user = users.json()

        # Filter completed tasks
        comp_tasks = [item for item in todo if item["completed"]]

        # Print information
        print(
            f"Employee {user.get('name')} is done with tasks "
            f"({len(comp_tasks)}/{len(todo)}):"
        )

        # Print titles of completed tasks
        for item in comp_tasks:
            print(f"\t {item['title']}")

