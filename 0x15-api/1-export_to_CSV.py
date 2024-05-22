#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
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

        # Specify the path to save the CSV file
        csv_file = "USER_ID.csv"

        # Define username
        username = user.get("username")

        # Write JSON data to CSV file
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            [writer.writerow(
                [user_id, username, t.get("completed"), t.get("title")]
            ) for t in todo]

