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
app.config['MONGO_URI'] = 'mongodb+srv://Kristijan_10:Messi123@digitality-4hkuh.mongodb.net/digitality_production?retryWrites=true&w=majority'

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
        return jsonify(False)
    
    personal_archive_id = user['personal_archive_id']
    archive = mongodb.get_archive(personal_archive_id)
    
    if not archive:
        return jsonify(False)

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
            
            for doc in documents:
                doc['id_dokumenta'] = str(doc['id_dokumenta'])
                    
            return jsonify(documents) 

        else:
            documents = False
            return jsonify(documents)

    for x in mongo.db.archives.find():
        if(str(x['_id']) == personal_archive_id):
            if (len(x[subArchive_name]) == 0):
                documents = False
                return jsonify(documents)

# RAZRADA JOS TESKA
@app.route('/send_document', methods=['POST'])
def sendDocument():

    doc_url = request.get_json()['doc_url']
    doc_data = scan_engine.photo_to_dict(doc_url)

    return jsonify(doc_data)


@app.route('/search/lista_arhiva', methods=['POST'])
def searchArchives():

    searchTerm = str(request.get_json()['searchTerm'])
    searchTerm = searchTerm.lower()
    personal_archive_id = ObjectId(request.get_json()['personal_archive_id']) 
    result = []

    if(searchTerm):
        r = re.compile('^(%s)' % searchTerm)

        for x in mongo.db.archives.find():
            if(x['_id'] == personal_archive_id):
                for sub in x['subarchive_names']:
                    if(r.match(sub['name'])):
                        result.append(sub)    

        for sub in result:
            sub['subarchive_id'] = str(sub['subarchive_id'])

        return jsonify(result)

    else:
        for x in mongo.db.archives.find():
           if(x['_id'] == personal_archive_id):
               for sub in x['subarchive_names']:
                   result.append(sub)    

        for sub in result:
            sub['subarchive_id'] = str(sub['subarchive_id'])
        
            
        return jsonify(result)  


@app.route('/archives/createSubarchive', methods=['POST'])
def createSubarchive():
    archive_name = request.get_json()['archive_name'].lower()
    personal_archive_id = ObjectId(request.get_json()['personal_archive_id'])
    
    subarchive_id = ObjectId()
    
    mongo.db.archives.update({'_id': personal_archive_id},{'$push':{
        'subarchive_names': {
            'subarchive_id': subarchive_id,
            'name': archive_name,
            'examination_date': datetime.datetime.now()
        }}, '$set':{ archive_name: [] }})
        
    return "Dodano"


@app.route('/archive/deleteSubarchive', methods=['POST'])
def deleteSubarchive():
    personal_archive_id = ObjectId(request.get_json()['personal_archive_id'])
    subarchive_id = ObjectId(request.get_json()['subarchive_id'])
    subarchive_name = request.get_json()['subarchive_name'].lower()
    result = []

    mongo.db.archives.update({'_id': personal_archive_id},{'$pull':{'subarchive_names':{'subarchive_id':subarchive_id}}})
    mongo.db.archives.update({subarchive_name: []},{'$unset':{ subarchive_name: 1}})
    for x in mongo.db.archives.find():
        if(x['_id'] == personal_archive_id):
            for sub in x['subarchive_names']:
                result.append(sub)
    
    for sub in result:
        sub['subarchive_id'] = str(sub['subarchive_id'])
    
    return jsonify(result)


@app.route('/archive/UpdateExaminationDate', methods=['POST'])
def update_examination_date():

    personal_archive_id = ObjectId(request.get_json()['personal_archive_id'])
    subarchive_id = ObjectId(request.get_json()['subarchive_id'])
    for x in mongo.db.archives.find():
        if(x['_id'] == personal_archive_id):
            mongo.db.archives.update({'subarchive_names.subarchive_id':subarchive_id},{'$set':{'subarchive_names.$.examination_date': datetime.datetime.now()}})
            return "Dodano"


@app.route('/archives/SortArchives', methods=['POST'])
def sortArchives():

    if (mongo.db.archives.count() == 0):
        provjera = False
        return provjera

    else:
        sorttype = request.get_json()['sorttype']
        personal_archive_id = ObjectId(request.get_json()['personal_archive_id'])
        subArchives = []

        if(sorttype == 'abecedno_uzlazno' or sorttype == 'datum_pregleda_uzlazno'): ascORdes = False
        else: ascORdes = True
        if(sorttype == 'abecedno_uzlazno' or sorttype == 'abecedno_silazno'): sortby = "name"
        else: sortby = "examination_date"

        for x in mongo.db.archives.find():
            if(x['_id'] == personal_archive_id):
                for sub in x['subarchive_names']:
                    subArchives.append(sub)

        for sub in subArchives:
            sub['subarchive_id'] = str(sub['subarchive_id'])

        subArchives.sort(key=operator.itemgetter(sortby),reverse=ascORdes)

        return jsonify(subArchives)
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)
