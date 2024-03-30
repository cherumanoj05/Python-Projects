import creds
import requests

headers = {
    'Accept': 'application/json',
    "Authorization": "Bearer "+creds.token
}

# Function to search player with id as parameter
def search_player(id):
    # URL to request player
    url = 'https://api.clashofclans.com/v1/players/%23'+id

    # Getting response
    response = requests.get(url,headers = headers)

    # Checking if response is valid if not display Player not found
    if(response.status_code==200):
        
        # Storing the response JSON inside details variable
        details = response.json()

        # manipulating the JSON and storing inside variables
        name = details['name']
        townHallLevel = details['townHallLevel']
        expLevel = details['expLevel']
        trophies = details['trophies']
        bestTrophies = details['bestTrophies']
        warStars = details['warStars']
        clan = details['clan']['name']
        role = details['role']
        league = details['league']['name']

        # printing the values
        print(f'''
              ###Player Details###\n\nPlayer Name: {name} \nTownhall Level: {townHallLevel} \nPlayer Experience: {expLevel} \nPlayer trophies: {trophies} \nHighest trophy: {bestTrophies} \nTotal war starts: {warStars} \nClan: {clan} \nRole: {role} \nCurrent League: {league}
              ''')
        

    # IF response is wrong, display player not found
    else:
        print(f"Player with tag {id} not found.")
        print(response.status_code)

    return ""

id = input("Enter the player id:")
print(search_player(id)) 