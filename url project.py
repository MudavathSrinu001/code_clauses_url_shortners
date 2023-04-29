from flask import Flask, redirect, request
import string
import random

app = Flask(__name__)

url_map = {}

def generate_short_url():
    """Generate a random string of 6 characters for use as a short URL"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(6))

@app.route('/')
def home():
    return 'Welcome to the URL shortener!'

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = generate_short_url()
    url_map[short_url] = long_url
    return short_url

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_map.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return 'Sorry, this short URL does not exist.'

if __name__ == '__main__':
    app.run()