from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    """docstring for login"""
    return render_template('login.html')


@app.route('/register')
def regsiter():
    """docstring for regsiter"""
    return render_template('register.html')


@app.route('/forgot')
def forgot():
    """docstring"""
    return render_template('forgot.html')


@app.route('/account')
def account():
    """docstring"""
    return render_template('account.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
