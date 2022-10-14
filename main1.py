from pprint import pprint

import requests

def superhero():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url)
    set = resp.json()
    iq = {}
    status = 0
    for i in range(len(set)):
        name = set[i].get('name')
        powerstats = set[i].get('powerstats')
        intelligence = powerstats.get('intelligence')
        if name == 'Hulk':
            iq.setdefault(intelligence, name)
        if name == 'Captain America':
            iq.setdefault(intelligence, name)
        if name == 'Thanos':
            iq.setdefault(intelligence, name)
    for stat in iq:
        if status < stat:
            status = stat
    print(f'Cамый умный из трех супергероев: {iq.get(status)}')
    
superhero()