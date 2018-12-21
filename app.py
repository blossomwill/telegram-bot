import os
import requests
from flask import Flask, request
app = Flask(__name__)

token = os.getenv('TELEGRAM_BOT_TOKEN')

@app.route("/") 
def hello():
    return "Hello World!"
    
@app.route(f"/{token}", methods = ['POST']) #c9 Editor의 python이 낮은버전이라 에러뜸
def telegram():
    
    # 1.구조 확인하기
    from_telegram = request.get_json() #=> dict
    print(from_telegram)
    
    # 2. 그대로 돌려보내기(메아리)
    # ['message'] #=> 키가 없으면, 에러 발생!
    # .get('message') #=> 키가 없으면, None
    if from_telegram.get('message') is not None:
        chat_id = from_telegram['message']['from']['id']
        text = from_telegram['message']['text']
        # api.telegram.org => api.hphk.io/telegram
        requests.get(f"https://api.hphk.io/bot{token}/sendMessage?chat_id={chat_id}&text={text}")
    
    return '', 200
    

# FLASK_APP=app.py flask run --hosh=$IP --port=$PORT 포함시킨다.
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
    