import scan as scan
import extraction as extract
import mongodb as db
import data_analyse as da

from datetime import datetime

"""
    Za spojit treba naadodat:
        mongodb.py line 39
        
    Test data:
        if __name__=... u svakom file-u 

        extraction.py -> oib_numbers(text)
"""

# SCAN IMG
def build_dict(company_data, user_data, place, dates, amounts):
    if not company_data:
        company_data = {
            'naziv': None,
            'oib': None,
            'iban': None        
        }
    
    if not user_data:
        user_data = {
            'ime': None,
            'prezime': None,
            'oib': None,
            'iban': None,            
        }
    
    return {
        'naziv_dobavljaca': company_data['naziv'],
        'oib_dobavljaca': company_data['oib'],
        'iban_primatelja': company_data['iban'],     
        
        'naziv_kupca': user_data['ime'] + " " + user_data['prezime'],
        'oib_kupca': user_data['oib'],
        'iban_platitelja': user_data['iban'],
        
        'mjesto_izdavanja': place,
        'datum_izdavanja': dates['izdavanje'],
        'datum_dospijeca': dates['dospijece'],
        
        'broj_racuna': None,
        'poziv_na_broj': None,
        
        'iznos': amounts['total'],
        'pdv': amounts['pdv'],
        'neto': amounts['neto']       
    }

def photo_to_dict(path):
    scanned_text = scan.scan_image(path)
    
    amounts = extract.amounts_extraction(scanned_text)
    place = extract.postal_numbers(scanned_text)
    dates = extract.payment_dates(scanned_text)
    iban_list = extract.iban_numbers(scanned_text)
    
    # Na temelju oib-a se iz baze povlace podaci o korisniku i izdavacu racuna
    user_data, company_data = extract.oib_numbers(scanned_text)

    company_data['iban'] = da.check_iban(iban_list, company_data)
    
    return build_dict(company_data, user_data, place, dates, amounts)

# ADD DOC
def add_meta_data():
    with open('current_user.json', 'r') as fp:
        user = json.load(fp) 
    
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return {'user': user['email'], 'date': date}

def add_to_database(archive, document):
    document['meta_data'] = add_meta_data()
    
    db.add_new_document(archive, document)
    update_data(document)

def update_data(document):
    company_data = db.get_company(db.connect_to_db(), document['oib_dobavljaca'])
    update_company_iban(document['iban_primatelja'], company_data)


# TESTING 
def test_scaning():
    path = r'https://firebasestorage.googleapis.com/v0/b/digitality-1234567890.appspot.com/o/kkrulic%40unipu.hr%2F1591097366198.png?alt=media&token=2c0371a9-6912-405e-a0b0-b28b00f486c6&fbclid=IwAR1fslrU4OcNOud192dLA5QQUdxwdFOpNH8STNpYT1u4iryGLOsFAoL0oJs'
    #path = './images/20200416_135328.jpg'
    #path = './images/20200323_142140.jpg'
    final_dict = photo_to_dict(path)
    
    print("###########################################################\n")
    
    print('Naziv dobavljaca: ',final_dict['naziv_dobavljaca'])
    print('OIB dobavljaca: ',final_dict['oib_dobavljaca'])
    print('IBAN primatelja: ',final_dict['iban_primatelja'])

    print('Naziv kupca: ',final_dict['naziv_kupca'])
    print('OIB kupca: ',final_dict['oib_kupca'])
    print('IBAN platitelja: ',final_dict['iban_platitelja'])

    print('Mjesto izdavanja: ',final_dict['mjesto_izdavanja'])
    print('Datum izdavanja: ',final_dict['datum_izdavanja'])
    print('Datum dospijeca: ',final_dict['datum_dospijeca'])

    print('Broj racuna: ',final_dict['broj_racuna'])
    print('Poziv na broj: ',final_dict['poziv_na_broj'])

    print('Neto: ',final_dict['neto'])   
    print('PDV: ',final_dict['pdv'])   
    print('Iznos: ',final_dict['iznos'])   
    
    print("\n###########################################################")

def test_update_data():
    doc = {
        'meta_data': {
            'added_by': 'john@smith.com',
            'added_on': '01/01/2020',
            'added_at': '12:00'
        },
        'naziv_dobavljaca': 'Company A',
        'oib_dobavljaca': '16962783514',
        'iban_primatelja': 'HR012329678912',    
        
        'naziv_kupca': 'John Smith',
        'oib_kupca': '12345678901',
        'iban_platitelja': 'HR123456789012',
        
        'mjesto_izdavanja': 'Zagreb',
        'datum_izdavanja': '01/01/2020',
        'datum_dospijeca': '01/02/2020',
        
        'broj_racuna': 'user_input',
        'poziv_na_broj': 'user_input',
        'vrsta_usluge': 'Internet',
        'iznos': '100kn'
    }
    res = update_data(doc)
    print(res)
    
if __name__ == '__main__':
    test_scaning()
    #test_update_data()
    
    
