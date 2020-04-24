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


@app.route('/arhives',)
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


@app.route('/documents', methods=['POST'])
def getdocument():

    naziv_arhive = request.get_json()['naziv']
    lista_dokumenta = mongo.db.Lista_arhiva
    dokumenti = {}
    i = 0

    for x in lista_dokumenta.find():
        if(naziv_arhive == x['naziv']):
            for y in x['documents']:    
                # staviti if da se nađe id korisnika
                dokumenti[i] = {
                    'id' : str(y['id']),
                    'tekst' : y['tekst']
                }
                i += 1

    return jsonify(dokumenti)


@app.route('/send_document', methods=['POST'])
def sendDocument():
    docfile = request.get_json()['docfile']
    docname = request.get_json()['docname']
    mongo.db.test_loadImage.insert({
        'docfile' : docfile,
        'docname' : docname
    })



if __name__ == "__main__":
    app.run(port=5000, debug=True)
