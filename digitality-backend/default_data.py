from bson import ObjectId
from datetime import datetime

def get_default_arc():
    id = ObjectId()
    cur_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    example_dict = {
        "meta_data":{
            "added_by":"primjer@doe.com",
            "created_on": cur_date,
            "viewed_on": cur_date
        },
        
        "id_dokumenta": ObjectId(),
        
        "naziv_dobavljaca": "Company C",
        "oib_dobavljaca": "16942983514",
        "iban_primatelja": "HR012329671212",
        
        "naziv_kupca": "John Doe",
        "oib_kupca": "32145678901",
        "iban_platitelja": "HR321456789012",
        "mjesto_izdavanja": "Zagreb",
        
        "datum_izdavanja": "01/01/2020",
        "datum_dospijeca": "01/02/2020",
        
        "broj_racuna":"user_input",
        "poziv_na_broj":"user_input",
        
        "vrsta_usluge":"Struja",
        "iznos":"100kn"
    }
    
    subarchive = {
        'subarchive_id': ObjectId(),
        'name': "primjer",
        'last_used': cur_date,
        'documents': [example_dict]
    }
    
    return {
        '_id' : id,
        'naziv' : 'Example archive',
        
        'subarchives' : [subarchive],
    }
    
    
    
    
    