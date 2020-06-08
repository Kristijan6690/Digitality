from pymongo import MongoClient
from datetime import datetime, timedelta

import bcrypt
import json
from bson import ObjectId

import default_data as dflt

def connect_to_db():
    try:
        cluster = MongoClient("mongodb+srv://Kristijan_10:Messi123@digitality-4hkuh.mongodb.net/digitality_production?retryWrites=true&w=majority")
        #cluster = MongoClient("mongodb+srv://admin:admin@cluster0-5uwqu.mongodb.net/test?retryWrites=true&w=majority")
        return cluster["digitality_production"]
    except:
        print("Failed to connect to the database!")
        return None 


def update_company(company_data):
    db = connect_to_db()
    if not db:
        return None
    collection = db["Company"]
    
    try:
        result = collection.find_one_and_replace({'_id': company_data['_id']}, company_data)   
    except:
        print("update_company() - Unable to find and replace the document")
        return
    
    return result
 

def get_company(db, oib):
    collection = db["Company"]
    return collection.find_one({'oib': oib})


def get_data_oib(oib_list):
    db = connect_to_db()
    if not db:
        return None
        
    user_data = None
    company_data = None
    
    for oib in oib_list:
        if not company_data:
            company_data = get_company(db, oib)       
        elif not user_data:
            user_data = get_cur_alias()[0]
            
        if user_data and company_data:
            break
            
    return (user_data, company_data)
 

def get_archive(archive_id, collection=None):
    if not collection:
        db = connect_to_db()
        if not db:
            return None    
        collection = db["archives"]
    
    filter = {'_id': ObjectId(archive_id)}
    try:
        arc = collection.find_one(filter)  
    except:
        print("Fail - Collection.FindOne")
        arc = None
        
    return arc

def update_subarchive(arc, document):
    filter = {'_id': arc}
    update = {'$set': {subarchive: document}}
    
    try:
        result = collection.update_one(filter, update)   
    except:
        print("Unable to update document")
        result = None
    
    return result   


def update_document(arc, document):
    db = connect_to_db()
    if not db:
        return None    
    collection = db["archives"]
    
    arc = get_archive(arc, collection)
    subarchive = document['naziv_dobavljaca']
    
    # FIND AND REPLACE DOC IN LIST
    
    return update_subarchive(archive, arc[subarchive])

def create_document(arc, document):
    db = connect_to_db()
    if not db:
        return None    
    collection = db["archives"]
    
    arc = get_archive(arc, collection)
    subarchive = document['naziv_dobavljaca']
    
    try:
        arc[subarchive].append(document)
    except KeyError:
        arc[subarchive] = [document]
    
    return update_subarchive(arc, arc[subarchive])


def get_cur_alias():
    with open('current_user.json', 'r') as fp:
        user = json.load(fp)   
    return user['alias']       

# INDEXING ##########################################################
def index_email():
    db = connect_to_db()
    if not db:
        return None    
    collection = db["users"]
    
    collection.create_index([ ("email", -1) ], unique=True)

# USER ##############################################################
def register_user(user):
    db = connect_to_db()
    if not db:
        return None    
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
    db = connect_to_db()
    if not db:
        return None    
    collection = db["users"]
    
    if collection.count == 0:
        return False

    return collection.find_one({'email': email})
        
        
# TESTING
def test_add_new_doc():
    document = {
        'meta_data': {
            'added_by': 'jane@doe.com',
            'added_on': '01/01/2020',
            'added_at': '12:00'
        },
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
    add_new_document('7', document)
    
def test_get_data():
    oib = ['16962783514', '12345678901']
    print("Data:", get_data_oib(oib))
      
if __name__ == "__main__":
    test_add_new_doc()
