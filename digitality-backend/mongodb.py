from pymongo import MongoClient
from datetime import datetime, timedelta

import bcrypt
import json
from bson import ObjectId

import default_data as dflt

db = None

def connect_to_db():
    try:
        cluster = MongoClient("mongodb+srv://Kristijan_10:Messi123@digitality-4hkuh.mongodb.net/digitality_production?retryWrites=true&w=majority")
        #cluster = MongoClient("mongodb+srv://admin:admin@cluster0-5uwqu.mongodb.net/test?retryWrites=true&w=majority")
        
        global db
        db = cluster["digitality_production"]
        
        index_email()
    
    except:
        print("Failed to connect to the database!")
        return None 
    
def index_email():
    collection = db["users"]
    collection.create_index([ ("email", -1) ], unique=True)


# COMPANY ###########################################################
def add_new_company(data):
    collection = db["Company"]
    data['_id'] = str(ObjectId())
    
    try:
        collection.insert(data)
    except:
        print("add_new_company() - failed to add new company!")
        return False
    
    return True

def get_company(oib):
    collection = db["Company"]
    return collection.find_one({'oib': oib})

def update_company(company_data): 
    collection = db["Company"]
    
    try:
        collection.find_one_and_replace({'_id': company_data['_id']}, company_data)   
    except:
        print("update_company() - failed to find and replace the document!")
        return False
    
    return True

# ARCHIVE ###########################################################
def get_archives(archive_ids):
    collection = db["archives"]
    
    filter = {'_id': {'$in':archive_ids}}
    
    try:
        arc = collection.find(filter)
    except:
        print("get_archives() - failed to get archives!")
        arc = None
        
    return arc

def get_one_archive(archive_id):
    collection = db["archives"]
    
    filter = {'_id': archive_id}
    try:
        arc = collection.find_one(filter)  
    except:
        print("get_one_archive() - failed to get archive!")
        arc = None
        
    return arc

def delete_archive(arc_id):
    collection = db["archives"]
    
    filter = {'_id': arc_id}

    try:
        collection.delete_one(filter)   
    except:
        print("delete_archive() - failed to delete archive!")
        return False
    
    return True     
    

# SUBARCHIVE ########################################################

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
        collection.update_one(filter, update)   
    except:
        print("update_subarchive() - failed to update document!")
        return False
    
    return True  

def delete_subarchive(arc_id, subarc_id):
    collection = db["archives"]
    
    filter = {'_id': arc_id}
    update = {
        '$pull':{'subarchives':{'subarchive_id': subarc_id}}
    }
    
    try:
        collection.update(filter, update)
    except:
        print("delete_subarchive() - failed to delete subarchive")
        return False
    
    return True


# Documents #########################################################
def create_document(arc_id, document):
    arc = get_one_archive(arc_id)
    index, subarchive = get_subarchive(arc, document['naziv_dobavljaca'])
    
    subarchive['documents'].append(document)
    if index:
        arc['subarchives'][index] = subarchive
    else:
        arc['subarchives'].append(subarchive)
    
    return update_subarchive(arc_id, arc['subarchives'])

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

def delete_document(arc_id, document):
    arc = get_one_archive(arc_id)
    index, subarchive = get_subarchive(arc, document['naziv_dobavljaca'])
    
    filtered_subarchive = [cur_doc for cur_doc in subarchive['documents'] if cur_doc['id_dokumenta'] != document['id_dokumenta']]
    subarchive['documents'] = filtered_subarchive
    
    arc['subarchives'][index] = subarchive
    
    return update_subarchive(arc_id, arc['subarchives']) 


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
        return False
    
    try:
        arc_collection.insert(default_arc)
    except:
        print("Failed to insert archive!")
        user_collection.delete_one({'_id': user['_id']}) # Ako je user insertan a archive nije, obrisi usera
        return False
    
    return True

def get_user(email):  
    collection = db["users"]
    
    if collection.count == 0:
        return False

    return collection.find_one({'email': email})

def delete_user(user):
    collection = db["users"]
    
    try:
        collection.delete_one({'email': user['email']})
        delete_archive(user['personal_archive_id'])
    except:
        print("Failed to delete user!")
        return False
    
    return True

def add_alias(alias):
    with open('current_user.json', 'r') as fp:
        user = json.load(fp)

    collection = db["users"]
    
    try:
        collection.update_one(
            {'email': user['email']},
            {'$push': {'alias_list': alias}}
        )
    except:
        print('add_alias() - cannot add alias!')
        return False
    
    return True

def delete_alias(alias_oib):
    with open('current_user.json', 'r') as fp:
        user = json.load(fp)

    collection = db["users"]
    
    try:
        collection.update_one(
            {'email': user['email']},
            {'$pull': {'alias_list': {'oib': alias_oib }}}
        )
    except:
        print('delete_alias() - cannot delete alias!')
        return False
    
    return True
        


# TESTING
def test_add_new_doc(test_archive_id):
    document = {
        'meta_data': {
            'added_by': 'jane@doe.com',
            'added_on': '01/01/2020',
            'added_at': '12:00'
        },
        'id_dokumenta': '5edfa361c509ffb1cf2ea928',
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
        'id_dokumenta': '5edfa361c509ffb1cf2ea928',
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

def test_delete_arc(test_archive_id):
    delete_archive(test_archive_id)

def test_delete_doc(test_archive_id, id_dokumenta):
    document = {
        'id_dokumenta': id_dokumenta,
        'naziv_dobavljaca': 'primjer'
    }
    
    delete_document(test_archive_id, document)

def test_delete_user():
    with open('current_user.json', 'r') as fp:
        user = json.load(fp) 
        
    delete_user(user)

def test_update_user():
    with open('current_user.json', 'r') as fp:
        user = json.load(fp) 
        
    update_user(user)

def test_add_alias():
    with open('current_user.json', 'r') as fp:
        user = json.load(fp)

    alias = {
        'ime': 'John',
        'prezime': 'Smith',
        'oib': '12345678901',
        'iban': 'HR123456789012',
        'postal_code': '10000',
    }
          
    add_alias(user, alias)

def test_delete_alias():
    with open('current_user.json', 'r') as fp:
        user = json.load(fp)

    alias = {
        "ime" : "John",
        "prezime" : "Smith",
        "oib" : "12345678901",
        "iban" : "HR123456789012",
        "postal_code" : "10000"
    }
    
    delete_alias(user, alias['oib'])
        

if __name__ == "__main__":
    connect_to_db()
    
    test_archive_id = '5eedf7ed594dfad0afab86c6'
    id_dokumenta = '5edfa361c509ffb1cf2ea928'
    
    #test_add_new_doc(test_archive_id)
    #test_update_doc(test_archive_id)
    
    #test_delete_arc(test_archive_id)
    #test_delete_doc(test_archive_id, id_dokumenta)
    
    #test_delete_user()
    #test_update_user()
    #test_add_alias()
    test_delete_alias()