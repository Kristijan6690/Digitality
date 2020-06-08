from flask import Flask, jsonify , request, json
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson import ObjectId
import operator,re,datetime,scan_engine

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
    
    name = request.get_json()['name']
    surname = request.get_json()['surname']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password'])
    personal_archive_id = ObjectId()
    subarchive_id = ObjectId()
    date = datetime.datetime.now()
    document_id = ObjectId()
    user_id = ObjectId()

    mongo.db.users.insert({
        '_id' : user_id,
        'name' : name,
        'surname' : surname,
        'email' : email,
        'password' : password,
        'personal_archive_id' : personal_archive_id,
        'archive_ID' : [],
        'alias' : []
    })
    mongo.db.archives.insert({
        '_id' : personal_archive_id,
        'naziv' : 'Arhiva A',
        'subarchive_names' : [{'subarchive_id': subarchive_id,'name': "primjer",'examination_date': ''}],
        'primjer' : [{"meta_data":{"added_by":"primjer@doe.com","added_on":"01/01/2020","added_at":"12:00"},"id_dokumenta":document_id,"naziv_dobavljaca":"Company C","oib_dobavljaca":"16942983514","iban_primatelja":"HR012329671212","naziv_kupca":"John Doe","oib_kupca":"32145678901","iban_platitelja":"HR321456789012","mjesto_izdavanja":"Zagreb","datum_izdavanja":"01/01/2020","datum_dospijeca":"01/02/2020","datum_dodavanja":date,"datum_pregleda":"06/06/2020","broj_racuna":"user_input","poziv_na_broj":"user_input","vrsta_usluge":"Struja","iznos":"100kn"}]
    })

    return "Poslano"


@app.route('/login', methods=['POST'])
def login():

    access = ""
    
    if (mongo.db.users.count() == 0):
        access = False
        return jsonify(access)

    else:
        email = request.get_json()['email']
        password = request.get_json()['password']
        for x in mongo.db.users.find():
            if (x['email'] == email):
                if bcrypt.check_password_hash(x['password'],password):
                    access = {
                        'id' : str(x['_id']),
                        'ime' : x['name'],
                        'prezime' : x['surname'],
                        'email' : x['email'],
                        'personal_archive_id' : str(x['personal_archive_id'])
                    }     
                else:
                    access = False
        
        return jsonify(access)


#jos da vraća alliase kad budu
@app.route('/GetArchives', methods=['POST'])
def getarhive():

    if (mongo.db.archives.count()== 0):
        provjera = False
        return jsonify(provjera)

    else:
        user_id = request.get_json()['user_id']
        provjera = False

        for x in mongo.db.users.find():
            if(str(x['_id']) == user_id):
                personal_archive_id = str(x['personal_archive_id'])
                provjera = True

        if(provjera):
            for x in mongo.db.archives.find():
                if(str(x['_id']) == personal_archive_id):
                    subArchives = []
                    for subAtributes in x['subarchive_names']:
                        subArchives.append(subAtributes)
            #str(OBJECTID)
            for counter,sub in enumerate(subArchives):
                if(subArchives[counter]['subarchive_id']):
                    sub = subArchives[counter]['subarchive_id']
                    subArchives[counter]['subarchive_id'] = str(sub)

            return jsonify(subArchives)

        else:
            return jsonify(provjera)


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
