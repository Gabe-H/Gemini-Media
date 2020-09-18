import json

with open('videos.json') as f:
    data = json.load(f)

myURI = input('Spotify URI: ')
print(myURI)
myURL = input('URL: ')
myCSS = input('CSS (leave blank if none): ')


data['ids'].append({
    "id": myURI,
    "url": myURL,
    "css": myCSS
})

result = json.dumps(data, indent=4)

with open("videos.json", "w") as data_file:
    json.dump(data, data_file, indent=4)

print(result)