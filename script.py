# Import libraries
import json
import csv
import requests


# open method for csv file to read
with open('exp_tournesol_upcoming_onsales_202210141028.csv', 'r') as  f:
    
    # read csv file
    reader = csv.reader(f)

    # create empty dictionary for storing data
    data = {"results":[]}

    # go to next row in csv
    next(reader)

    # start looping reader object
    for row in reader:
        data["results"].append({"user_id": row[1]})


# create empty dictonary for processed data
processed_data = []

# loop through object
for i, d in enumerate(data["results"]):

    # get user id
    user_id = data['results'][i]['user_id']

    # remove dupes
    if user_id not in processed_data:
        processed_data.append(user_id)


working_users = []

for i, id in enumerate(processed_data):

    uid = processed_data[i]

    

    api_request = 'https://api.dice.fm/linked-data/upcoming-onsales?uid=' + uid + '&partner=1&limit=7'
    response =  requests.get(api_request)
    status = response.status_code

    # print(f'Api Request: {api_request}')
    # print(f'status: {status}')
    # print(f'response: {response.text}')

    if status != 200 and response != '[]':
        working_users.append(id)
        
        print('working user below')
        print(f'User id: {uid}')
        print(f'response: {response.text}')
        print(f'status: {status}')
        print(f'response: {response.text}')
    else:
        print('user IS NOT WORKING below')
        print(f'User id: {uid}')
        print(f'response: {response.text}')
        print(f'status: {status}')
        print(f'response: {response.text}')

print(working_users)


# create new file to write
# with open('rotas.json', 'w') as f:
     
    #  dump data in the file and indent by 4
    #  json.dump(data,f,indent=4)