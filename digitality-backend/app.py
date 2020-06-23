from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from flask import Flask, jsonify , request, json
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson import ObjectId

import datetime, jwt, os, json, re, operator
import current_user as current
import default_data as dflt
import mongodb as mongodb
import scan_engine

mongodb.connect_to_db()

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Kristijan_10:Messi123@digitality-4hkuh.mongodb.net/digitality_production?retryWrites=true&w=majority'
#app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@cluster0-5uwqu.mongodb.net/test?retryWrites=true&w=majority'


mongo = PyMongo(app)
bcrypt = Bcrypt(app)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return "Hello World"

@app.route('/register', methods=['POST'])
def register():
    doc = request.get_json()
    
    user = {
        '_id': str(ObjectId()),
        'name': doc['name'],
        'surname': doc['surname'],
        'email': doc['email'],
        'password': bcrypt.generate_password_hash(doc['password'], 8),
        'personal_archive_id': None,
        'archive_ids': None,        
        'alias_list': [],
        'email_list': []
    }
    
    res = mongodb.register_user(user)
    return jsonify(res)


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
    
    current.user = user 
        
    return jsonify(user)


@app.route('/GetArchives', methods=['POST'])
def getarhive():
    print(request.get_json(['email']))
    user = mongodb.get_user(request.get_json()['email'])
    
    if not user:
        return jsonify(False)
    
    archive_ids = user['archive_ids']
    archives = list(mongodb.get_archives(archive_ids))
    
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
    result = mongodb.get_archives( request.get_json()['archive_ids'] )
    searchTerm = str(request.get_json()['searchTerm']).lower()
    
    if not searchTerm:
        return jsonify(result)
    
    currentArchive_id = request.get_json()['currentArchive_id']
    cur_arc = mongodb.get_one_archive(currentArchive_id)
    
    regex = re.compile('^(%s)' % searchTerm)
    subarchives = [sub_arc for sub_arc in cur_arc['subarchives'] if regex.match(sub_arc['name']) ] 
    
    for archives in result:
        if archives['_id'] == currentArchive_id:
            archives['subarchives'] = subarchives

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

@app.route('/archive/deleteSubarchive', methods=['DELETE'])
def deleteSubarchive():
    doc = request.get_json()

    user = current.user
        
    if user['personal_archive_id'] == doc['personal_archive_id']:
        res = mongodb.delete_subarchive(doc['personal_archive_id'], doc['subarchive_id'])
        return jsonify(res)
    else:
        return jsonify(False)


@app.route('/archive/UpdateExaminationDate', methods=['POST'])
def update_examination_date():
    res = mongodb.update_examination_time(request.get_json())
    
    return jsonify(res)


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


@app.route('/archives/share', methods=['POST'])
def share_archive():

    doc = request.get_json()
    flag1 = False
    flag2 = True

    for user in mongo.db.users.find():
        if(user['email'] == doc['shared_email']):
            share_user = user
            flag1 = True
    
    for user in mongo.db.users.find():
        if(user['email'] == doc['user_email']):
            for email in user['email_list']:
                if(email == doc['shared_email']):
                    flag2 = False

    if(flag1 and flag2):
        mongo.db.users.update({'email': doc['user_email']},{'$push': {'archive_ids': share_user['personal_archive_id'],'email_list': share_user['email']}})
        return jsonify(share_user['_id'],share_user['email'])

    else: return jsonify(False) 


@app.route('/archives/shareDelete', methods=['POST'])
def delete_shared_archive():

    doc = request.get_json()
    share_user = mongo.db.users.find_one({'email': doc['shared_email']})
    mongo.db.users.update({'email': doc['user_email']},{'$pull':{'archive_ids': share_user['personal_archive_id'],'email_list': share_user['email']}})
    owner = mongo.db.users.find_one({'email': doc['user_email']})
    return jsonify(owner['archive_ids'], owner['email_list'])


@app.route('/addAlias', methods=['PUT'])
def add_alias():
    new_alias = request.get_json()
    res = mongodb.add_alias(new_alias)
    
    return jsonify(res)


@app.route('/deleteAlias', methods=['DELETE'])
def delete_alias():
    alias = request.get_json()
    res = mongodb.delete_alias(alias['oib'])

    return jsonify(res)


if __name__ == "__main__":
    app.run(port=5000, debug=True)