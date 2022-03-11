import csv
import requests

with open('./movies_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        rating = float(row[1])
        year = int(name[name.find("(")+1:name.find(")")])
        name = name[name.find(".")+1:name.find("(")]
        
        url = "http://127.0.0.1:8000/movies/"
        movie = {
            "name": name,
            "rating": rating,
            "year": year
        }
        x = requests.post(url, data = movie)
        print(x)