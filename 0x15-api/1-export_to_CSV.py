#!/usr/bin/python3
"""Gather data for another purpose"""

if __name__ == "__main__":
    import requests
    from sys import argv

    file_path = argv[1] + "_data.csv"
    api_url = "https://jsonplaceholder.typicode.com"
    user = requests.get('{}/users/{}'.format(api_url, argv[1])).json()
    posts = requests.get('{}/posts/?userId={}'.format(api_url, argv[1])).json()
    cm = requests.get('{}/comments/?postId={}'.format(api_url, argv[1])).json()

    user_name = user.get('username')
    with open(file_path, 'a') as f:
        for post in posts:
            f.write(
                "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                    argv[1],
                    user_name,
                    post.get('title'),
                    post.get('body')
                )
            )

        for comment in comments:
            f.write(
                "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                    argv[1],
                    user_name,
                    comment.get('email'),
                    comment.get('body')
                )
            )
