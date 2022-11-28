import json, requests 

antwoord = requests.get("https://api.covid19api.com/world/total").text
antwoord_dict = json.loads(antwoord)#form antwoord(string in JSON-formaat) om naar dictionary tegaan
print(antwoord_dict)
