from pymongo import MongoClient

def connect_to_db():
    #Funkcija koja se poziva pri spajanju na bazu
    #   ako se se ne uspije spojiti, ispisuje se poruka i vraća None
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

    # SET THE FILTER
    filter = {
        '_id': company_data['_id']
    }
    
    # UPDATE THE DATABASE
    try:
        result = collection.find_one_and_replace(filter, company_data)   
    except:
        print("update_company() - Unable to find and replace the document")
        return
    
    return result


def get_pc_dict():
    db = connect_to_db()
    if not db:
        return None
    collection = db["Postal_code_dict"]
    
    return collection.find_one()    


def search_company(db, filter):
    #Dohvacamo trazeni collection s baze
    collection = db["Company"]
    
    return collection.find_one(filter)


def search_alias(db, filter):
    #Dohvacamo trazeni collection s baze
    collection = db["User"]        
    
    #Dohvacamo kljuc iz filtera prema kojem cemo pretrazivati podatke u aliasu
    key = next(iter(filter))
    
    #Dohvacamo trenutnog usera te listu njegovih aliasa spremamo u zasebnu varijablu   
    current_id = {
        '_id': '1'
    }
    user = collection.find_one(current_id) 
    aliases = user['alias']
    
    #Prolazimo kroz sve aliase te usporedujemo podatak iz filtera sa onim u aliasu
    #   Ako se podatak podudara, zaustavlja se for loop i vraca trenutni alias, u suprotnome,
    #   ako se niti jedan podatak ne podudara, for loop prolazi kroz sve aliase i vraća None
    data = None
    for alias in aliases:
        if filter[key] == alias[key]:
            data = alias
            break
        
    return data

        
def get_data_oib(oib_list):
    #Poziva se funkcija za spajanje na bazu, ako povezivanje na bazu ne uspije, pretraživanje se prekida i funkcija vraca None
    db = connect_to_db()
    if not db:
        return None
        
    user_data = None
    company_data = None
    
    #Provjeravamo svaki oib iz dobivene liste oib-a te ih pretrazujemo u kolekciji poduzeca i korisnika
    for oib in oib_list:
        #Ukoliko su se u listi oib-a našli nekakvi slucajni podaci, a mi već imamo podatke spremljene u
        #   varijable 'user_data' i 'company_data' prekidamo for loop jer nema potrebe da se dalje izvršava
        if user_data and company_data:
            break
        
        #Stvaramo filter prema kojemu ćemo pretrazivati podatke na bazi
        print("Looking for " + oib + " in the database!")
        filter = {
            'oib': oib
        }
        
        #Ako je vrijednost 'company_data' None tada se pretražuje collection za poduzeca
        #   prema danom filteru, ista stvar vrijedi za user data
        if not company_data:
            company_data = search_company(db, filter)
                      
        if not user_data:
            user_data = search_alias(db, filter)
    
    #Vracamo podatke u obliku rijecnika, ukoliko se podaci nisu pronašli, vratit cemo None         
    return {
        'user' : user_data,
        'company': company_data
    }
 

def add_new_document(archive, document):
    # CONNECT TO DATABASE
    db = connect_to_db()
    if not db:
        return None    
    collection = db["Archives"]
    
    # GET ARCHIVE
    filter = {
        '_id': archive
    }
    try:
        arch = collection.find_one(filter)  
    except:
        print("Fail - Collection.FindOne")
        return
    
    # GET SUBARCHIVE
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

    

if __name__ == "__main__":
    """
        oib = ['16962783514', '12345678901']
        
        data = get_data_oib(oib)
        
        if data:
            print("Data:", data)
        else:
            print("Data not found!")
        #print(get_pc_dict())
    """
    
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
    #add_new_document('7', document)
    company_data={
        '_id': '69',
        'naziv': 'Company K',
        'oib': '16962783514',

        'usluga': 'Internet', 
        'iban': [[3, 'HR012329678912'], [2, 'HR012345678512'], [1, 'HR765456278512']]           
    }
    res = update_company(company_data)  
    
    print(res)