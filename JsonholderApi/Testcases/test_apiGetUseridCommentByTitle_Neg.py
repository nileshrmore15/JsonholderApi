
import requests
import json
from Utilities.APIhelper import APITestCase
us_id = False


class TestAPIGN(APITestCase):

    def test6_api_get_userid_by_title_Neg(self):
        global us_id
        status_code = True
        try:
            # ------------------------------------------------
            # Send Get request with title parameter, Here parameter is
            # 'title': 'optio molestias id quia eum'
            # ------------------------------------------------
            Invalid_title = 'optio nilesh molestias id quia eum'
            url = 'https://jsonplaceholder.typicode.com/posts'
            params = {'title': Invalid_title}

            # ------------------------------------------------
            # send response with below Api Helper function present in Utilities folder
            # ------------------------------------------------
            response = self.send_request('GET', url, params=params)

            # ------------------------------------------------
            # check performance and response time with below Api Helper function present in Utilities folder
            # ------------------------------------------------
            self.validate_response_time(response)

            #print(response.status_code)

            # ------------------------------------------------
            # Validate response with below Api Helper function present in Utilities folder
            # ------------------------------------------------
            status = self.validate_response_code(response, 200)
            status_code = status
            #print("Status : ", status)

            if status:
                data = response.json()
                us_id = data[0]['userId']
            else:
                print('Test Passed: Title not found as expected.')
                print(f"Response code: {response.status_code}")
        except Exception as e:
            print("Exception is = ", e)
        assert type(us_id) is not int, "Test failed because the given Title present"



    def test7_fetch_userdata_by_userid_Neg(self):
        global us_id
        status = True
        try:
            url = f"https://jsonplaceholder.typicode.com/users/{us_id}"
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

            if status == True:
                print("Test case Failed")
            else:
                print('Test case Passed: Userid not found as expected.')
                print(f"Response code: {response.status_code}")
        except Exception as e:
            print("Exception is = ", e)
        assert type(us_id) is not int, "Test failed because userid is present & show user data"




    def test8_fetch_comment_by_userid_Neg(self):
        global us_id
        status = True
        try:
            url = f"https://jsonplaceholder.typicode.com/posts/{us_id}/comments"
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
                    print(f"Comments for userid {us_id}:")
                    comment = comments[0]["id"]
                    print(comment)
                else:
                    print(f"Error: User Data not present")
            else:
                print('Test Passed: Userid not found as expected.')
                print(f"Response code: {response.status_code}")

        except Exception as e:
            print("Exception is = ", e)
        assert type(us_id) is not int, "Test failed because Test failed because Comments is present"


