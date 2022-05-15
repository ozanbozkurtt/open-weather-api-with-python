import requests

baseUrl = "https://api.openweathermap.org/data/2.5/weather"
apiKey ="789d4cc69bffe4a1ed27b54347cc3c62"

city = input("Please enter a city: ")
requestUrl = f"{baseUrl}?appid={apiKey}&q={city}" # kullanıcının girdiği şehir adının sorgulanacağı url
reponse = requests.get(requestUrl) # urldeki bilgiyi alıp response'a atıyoruz

if reponse.status_code == 200: # response 200 ise başarılı olmuştur
    jsonData = reponse.json() # jsonData'ya atıyoruz
    print(f"The weather in {city} is {jsonData['weather'][0]['description']}") # weather'in description'ını yazdırıyoruz
else:
    print("City not found")