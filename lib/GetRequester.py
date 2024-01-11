import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        try:
            response_text = response_body.decode('utf-8') 
            return json.loads(response_text)  
        except ValueError:
            return None