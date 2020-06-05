from pymongo import MongoClient
import json

def connect_to_db():
    try:
        cluster = MongoClient("mongodb+srv://admin:admin@cluster0-5uwqu.mongodb.net/test?retryWrites=true&w=majority")
        return cluster["Test"]
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
 

def add_new_document(archive, document):
    db = connect_to_db()
    if not db:
        return None    
    collection = db["Archives"]
    
    filter = {'_id': archive}
    try:
        arch = collection.find_one(filter)  
    except:
        print("Fail - Collection.FindOne")
        return
    
    subarchive = document['naziv_dobavljaca']
    
    # APPEND NEW DOCUMENT
    try:
        arch[subarchive].append(document)
    except KeyError:
        arch[subarchive] = []
        arch[subarchive].append(document)
    except TypeError:
        print("Fail - Append()")
        return
    
    # UPDATE THE DATABASE
    update = {
        '$set': {subarchive: arch[subarchive]}
    }
    try:
        result = collection.update_one(filter, update)   
    except:
        print("Unable to update document")
        return
    
    return result


def get_cur_alias():
    with open('current_user.json', 'r') as fp:
        user = json.load(fp)   
    return user['alias']       



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
