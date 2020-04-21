from flask import Flask, jsonify , request, json # vraća json response
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Kristijan_10:Messi123@digitality-4hkuh.mongodb.net/Digitality?retryWrites=true&w=majority'


mongo = PyMongo(app)
bcrypt = Bcrypt(app)
CORS(app)

@app.route('/')
def index():
    return "Hello World"

@app.route('/register', methods=['POST'])
def registracija():
    
    ime = request.get_json()['ime']
    prezime = request.get_json()['prezime']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password'])

    mongo.db.Korisnik.insert({
        'ime' : ime,
        'prezime' : prezime,
        'email' : email,
        'password' : password
    })

    return "Poslano"


@app.route('/login', methods=['POST'])
def login():

    email = request.get_json()['email']
    password = request.get_json()['password']
    korisnici = mongo.db.Korisnik
    access = ""

    for x in korisnici.find():
        if (x['email'] == email):
            if bcrypt.check_password_hash(x['password'],password):
                access = {
                    'ID' : str(x['_id']),
                    'ime' : x['ime'],
                    'prezime' : x['prezime'],
                    'email' : x['email'],
                }     
            else:
                access = False

    return jsonify(access)


@app.route('/arhive',)
def getarhive():
    lista_arhiva = mongo.db.Lista_arhiva
    arhive = {}
    i = 0
    
    for x in lista_arhiva.find():
        arhive[i] = {
            'ID' : str(x['_id']),
            'naziv' : x['naziv']
        }
        i += 1

    return jsonify(arhive)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
