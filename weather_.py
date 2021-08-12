import requests
import json
import numpy as np

city = 'Osan'
apikey = '1399a83ed7d21513ede00876757068b5'
lang = 'kr'

api = f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&appid={apikey}'

result = requests.get(api)
data = json.loads(result.text)
print(data["name"],"의 날씨입니다.")
print("날씨는 " , data['weather'][0]["description"],'입니다')
print('현재 온도는 ', str(int(data['main']['temp'])/10),"입니다.")
print('체감 온도는 ', str(int(data['main']['feels_like']/10)),"입니다.")