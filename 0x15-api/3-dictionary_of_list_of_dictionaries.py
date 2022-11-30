#!/usr/bin/python3
"""
    exporting the todo list data of a all employees ID to JSON format
"""
if __name__ == "__main__":
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump({u.get('id'): [{
            "task": t.get("title"),
            "completed": u.get("completed"),
            "username": username
        } for t in response.get(url + "todos",
                                params={"userId": u.get("id")}).json()]},
                                jsonfile)
