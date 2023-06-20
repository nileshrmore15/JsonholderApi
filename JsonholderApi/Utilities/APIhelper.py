import requests

class APITestCase:
    # def __init__(self, base_url):
    #     self.base_url = base_url

    def send_request(self, method, url, params=None, data=None):
        response = requests.request(method, url, params=params, json=data)
        return response

    def validate_response_code(self, response, expected_status_code):
        #assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}."
        if response.status_code == expected_status_code:
            return True
        else:
            return False

    def validate_json(self, response, expected_json):
        assert response.json() == expected_json, f"Expected JSON {expected_json}, but got {response.json()}."

    def validate_response_time(self, response):
        response_time = response.elapsed.total_seconds()
        assert response_time < 1500, "Response time is not less than 1500ms"

    def get_user_id_by_title(self, endpoint,  title):
        #url = 'https://jsonplaceholder.typicode.com/posts'
        url = self.base_url + endpoint
        params = {'title': title}

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]['userId']
            else:
                raise ValueError('Title not found.')
        else:
            raise ValueError('Error occurred while fetching data.')

