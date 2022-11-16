#!/usr/bin/python3
""" using a REST API for a given employee ID
    returns information about his/her TODO list progress
    accept an integer as a parameter (employee ID)

"""

if __name__ == "__main__":
    """ concatinating url with query strings
        request the page
        json.loads to convert json to python dictionary
    """
    import json
    import requests
    import sys

    
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    
    #User detail
    user_det_url = url + "users?id=" + id
    user_detail = requests.get(user_det_url)
    usr = json.loads(user_detail.text)
    
    # request all todo list of the ID
    todo_det_url = url + "todos?userId=" + id
    todo_detail_total = requests.get(todo_det_url)
    todo_user2 = json.loads(todo_detail_total.text)
    
    # completed todo task
    todo_completed_url = todo_det_url + "&completed=true"
    todo_completed = requests.get(todo_completed_url)
    todo_completed = json.loads(todo_completed.text)

    print("Employee {} is done with tasks({}/{}):".format(usr[0]["name"], len(todo_completed), len(todo_user2)))
    # loop through to display each task title
    for task in todo_completed:
        print("\t {}".format(task["title"]))