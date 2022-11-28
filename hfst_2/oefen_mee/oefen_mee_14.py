import requests#importeer request
antwoord = requests.get("https://api.covid19api.com/world/total").text #haal text van website af, zet in antwoord
print(antwoord("TotalDeaths"))#print antwoord 