import re
import datetime
import mongodb as db
import data_analyse as da

# IZNOS RACUNA ##################################
def build_amounts_dict(total, pdv):
    #Pretrazujemo tekst za PDV te pomocu njega izracunavamo neto iznos
    neto = None
    if total:
        neto = total / (1 + (pdv/100))
    
    #Iznos racuna, pdv i neto iznos vracamo kao dictionary
    return {
        'total': total,
        'pdv': pdv,
        'neto': neto
    }    

def extract_pdv(text):
    #Tražimo pdv u tekstu, te zatim iz njega uklanjamo '%' da ga možemo pretvoriti u int
    #   ako nismo pronašli pdv, postavljamo ga na default, tj 25% 
    pattern = '(\d{2}%)'
    pdv = re.search(pattern, text).group()

    if pdv:
        pdv = pdv[:-1]
        pdv = int(pdv)
    else:
        pdv = 25
        
    return pdv    

def amounts_extraction(text):
    #Cijena moze biti zapisana sa '.' i sa ',' pa zbog toga imamo dva filter koja nam vracaju
    #   stringove koji se podudaraju s tim patternom
    pattern = '(\d{2,3},\d\d)'
    result = re.findall(pattern, text)

    pattern = '(\d{2,3}[.]\d\d)'
    result += re.findall(pattern, text)

    #Konacni iznos racuna pronalazimo tako da u nasoj listi pronalazimo najvecu vrijednost
    total = None
    if result:
        total = 0
        for price in result:
            price = float(price.replace(',', '.'))
            if price > total:
                total = price
    
    pdv = extract_pdv(text)
    
    return build_amounts_dict(total, pdv)


# POSTANSKI BROJ ################################
def postal_numbers(text):
    #Trazimo postanske brojeve na temelju danog patterna
    pattern = '\s\d{5}\s'
    postal_num = re.findall(pattern, text)
    
    #Uklanjamo duplikate iz nase liste te one brojeve koji nisu >= 10000 te <= 53296
    #   unutar tog raspona se krecu postanski brojevi u RH
    #   takve brojeve spremamo u novu listu koju zatim vracamo
    if postal_num:
        pc_nums = []
        for num in postal_num:
            num = int(num)
            if num >= 10000 and num <= 53296 and num not in pc_nums:
                pc_nums.append(num)
    
        return da.check_postal_code(pc_nums)
    else:
        return None


# DATUM #########################################
def payment_dates(text):
    #Trazimo datume po danom patternu
    pattern = '(\d{1,2}\.\d{1,2}.\d{4})'
    dates = re.findall(pattern, text)

    if dates:
        #Datume pretvaramo u datetime objekt za laksi daljni rad
        dates = [datetime.datetime.strptime(date, '%d.%m.%Y').date() for date in dates]

        #Uklanjamo duplikate iz liste te sortiramo listu datuma
        pc_nums = []
        for date in dates:
            if date not in pc_nums:
                pc_nums.append(date)    
        dates = sorted(pc_nums)

        #Vracamo dictionary sa datumom dospijeca i datumom izdavanja
        return {
            'dospijece': dates[-1],
            'izdavanje': dates[-2],
        }
    else:
        return {
            'dospijece': None,
            'izdavanje': None,
        }


# IBAN ##########################################
def iban_numbers(text):
    #Trazimo iban brojeve po danom patternu
    pattern = 'HR\d{19}'
    account_num = re.findall(pattern, text)
    
    pc_nums = None
    if account_num:
        #Uklanjamo duplikate iz liste
        pc_nums = []
        for num in account_num:
            if num not in pc_nums:
                pc_nums.append(num)
        
    #Vracamo listu iban brojeca
    return pc_nums


# OIB ###########################################
def oib_numbers(text):
    #Trazimo oib-e po danom patternu
    pattern = '\D\d{11}\D'
    oib = re.findall(pattern, text)

    #Dodatno filtriramo dobivene podatke jer gornji filter dohvaca suvisne znakove
    #   koje ovim for loopom uklanjamo
    if oib:
        pc_nums = []
        for num in oib:
            pattern = '\d{11}'
            result = re.findall(pattern, num)
            pc_nums.append(result[0])

        #Dohvacamo podatke o koriniku, to jest o izdavacu racuna iz baze na temelju oib-a
        #   te podatke zatim vracamo u main.py
        
        # TEST DATA #
        pc_nums = ['16962783514', '12345678901']
        
        return db.get_data_oib(pc_nums)
    else:
        return None

if __name__ == "__main__":
    file = open("text.txt","r+")
    text = file.read()

    print("###########################################################\n\n")
    
    print("Amounts:", amounts_extraction(text))
    print("Postal numbers:", postal_numbers(text))
    print("Payment dates", payment_dates(text))
    print("IBAN:", iban_numbers(text))
    #print("OIB:", oib_numbers(text))
    
    print("\n\n ###########################################################\n")