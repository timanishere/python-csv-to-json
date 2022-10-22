# Import libraries
import json
import csv

# Create input field
csv_name = input('Enter the name of .csv file: ')

def convert_csv_to_json(csv_name):
    # open method for csv file to read
    with open(csv_name, 'r') as  f:
    
        # read csv file
        reader = csv.reader(f)
    
        # create empty dictionary for storing data
        data = {"results":[]}
    
        # go to second row in csv
        next(reader)
    
        # start looping reader object
        for row in reader:
            data["results"].append({"rota_id": row[1],"date": row[2],"shift_id": row[3]})
        
        print(data)
        

    # create new file to write so that results can be saved in a file
    with open('rotas.json', 'w') as f:
    
    # dump data in the file and indent by 4
        json.dump(data,f,indent=4)


    print("conversion completed")



convert_csv_to_json(csv_name)