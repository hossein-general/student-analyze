# This module will be used to be a bridge between the data base and the applications internal storage manager
# TODO add the data base and connect it to this module
# TODO creating a function for updating applications data manager object
# TODO creating functions to directly get data from database


# for dal direct access
import ipdb

# # importin json to work with it
# import json
# json.loads()      # convert to python
# json.dumps()      # convert to json



from os import system
import requests


def get_posts():
    # Define the API endpoint URL
    url = "http://127.0.0.1:8000/show/es"

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


# ------------------------------------------------------------------------
main_url = 'http://127.0.0.1:8000'

# This get handles any model type, also handels getting all or by id
def get_model(the_model:str, the_id:int=None):
    # creating the url
    api_url = main_url + '/get/' + the_model
    if the_id is not None:
        api_url = api_url + '/' + str(the_id)

    response = requests.get(api_url)
    print(response.json())
    # return response.json  # to be used within the program



def post_model(the_model:str, model_instance: any):
    # creating the url
    api_url = main_url + '/add/' + the_model + '/'

    model_item = model_instance.get_dict() # as right now its only defined in GlobalAttributes classes
    response = requests.post(api_url, json=model_item)
    print(response.json)
    # return response.json




    
def run(data):
    # entered dal module
    ipdb.set_trace()





def main():
    posts = get_posts()
    if posts:
        print(posts)
        print('-----------------------------')

        for item in posts:
            print(item)
        
    else:
        print("Failed to fetch posts from API.")


if __name__ == "__main__":
    system("cls")
    main()





