from bson import ObjectId
from datetime import datetime

def get_subarchive(name):
    cur_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    return {
        #'subarchive_id': str(ObjectId()),
        'subarchive_id': 4,
        'name': name,
        'last_used': cur_date,
        'documents': []
    }

def get_default_arc():
    cur_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    example_dict = {
        "meta_data":{
            "added_by":"primjer@doe.com",
            "created_on": cur_date,
            "viewed_on": cur_date
        },
        
        #"id_dokumenta": str(ObjectId()),
        "id_dokumenta": 3,
        
        "naziv_dobavljaca": "primjer",
        "oib_dobavljaca": "16942983514",
        "iban_primatelja": "HR012329671212",
        
        "naziv_kupca": "John Doe",
        "oib_kupca": "32145678901",
        "iban_platitelja": "HR321456789012",
        "mjesto_izdavanja": "Zagreb",
        
        "datum_izdavanja": "01/01/2020",
        "datum_dospijeca": "01/02/2020",
        "datum_dodavanja": cur_date,
        
        "broj_racuna":"user_input",
        "poziv_na_broj":"user_input",
        
        "vrsta_usluge":"Struja",
        "iznos":100
    }
    
    subarchive = {
        #'subarchive_id': str(ObjectId()),
        'subarchive_id': 2,
        'name': "primjer",
        'last_used': cur_date,
        'documents': [example_dict]
    }
    
    return {
        #'_id' : str(ObjectId()),
        '_id' : 1,
        'name' : 'Example archive',
        'subarchives' : [subarchive],
    }
    
    
    
    
    