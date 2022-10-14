from pprint import pprint

import requests

def get_info():
    url = "https://api.stackexchange.com/2.3/questions?fromdate=1665532800&todate=1665705600&order=desc&sort=activity&tagged=python&site=stackoverflow"
    response = requests.get(url)
    set = response.json()
    pprint(set)
get_info()