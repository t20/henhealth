from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page!"

@app.route('/hello')
def hello_world():
    return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return "User page"

@app.route('/')
def login():
    """docstring for login"""
    pass


@app.route('/')
def regsiter():
    """docstring for regsiter"""
    pass


if __name__ == '__main__':
    app.debug = True
    app.run()