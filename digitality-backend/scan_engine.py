import scan as scan
import extraction as extract
import mongodb as db
import data_analyse as da

from os import system

"""
Za spojit treba naadodat:
    mongodb.py line 39
    
Test data:
    if __name__=... u svakom file-u 

    extraction.py -> oib_numbers(text)
    
    data_analyse.py -> compare_user_iban(iban_list)
    data_analyse.py -> check_user_pc(pc_nums)
    data_analyse.py -> compare_user_iban(iban_list)
"""

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
    #Pozivamo funkciju za OCR kojoj proslijedujemo sliku racuna
    #   funkcija nam vraca tekst racuna koji ce se u daljem izvodenju koda obradivati
    scanned_text = scan.scan_image(path)
    
    #Funkcija za iznos racuna
    amounts = extract.amounts_extraction(scanned_text)
    
    #Funkcija za dobivanje postanskih brojeva sa racuna te dohvacanje mjesta izdavanja
    place = extract.postal_numbers(scanned_text)
    
    #Funkcija za dobivanje datuma dospijeca i datuma izdavanja
    dates = extract.payment_dates(scanned_text)
    
    #Funkcija nam daje listu iban brojeva koje pronade na racunu
    #   ocekuje se da ce vratiti listu sa 2 elementa[iban primatelja i iban platitelja]
    iban_list = extract.iban_numbers(scanned_text)
    
    #Funkcija u skeniramom tekstu pronalati oib-e te na temelju tih oib-a 
    #   vraca podatke o izdavacu racuna i kupcu
    data = extract.oib_numbers(scanned_text)
    user_data = data['user']
    company_data = data['company']

    company_data['iban'] = da.check_iban(iban_list, company_data)
    
    return build_dict(company_data, user_data, place, dates, amounts)


def add_to_database(archive, document): # Kao argument prima dokument(dict) koji se pohranjuje na bazu te _id arhive u koju se pohranjuje
    add_new_document(archive, document)
    update_data(document)

def update_data(document): # Kao argument prima dokument(dict), na temelju tih podataka se vrsi update vec postojecih podataka na bazi
    company_data = db.search_company(oib)


# TESTIRANJE ####################################
if __name__ == '__main__':
    print("\n")
    """
    path = './images/20200416_135328.jpg'
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
    """
    
    #update_data()
    
    
