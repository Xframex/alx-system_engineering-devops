#!/usr/bin/python3
"""gather data by api"""

if __name__ == "__main__":
    import requests
    from sys import argv

    api_url = "https://jsonplaceholder.typicode.com"
    user = requests.get('{}/users/{}'.format(api_url, argv[1])).json()
    todo = requests.get('{}/todos/?userId={}'.format(api_url, argv[1])).json()
    todo_done = requests.get('{}/todos/?userId={}&completed=true'
                             .format(api_url, argv[1])).json()
    user_name = user.get('name')

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, len(todo_done), len(todo)))

    for tasks in todo_done:
        print('\t {}'.format(tasks.get('title')))
