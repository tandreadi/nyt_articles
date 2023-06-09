import requests
import ndjson
import os

class NYTimesAPI:

    def __init__(self):
        self.parameters = {
            "limit": "100",  # 100 articles
            "api-key": os.environ.get('API_KEY')
        }
        self.api = 'https://api.nytimes.com/svc/news/v3/content/all/all.json'
        self.get_articles_from_nyt()

    def get_articles_from_nyt(self):
        '''Get data from Times Newswire API'''

        requestHeaders = {
            "Accept": "application/json"
        }
        response = requests.get(self.api, params=self.parameters, headers=requestHeaders)
        json_object = response.json()
        results = json_object['results']
        ndjson_data = ndjson.dumps(results)

        return ndjson_data
