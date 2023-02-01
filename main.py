from flask_cors import CORS, cross_origin
from flask import Flask, request
from services.hill_cipher import HillCipher
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/hill-cipher/encrypt', methods=['GET'])
@cross_origin()
def encrypt_hill_cipher():
    key = request.args['key']
    mat = json.loads(key)
    
    hc = HillCipher(mat)
    
    return hc.encrypt(request.args['msg'])

@app.route('/hill-cipher/decrypt', methods=['GET'])
@cross_origin()
def decrypt_hill_cipher():
    key = request.args['key']
    mat = json.loads(key)
    
    hc = HillCipher(mat)
    return hc.decrypt(request.args['msg'])

if __name__ == '__main__':
    app.run()
