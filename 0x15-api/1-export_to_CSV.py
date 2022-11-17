#!/usr/bin/python3
"""
    exporting the data requested to CSV
"""
if __name__ == "__main__":
    """converts json to python dictionary
    export to csv file
    Format:
        "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    """
    import csv
    import io
    import json
    import requests
    import sys

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # User detail
    user_det_url = url + "users?id=" + id
    user_detail = requests.get(user_det_url)
    usr = json.loads(user_detail.text)

    # request all todo list of the ID
    todo_det_url = url + "todos?userId=" + id
    todo_detail_total = requests.get(todo_det_url)
    todo_user = json.loads(todo_detail_total.text)

    # create dictionary with the right format and
    # store each dictionaary to a list
    fieldnames = [
        "USER_ID", "USERNAME",
        "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ]
    user_info = []
    for no in range(0, len(todo_user)):
        info = {}
        info["USER_ID"] = todo_user[no]["userId"]
        info["USERNAME"] = usr[0]["username"]
        info["TASK_COMPLETED_STATUS"] = todo_user[no]["completed"]
        info["TASK_TITLE"] = todo_user[no]["title"]
        user_info.append(info)

    # writing newly created py dictionary into a csv file
    with open('USER_ID.csv', 'wt') as csvfile:
        writer = csv.DictWriter(csvfile, quoting=csv.QUOTE_ALL, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerows(user_info)
