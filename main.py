from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/joe")
def hello_joe():
    return "<h1>Yo Joe!</h1>"

@app.route('/sendList', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return post()
    else:
        return get()
    
def get():
    return "You Got."

def post(data: str):
    return data + " Thanks!"

