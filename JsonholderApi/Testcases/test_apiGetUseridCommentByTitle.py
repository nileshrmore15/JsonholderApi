
import requests
import json
from Utilities.APIhelper import APITestCase
user_id = False


class TestAPIG(APITestCase):

    def test3_api_get_userid_by_title(self):
        global user_id
        try:
            # ------------------------------------------------
            # Send Get request with title parameter, Here parameter is
            # 'title': 'optio molestias id quia eum'
            # ------------------------------------------------
            title = 'optio molestias id quia eum'
            url = 'https://jsonplaceholder.typicode.com/posts'
            params = {'title': title}

            # ------------------------------------------------
            # send response with below Api Helper function present in Utilities folder
            # ------------------------------------------------
            response = self.send_request('GET', url, params=params)

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
                data = response.json()
                user_id = data[0]['userId']
                print(f"User ID for title '{title}': {user_id}")

                print("Response josn :", response.text)
                # ------------------------------------------------
                # open and read json file for expected json
                # ------------------------------------------------
                # file = open("D:\\pariplay\\JsonholderApi\\JsonFiles\\expected_user_by_title.json", 'r')
                file = open("JsonFiles/expected_user_by_title.json", 'r')
                expected_json = json.loads(file.read())
                print("Exp Json: ", expected_json)
                # ------------------------------------------------
                # Validate response json with expected json using below Api Helper function present in Utilities folder
                # ------------------------------------------------
                status = self.validate_json(response, expected_json)
            else:
                #print('Title not found.')
                print(f"Error in Response code: {response.status_code}")
        except Exception as e:
            print("Exception is = ", e)
        assert type(user_id) is int, "Test failed because the given Title not present"



    def test4_fetch_userdata_by_userid(self):
        global user_id
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        # ------------------------------------------------
        # send response with below Api Helper function present in Utilities folder
        # ------------------------------------------------
        response = self.send_request('GET', url)

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
            #print("Userdata Details :", response.text)
            user_data = json.loads(response.text)
            if user_data:
                print(f"User ID: {user_data['id']}")
                print(f"Name: {user_data['name']}")
                print(f"Email: {user_data['email']}")
                # Add more fields as needed
        else:
            print(f"Error in Response code: {response.status_code}")
        assert type(user_id) is int, "Test failed because userid is Null, can't show user data"


    def test5_fetch_comment_by_userid(self):
        global user_id
        url = f"https://jsonplaceholder.typicode.com/posts/{user_id}/comments"
        # ------------------------------------------------
        # send response with below Api Helper function present in Utilities folder
        # ------------------------------------------------
        response = self.send_request('GET', url)

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
            comments = response.json()

            if comments is not None:
                print(f"Comments for userid {user_id}:")
                for comment in comments:
                    print(f"Comment ID: {comment['id']}")
                    print(f"Name: {comment['name']}")
                    print(f"Email: {comment['email']}")
                    print(f"Body: {comment['body']}")
                    print("-" * 30)
            else:
                print(f"Error: User Data not present")
        else:
            print(f"Error in Response code: {response.status_code}")
        assert type(user_id) is int, "Test failed because userid is Null, can't show user data"

