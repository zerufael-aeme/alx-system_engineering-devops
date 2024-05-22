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

        # Specify the path to save the CSV file
        csv_file = "USER_ID.csv"

        # Specify the order of columns
        fieldnames = ["userId", "username", "completed", "title"]

        # Parse JSON responses
        todo = todos.json()
        user = users.json()

        # Filter completed tasks
        comp_tasks = [item for item in todo if item["completed"]]

        # Write JSON data to CSV file
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # Write data from first JSON file
            for row1 in comp_tasks:
                row = {key: row1.get(key, "") for key in fieldnames}
                writer.writerow(row)

            # Write data from second JSON file
            for row2 in user:
                row = {key: row2.get(key, "") for key in fieldnames}
                writer.writerow(row)

