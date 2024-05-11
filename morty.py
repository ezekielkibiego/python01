import requests
import csv
import os

def character_data(api_url, csv_filename):
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            
            characters = data['results']
            
            fieldnames = ['Name', 'Status', 'Species', 'Gender']
            
            file_exists = os.path.isfile(csv_filename)
            
            with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                if not file_exists:
                    writer.writeheader()
                    
                for character in characters:
                    writer.writerow({
                        'Name': character['name'],
                        'Status': character['status'],
                        'Species': character['species'],
                        'Gender': character['gender']
                    })
                    
            print(f"Character data has been saved to {csv_filename}")
            
        else: 
            print(f"Error: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        
api_url = 'https://rickandmortyapi.com/api/character'
csv_filename = 'morty.csv'

character_data(api_url, csv_filename)