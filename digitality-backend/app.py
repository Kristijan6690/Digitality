from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from flask import Flask, jsonify , request, json
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson import ObjectId

import datetime
import jwt
import os

import scan_engine
import default_data as dflt
import mongodb as mongodb

mongodb.index_email()

app = Flask(__name__)
#app.config['MONGO_URI'] = 'mongodb+srv://Kristijan_10:Messi123@digitality-4hkuh.mongodb.net/digitality_production?retryWrites=true&w=majority'
app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@cluster0-5uwqu.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
CORS(app)

@app.route('/')
def index():
    return "Hello World"

@app.route('/register', methods=['POST'])
def register():
    doc = request.get_json()
    
    user = {
        'name': doc['name'],
        'surname': doc['surname'],
        'email': doc['email'],
        'password': bcrypt.generate_password_hash(doc['password'], 8),
        'personal_archive_id': None,
        'archive_ids': None,        
        'alias_list': []
    }
    
    res = mongodb.register_user(user)
    
    return res


@app.route('/login', methods=['POST'])
def login():
    email = request.get_json()['email']
    password = request.get_json()['password']
    
    user = mongodb.get_user(email)
    
    if (user and user['password']) and (bcrypt.check_password_hash(user['password'], password)):
        del user['password']
        del user['_id']
        
        user['exp'] = datetime.datetime.now() + datetime.timedelta(days=7)
        user['token'] = jwt.encode(user, os.getenv("JWT_SECRET"), algorithm='HS256').decode("utf-8")
    
    return jsonify(user)


@app.route('/GetArchives', methods=['POST'])
def getarhive():
    user = mongodb.get_user(request.get_json()['email'])
    
    if not user:
        return False
    
    personal_archive_id = user['personal_archive_id']
    archive = mongodb.get_archive(personal_archive_id)
    
    if not archive:
        return False

    subArchives = archive['subarchive_names']
    
    for sub_arc in subArchives:
        sub_arc['subarchive_id'] = str(sub_arc['subarchive_id'])

    return jsonify(subArchives)


# još da vraća alliase kad budu
@app.route('/documents', methods=['POST'])
def getdocument():

    subArchive_name = request.get_json()['subArchive_name'].lower()
    personal_archive_id = request.get_json()['personal_archive_id']
    documents = []

    for x in mongo.db.archives.find():
        if(str(x['_id']) == personal_archive_id):
            if (len(x[subArchive_name]) == 0):
                documents = False
                return jsonify(documents)

            else:
                for atributes in x[subArchive_name]:
                        documents.append(atributes)
            #str(OBJECTID)
            for counter,doc in enumerate(documents):
                if(documents[counter]['id_dokumenta']):
                    doc = documents[counter]['id_dokumenta']
                    documents[counter]['id_dokumenta'] = str(doc)
                    
            return jsonify(documents) 

        else:
            documents = False
            return jsonify(documents)


# RAZRADA JOS TESAK
@app.route('/document', methods=['POST'])
def sendDocument():

    doc_url = request.get_json()['doc_url']
    temp = scan_engine.photo_to_dict(doc_url)

    return "Poslano u bazu"


@app.route('/search/lista_arhiva', methods=['POST'])
def searchArchives():

    searchTerm = str(request.get_json()['searchTerm'])
    searchTerm = searchTerm.lower()
    rezultat = {}
    i = 0

    if(searchTerm):

        cursor = mongo.db.Lista_arhiva.find({'naziv':{'$regex':'^(%s)' % searchTerm}})
        result = list(cursor)
        
        for x in result:
            rezultat[i] = {
                'ID' : str(x['_id']),
                'naziv' : x['naziv'].capitalize()
            }
            i += 1
            
        return jsonify(rezultat)

    else:
        for x in mongo.db.Lista_arhiva.find():
            rezultat[i] = {
                'ID' : str(x['_id']),
                'naziv' : x['naziv'].capitalize()
            }
            i += 1  
            
        return jsonify(rezultat)  


@app.route('/archives/createSubarchive', methods=['POST'])
def createSubarchive():
    archive_name = request.get_json()['archive_name'].lower()
    personal_archive_id = ObjectId(request.get_json()['personal_archive_id'])
    subarchive_id = ObjectId()
    mongo.db.archives.update({'_id': personal_archive_id},{'$push':{
        'subarchive_names': {
            'subarchive_id': subarchive_id,
            'name': archive_name,
            'examination_date': ''
        }}, '$set':{ archive_name: [] }})
        
    return "Dodano"


@app.route('/archive/deleteSubarchive', methods=['POST'])
def deleteSubarchive():
    personal_archive_id = ObjectId(request.get_json()['personal_archive_id'])
    subarchive_id = ObjectId(request.get_json()['subarchive_id'])
    subarchive_name = request.get_json()['subarchive_name'].lower()
    mongo.db.archives.update({'_id': personal_archive_id},{'$pull':{'subarchive_names':{'subarchive_id':subarchive_id}}})
    mongo.db.archives.update({'$unset':{ subarchive_name: []}})
    

    return "Obrisano"


@app.route('/archive/UpdateExaminationDate',methods=['POST'])
def update_examination_date():

    naziv_arhive = request.get_json()['archive_name'].lower()
    mongo.db.Lista_arhiva.update_one({'naziv':naziv_arhive},{'$set':{'datum_pregleda':datetime.datetime.now()}})

    return "Dodano"


@app.route('/archives/SortArchives',methods=['POST'])
def sortArchives():

    if (mongo.db.Lista_arhiva.count()== 0):
        provjera = False
        return provjera

    else:
        sorttype = request.get_json()['sorttype']
        arhive = {}
        i = 0

        if(sorttype == 'abecedno_uzlazno' or sorttype == 'datum_pregleda_uzlazno'): ascORdes = 1
        else: ascORdes = -1
        if(sorttype == 'abecedno_uzlazno' or sorttype == 'abecedno_silazno'): sortby = "naziv"
        else: sortby = "datum_pregleda"

        for x in mongo.db.Lista_arhiva.find().sort('%s' % sortby,ascORdes):
            arhive[i] = {
                'ID' : str(x['_id']),
                'naziv' : x['naziv'].capitalize(),
                'datum_dodavanja' : x['datum_dodavanja'],
                'datum_pregleda' : x['datum_pregleda']
            }
            i += 1

        return jsonify(arhive)
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)
