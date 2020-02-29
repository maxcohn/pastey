from flask import Flask, request
import os


STORE_DIR = os.path.join(os.path.abspath(os.curdir), 'store')

app = Flask(__name__)


@app.route('/')
def home():
    import sys
    print(STORE_DIR, file=sys.stderr)
    return 'asdasdasd'

@app.route('/<paste_id>', methods=['GET'])
def upload(paste_id: str):
    

    return 'UPLOAD'

@app.route('/<paste_id>', methods=['POST'])
def download(paste_id: str):
    return 'DOWNLOAD'

if __name__ == '__main__':
    
    app.run()