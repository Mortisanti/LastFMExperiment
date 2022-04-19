import requests
import json
import my_secrets

API_KEY = my_secrets.API_KEY
artist = 'Cannibal Corpse'
album = 'Kill'
method = 'album.getinfo'
return_format = 'json'
params = {
    'method': method,
    'api_key': API_KEY,
    'artist': artist,
    'album': album,
    'format': return_format
}
URL = f'http://ws.audioscrobbler.com/2.0/?'

def main():
    r = requests.get(URL, params=params)
    print(r.url)
    with open('result.json', 'w') as f:
        f.write(r.text)


if __name__ == '__main__':
    main()