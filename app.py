from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Simple Web App</h1><p>This is the home page.</p>"

@app.route('/about')
def about():
    return "<h1>About</h1><p>This is the about page.</p>"

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8000)

