from flask import Flask, request, redirect, render_template
import hashlib

app = Flask(__name__)

# In-memory storage for URLs
url_map = {}

# Helper function to create a short key for a URL
def shorten_url(original_url):
    return hashlib.md5(original_url.encode()).hexdigest()[:6]

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', short_url=request.args.get('short_url'))

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_key = shorten_url(original_url)
    url_map[short_key] = original_url
    short_url = request.host_url + short_key
    return redirect('/?short_url=' + short_url)

@app.route('/<short_key>')
def redirect_to_url(short_key):
    original_url = url_map.get(short_key)
    if original_url:
        return redirect(original_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run()
