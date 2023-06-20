
import requests
import json
from Utilities.APIhelper import APITestCase
user_id = False


class TestAPICU(APITestCase):

    # We use 'POST' method to create Resource
    def test1_api_create_user(self):
        url = 'https://jsonplaceholder.typicode.com/users'

        file = open("JsonFiles/create_user.json", 'r')
        data_body = json.loads(file.read())
        print("Create user: ", data_body)

        # ------------------------------------------------
        # send response with below Api Helper function present in Utilities folder
        # ------------------------------------------------
        response = self.send_request('POST', url, data_body)

        # ------------------------------------------------
        # check performance and response time with below Api Helper function present in Utilities folder
        # ------------------------------------------------
        self.validate_response_time(response)

        # ------------------------------------------------
        # Validate response with below Api Helper function present in Utilities folder
        # ------------------------------------------------
        status = self.validate_response_code(response, 201)
        print("Status : ", status)
        if status:
            print('User created successfully!')
            print('User ID:', response.json().get('id'))
            print('User All Details :', response.text)
        else:
            print(f"Error in Response code: {response.status_code}")
        assert status is True, "Test failed because User not created "


    # We use 'PUT' method to update Resource
    def test2_api_update_user(self):
        u_id = 2
        url = f"https://jsonplaceholder.typicode.com/users/{u_id}"

        data_body = {
            "name": "Nilesh R. More",
            "username": "nileshrmore",
            "email": "newnilesh@gmail.com"
        }
        # ------------------------------------------------
        # send response with below Api Helper function present in Utilities folder
        # ------------------------------------------------
        response = self.send_request('PUT', url, data_body)
        print("Response json: ", response.text)

        # ------------------------------------------------
        # check performance and response time with below Api Helper function present in Utilities folder
        # ------------------------------------------------
        self.validate_response_time(response)

        # ------------------------------------------------
        # Validate response with below Api Helper function present in Utilities folder
        # ------------------------------------------------
        status = self.validate_response_code(response, 200)
        print("Status : ", status)

        if status:
            print("User updated successfully.")
            response1 = self.send_request('GET', url)
            updated_user = response1.json()
            print("Updated User Details:")
            print("Name:", updated_user["name"])
            print("Username:", updated_user["username"])
            print("Email:", updated_user["email"])
        else:
            print("User update failed.")
            print(f"Error in Response code: {response.status_code}")
        assert status is True, "Test failed because User data not update "
