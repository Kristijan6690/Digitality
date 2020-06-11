from pymongo import MongoClient
from datetime import datetime, timedelta

import bcrypt
import json
from bson import ObjectId

import default_data as dflt

db = None

def connect_to_db():
    try:
        #cluster = MongoClient("mongodb+srv://Kristijan_10:Messi123@digitality-4hkuh.mongodb.net/digitality_production?retryWrites=true&w=majority")
        cluster = MongoClient("mongodb+srv://admin:admin@cluster0-5uwqu.mongodb.net/test?retryWrites=true&w=majority")
        global db
        db = cluster["digitality_production"]
    except:
        print("Failed to connect to the database!")
        return None 


def update_company(company_data):
    collection = db["Company"]
    
    try:
        result = collection.find_one_and_replace({'_id': company_data['_id']}, company_data)   
    except:
        print("update_company() - Unable to find and replace the document")
        return
    
    return result


def get_company(oib):
    collection = db["Company"]
    return collection.find_one({'oib': oib})

def get_archives(archive_ids):
    collection = db["archives"]
    
    filter = {'_id': {'$in':archive_ids}}
    
    try:
        arc = collection.find(filter)
    except:
        print("Fail - Collection.Find")
        arc = None
        
    return arc

def get_one_archive(archive_id):
    collection = db["archives"]
    
    filter = {'_id': archive_id}
    try:
        arc = collection.find_one(filter)  
    except:
        print("Fail - Collection.FindOne")
        arc = None
        
    return arc

def get_subarchive(arc, subarchive_name):
    for index, subarchive in enumerate(arc['subarchives']):
        if subarchive_name == subarchive['name']:
            return (index, subarchive)
        
    return (None, dflt.get_subarchive(subarchive_name))

def update_subarchive(arc_id, document):
    collection = db["archives"]
    
    filter = {'_id': arc_id}
    update = {'$set': {'subarchives': document}}
    
    try:
        result = collection.update_one(filter, update)   
    except:
        print("Unable to update document")
        result = None
    
    return result   


def update_document(arc_id, document):
    arc = get_one_archive(arc_id)
    index, subarchive = get_subarchive(arc, document['naziv_dobavljaca'])
    
    # FIND AND REPLACE DOC IN LIST
    for idx, doc in enumerate(subarchive['documents']):
        if doc['_id'] == document['_id']:
            subarchive['documents'][idx] = document
            break
      
    arc['subarchives'][index] = subarchive
    
    return update_subarchive(arc_id, arc['subarchives'])

def create_document(arc_id, document):
    arc = get_one_archive(arc_id)
    index, subarchive = get_subarchive(arc, document['naziv_dobavljaca'])
    
    subarchive['documents'].append(document)
    if index:
        arc['subarchives'][index] = subarchive
    else:
        arc['subarchives'].append(subarchive)
    
    return update_subarchive(arc_id, arc['subarchives'])
     

# INDEXING ##########################################################
def index_email():
    collection = db["users"]
    
    collection.create_index([ ("email", -1) ], unique=True)

# USER ##############################################################
def register_user(user): 
    user_collection = db["users"]
    arc_collection = db["archives"]
    
    default_arc = dflt.get_default_arc()

    user['archive_ids'] = [str(default_arc['_id'])]
    user['personal_archive_id'] = str(default_arc['_id'])
    
    try:
        user_collection.insert(user)
    except:
        print("Failed to insert user!")
        return "Fail"
    
    try:
        arc_collection.insert(default_arc)
    except:
        print("Failed to insert archive!")
        user_collection.remove({'_id': user['_id']}) # Ako je user insertan a archive nije, obrisi usera
        return "Fail"
    
    return "Success"


def get_user(email):  
    collection = db["users"]
    
    if collection.count == 0:
        return False

    return collection.find_one({'email': email})
        
        
# TESTING
def test_add_new_doc(test_archive_id):
    document = {
        'meta_data': {
            'added_by': 'jane@doe.com',
            'added_on': '01/01/2020',
            'added_at': '12:00'
        },
        '_id': '5edfa361c509ffb1cf2ea928',
        'naziv_dobavljaca': 'Company C',
        'oib_dobavljaca': '16942983514',
        'iban_primatelja': 'HR012329671212',    
        
        'naziv_kupca': 'John Doe',
        'oib_kupca': '32145678901',
        'iban_platitelja': 'HR321456789012',
        
        'mjesto_izdavanja': 'Zagreb',
        'datum_izdavanja': '01/01/2020',
        'datum_dospijeca': '01/02/2020',
        
        'broj_racuna': 'user_input',
        'poziv_na_broj': 'user_input',
        'vrsta_usluge': 'Struja',
        'iznos': '100kn'
    }
    create_document(test_archive_id, document)
    
def test_update_doc(test_archive_id):
    document = {
        'meta_data': {
            'added_by': 'jane@doe.com',
            'added_on': '01/01/2020',
            'added_at': '12:00'
        },
        '_id': '5edfa361c509ffb1cf2ea928',
        'naziv_dobavljaca': 'Company C',
        'oib_dobavljaca': '16942983514',
        'iban_primatelja': 'HR012329671212',    
        
        'naziv_kupca': 'John Doe',
        'oib_kupca': '32145678901',
        'iban_platitelja': 'HR321456789012',
        
        'mjesto_izdavanja': 'Zagreb',
        'datum_izdavanja': '01/01/2020',
        'datum_dospijeca': '01/02/2020',
        
        'broj_racuna': 'user_input',
        'poziv_na_broj': 'user_input',
        'vrsta_usluge': 'Struja',
        'iznos': '900kn'
    }
    update_document(test_archive_id, document)
        
def test_get_data():
    oib = ['16962783514', '12345678901']
    print("Data:", get_data_oib(oib))
      
if __name__ == "__main__":
    connect_to_db()
    
    test_archive_id = '5edfb6448f7d7c4c08b35d77'
    
    #test_add_new_doc(test_archive_id)
    #test_update_doc(test_archive_id)
