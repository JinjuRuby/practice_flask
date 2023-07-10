from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/hello") # 127.0.0.1
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/") # 127.0.0.1
def index():
    return send_from_directory('html', "index.html") # 127.0.0.1/html/index.html 메인 페이지가 뜬다

@app.route('/<path:name>')  #127.0.0.1/... 이후 모든 내용을 name으로 받는다
def start(name):
    return send_from_directory('html', name) # 127.0.0.1/html/... 전체 테마 내용이 홈페이지로 작동될 수 있다