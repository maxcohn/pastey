from flask import Flask, request, send_file
import os


STORE_DIR = os.path.join(os.path.abspath(os.curdir), 'store')

app = Flask(__name__)


@app.route('/')
def home():
    return 'asdasdasd'

@app.route('/<paste_id>', methods=['GET'])
def upload(paste_id: str):
    file_location = os.path.join(STORE_DIR, paste_id)

    if not os.path.exists(file_location):
        return '', 404

    return send_file(file_location)


@app.route('/<paste_id>', methods=['POST'])
def download(paste_id: str):

    file_location = os.path.join(STORE_DIR, paste_id)
    try:
        with open(file_location, 'wb') as f:
            f.write(request.get_data())
    except:
        return '', 400

    return '', 201

if __name__ == '__main__':
    
    app.run()