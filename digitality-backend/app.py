from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from flask import Flask, jsonify , request, json
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson import ObjectId

import datetime,jwt,os,scan_engine,re,operator
import default_data as dflt
import mongodb as mongodb

mongodb.connect_to_db()
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
    
    archive_ids = user['archive_ids']
    archives = list(mongodb.get_archive(archive_ids))
    
    if not archives:
        return jsonify(False)

    return jsonify(archives)


@app.route('/send_document', methods=['POST'])
def sendDocument():

    doc_url = request.get_json()['doc_url']
    doc_data = scan_engine.photo_to_dict(doc_url)

    return jsonify(doc_data)


@app.route('/search/lista_arhiva', methods=['POST'])
def searchArchives():

    searchTerm = str(request.get_json()['searchTerm'])
    searchTerm = searchTerm.lower()
    archive_ids = request.get_json()['archive_ids']
    currentArchive_id = request.get_json()['currentArchive_id']
    result = []
    subarchives = []

    for archives in mongo.db.archives.find({'_id': {'$in':archive_ids}}):
        result.append(archives)

    if(searchTerm):
        r = re.compile('^(%s)' % searchTerm)
        for archives in mongo.db.archives.find():
            if(archives['_id'] == currentArchive_id):
                for sub in archives['subarchives']:
                    if(r.match(sub['name'])):
                        subarchives.append(sub)   

        for archives in result:
            if(archives['_id'] == currentArchive_id):
                archives['subarchives'] = subarchives

        return jsonify(result)

    else:
        return jsonify(result)  


@app.route('/archives/createSubarchive', methods=['POST'])
def createSubarchive():
    archive_name = request.get_json()['archive_name'].lower()
    personal_archive_id = request.get_json()['personal_archive_id']
    subarchive_id = str(ObjectId())
    
    mongo.db.archives.update({'_id': personal_archive_id},{'$push':{
        'subarchives': {
            'subarchive_id': subarchive_id,
            'name': archive_name,
            'last_used': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'documents': []
        }}})
        
    return "Dodano"


@app.route('/archive/deleteSubarchive', methods=['POST'])
def deleteSubarchive():

    doc = request.get_json()
    mongo.db.archives.update({'_id': doc['personal_archive_id']},{'$pull':{'subarchives':{'subarchive_id':doc['subarchive_id']}}})
    
    return "Izbrisano"


@app.route('/archive/UpdateExaminationDate', methods=['POST'])
def update_examination_date():

    doc = request.get_json()
    for archive in mongo.db.archives.find():
        if(archive['_id'] == doc['currentArchive_id']):
            mongo.db.archives.update({'subarchives.subarchive_id':doc['subarchive_id']},{'$set':{'subarchives.$.last_used': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}})
            return "Dodano"


@app.route('/archives/SortArchives', methods=['POST'])
def sortArchives():

    if (mongo.db.archives.count() == 0):
        provjera = False
        return jsonify(provjera)

    else:
        doc = request.get_json()
        result = []
        subarchives = []

        if(doc['sorttype'] == 'abecedno_uzlazno' or doc['sorttype'] == 'datum_pregleda_uzlazno'): ascORdes = False
        else: ascORdes = True
        if(doc['sorttype'] == 'abecedno_uzlazno' or doc['sorttype'] == 'abecedno_silazno'): sortby = "name"
        else: sortby = "last_used"

        for archives in mongo.db.archives.find({'_id': {'$in':doc['archive_ids']}}):
            result.append(archives)

        for archives in mongo.db.archives.find():
            if(archives['_id'] == doc['currentArchive_id']):
                for sub in archives['subarchives']:
                    subarchives.append(sub)

        subarchives.sort(key=operator.itemgetter(sortby),reverse=ascORdes)
        
        for archives in result:
            if(archives['_id'] == doc['currentArchive_id']):
                archives['subarchives'] = subarchives

        return jsonify(result)
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)
