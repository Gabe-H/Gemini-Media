import json

with open('videos.json') as f:
    data = json.load(f)

myID = input('Spotify URI: ')
myURL = input('URL: ')
myCSS = input('CSS (leave blank if none): ')

myID = myID.split(':')
myID = myID[len(myID)-1]

data['ids'].append({
    "id": myID,
    "url": myURL,
    "css": myCSS
})

result = json.dumps(data, indent=4)

with open("videos.json", "w") as data_file:
    json.dump(data, data_file, indent=4)

print(result)