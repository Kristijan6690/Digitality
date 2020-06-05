import re
import datetime
import mongodb as db
import data_analyse as da

# IZNOS RACUNA ##################################
def build_amounts_dict(total, pdv):
    neto = None
    if total:
        neto = total / (1 + (pdv/100))
    
    return {'total': total, 'pdv': pdv, 'neto': round(neto, 2)}    

def extract_pdv(text):
    pattern = '(\d{2}%)'
    pdv = re.search(pattern, text).group()

    if pdv:
        return int(pdv[:-1])
    else:
        return 25 

def amounts_extraction(text):
    results = re.findall('(\d{2,3}(\.|,)\d\d)', text)
    results = [res[0] for res in results]

    if results:
        results = [float(elem.replace(',', '.')) for elem in results]
        total = max(results)
    
    pdv = extract_pdv(text)
    
    return build_amounts_dict(total, pdv)


# POSTANSKI BROJ ################################
def filter_p_codes(p_code):
    p_code = int(p_code)
    if (p_code >= 10000) and (p_code <= 53296):
        return p_code
        
def postal_numbers(text):
    p_codes = re.findall('\s\d{5}\s', text)

    if p_codes:
        p_codes = [filter_p_codes(code) for code in p_codes] # Uklanjanje nevazecih brojeva
        p_codes = list(dict.fromkeys(p_codes)) # Uklanjanje duplikata
    
        return da.check_postal_code(p_codes) # Postanski broj u mjesto
    else:
        return None


# DATUM #########################################
def check_dates(dates):
    length = len(dates)
    
    if length <= 2:
        add_on = [None for elem in range(2 - length)] # Ako su 2< datuma, dodaj kolko ih fali
        dates += add_on
    return dates
    
def payment_dates(text):
    dates = re.findall('(\d{1,2}\.\d{1,2}.\d{4})', text)

    dates = [datetime.datetime.strptime(date, '%d.%m.%Y').date() for date in dates]
    dates = sorted(list(dict.fromkeys(dates)))
    dates = check_dates(dates)
    
    return {'dospijece': dates[-1], 'izdavanje': dates[-2]}


# IBAN ##########################################
def iban_numbers(text):
    account_num = re.findall('HR\d{19}', text)
    
    if account_num:
        return list(dict.fromkeys(account_num))
    else:
        return None

# OIB ###########################################
def oib_numbers(text):
    oib_list = re.findall('\D\d{11}\D', text)

    if oib_list:
        oib_list = [re.findall('\d{11}', num)[0] for num in oib_list]
    
        oib_list = ['16962783514', '12345678901'] # TEST DATA <-----------------------------
        
        return db.get_data_oib(oib_list) # Dohvacamo alias/izdavaca racuna na temelju oib-a
    else:
        return (None, None)


# TESTIRANJE 
if __name__ == "__main__":
    file = open("text.txt","r+")
    text = file.read()

    print("###########################################################\n\n")
    
    #print("Amounts:", amounts_extraction(text))
    #print("Postal numbers:", postal_numbers(text))
    #print("Payment dates", payment_dates(text))
    #print("IBAN:", iban_numbers(text))
    
    user, company = oib_numbers(text)
    print("User:", user)
    print("Company:", company)
    
    print("\n\n ###########################################################\n")