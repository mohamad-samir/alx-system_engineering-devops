#!/usr/bin/python3
""" Rest API script that gathers data from an API. """
import requests
import sys

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()
        
        completed_tasks = [task for task in todos_data if task['completed']]
        
        print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{len(todos_data)}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

