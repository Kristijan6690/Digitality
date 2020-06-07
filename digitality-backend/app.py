from flask import Flask, jsonify , request, json
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson import ObjectId
import datetime
import scan_engine

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Kristijan_10:Messi123@digitality-4hkuh.mongodb.net/digitality_production?retryWrites=true&w=majority'


mongo = PyMongo(app)
bcrypt = Bcrypt(app)
CORS(app)

@app.route('/')
def index():
    return "Hello World"


@app.route('/register', methods=['POST'])
def registracija():
    
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
@app.route('/send_document', methods=['POST'])
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
    mongo.db.archives.update({'$unset':{subarchive_name}})
    

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
