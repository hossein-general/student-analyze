# This module will be used to be a bridge between the data base and the applications internal storage manager
# TODO add the data base and connect it to this module
# TODO creating a function for updating applications data manager object
# TODO creating functions to directly get data from database

from student_analyze import (
    # person base
    Person,
    Gender,
    # global attributes
    EducationState,
    EducationGrade,
    EducationGroup,
    Lesson,
    # school base
    School,
    # classroom and classgroup are accessable through the School class
)


# for dal direct access
import ipdb

# # importin json to work with it
# import json
# json.loads()      # convert to python
# json.dumps()      # convert to json



from os import system
import requests

# region test
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

# endregion

# ------------------------------------------------------------------------
main_url = 'http://127.0.0.1:8000'

# region GET
# This get handles any model type, also handels getting all or by id
def get_model(the_model:str, the_id:int=None):
    # creating the url
    if the_id is None:
        api_url = main_url + '/get/' + the_model 
    else:
        api_url = main_url + '/modify/' + the_model + '/' + str(the_id)

    response = requests.get(api_url)
    print(response.json())
    # return response.json  # to be used within the program

# endregion


# region POST
def post_model(the_model:str, model_instance: any):
    # creating the url
    api_url = main_url + '/add/' + the_model + '/'

    model_item = model_instance.get_dict() # as right now its only defined in GlobalAttributes classes
    response = requests.post(api_url, json=model_item)
    print(response.json)

# endregion

# region DELETE
def delete_model(the_model:str, the_id:int):
    # creating the url
    api_url = main_url + '/modify/' + the_model + '/' + str(the_id)

    response = requests.delete(api_url)
    print(response)

# endregion

# region PUT
def update_model(the_model:str, model_instance:any, the_id:int):
    # creating the url
    api_url = main_url + '/modify/' + the_model + '/' + str(the_id)

    model_item = model_instance.get_dict() # as right now its only defined in GlobalAttributes classes
    response = requests.put(api_url, json=model_item)
    print(response.json())

# endregion


# region fetch data
# fetch data
def fetch_data(data):
    # this function queries the whole data base to retrieve all data within it and store them locally within the client app

    # region ES
    es_list = get_model('es')
    for item in es_list:
        data.es.item[item['id']] = EducationState(state_name=item['name'])


    
# endregion



















def run(data):
    # entered dal module
    print(
        '-----------------------------------------',
        'get_model(the_model:str, the_id:int=None)',
        'post_model(the_model:str, model_instance: any)',
        'delete_model(the_model:str, the_id:int = None)',
        'update(the_model:str, model_instance:any, the_id:int)',
        'update_model(the_model:str, model_instance:any, the_id:int)',
        '-----------------------------------------',
        sep='\n',
    )
    ipdb.set_trace()
    delete_model('es', 1)
    get_model('es', 1)


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



