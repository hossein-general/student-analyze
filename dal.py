# This module will be used to be a bridge between the data base and the applications internal storage manager
# TODO add the data base and connect it to this module
# TODO creating a function for updating applications data manager object
# TODO creating functions to directly get data from database

from os import system
import requests

system("cls")


def get_posts():
    # Define the API endpoint URL
    url = "http://127.0.0.1:8000/all_person"

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print("Error:", response.status_code)
            return None

    except requests.exceptions.RequestException as e:

        # Handle any network-related errors or exceptions
        print("Error:", e)
        return None


def main():
    posts = get_posts()
    if posts:
        print(posts)
    else:
        print("Failed to fetch posts from API.")


if __name__ == "__main__":
    main()





