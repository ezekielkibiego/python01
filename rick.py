import requests

api_url = 'https://rickandmortyapi.com/api/character'

def display_character_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            
            for character in data['results']:
                print(f"Name: {character['name']}")
                print(f"Status: {character['status']}")
                print(f"Location: {character['location']['name']}")
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        
display_character_data(api_url)