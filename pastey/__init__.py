from flask import Flask, request, send_file, render_template
import os
import base64
import re
import sys
from dotenv import load_dotenv

STORE_DIR = os.path.join(os.path.abspath(os.curdir), 'store')#TODO env var?
BASIC_AUTH_RE = re.compile(r'^Basic ([0-9A-Za-z+/=]+$)')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<paste_id>', methods=['GET'])
def upload(paste_id: str):
    if not check_auth(request.headers.get('Authorization')):
        return '', 401
    
    file_location = os.path.join(STORE_DIR, paste_id)

    

    if not os.path.exists(file_location):
        return '', 404

    return send_file(file_location)


@app.route('/<paste_id>', methods=['POST'])
def download(paste_id: str):
    if not check_auth(request.headers.get('Authorization')):
        return 'nope', 401

    file_location = os.path.join(STORE_DIR, paste_id)

    
    try:
        with open(file_location, 'wb') as f:
            f.write(request.get_data())
    except:
        return '', 400

    return '', 201

def check_auth(auth_header: str):
    encoded = BASIC_AUTH_RE.search(request.headers.get("Authorization")).group(1)
    login  = base64.b64decode(encoded).decode('utf-8').strip()
    return login == os.getenv('LOGIN')

if __name__ == '__main__':
    
    app.run()