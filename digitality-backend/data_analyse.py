import mongodb as db
import json

# IBAN ##########################################
def compare_possible_ibans(iban, company_data):
    # possible_ibans - iban brojevi koji se nisu pojavili dovoljno puta da bi se smatrali validnima
    try:
        possible_ibans = company_data['possible_ibans'] # okida try/except
        
        boundary = 5 
        upgrade_index = -1
        is_found = False
        
        for index, cur_iban in enumerate(possible_ibans):
            if cur_iban[1] == iban: 
                cur_iban[0] += 1
                is_found = True
                
                if cur_iban[0] >= boundary:
                    upgrade_index = index
                else:
                    possible_ibans[index] = cur_iban
                    
                break
        
        if not is_found:
            new_iban = [1, iban]
            company_data['possible_ibans'].append(new_iban)  
        
        elif upgrade_index != -1:
            new_iban = possible_ibans.pop(upgrade_index)
            company_data['iban'].append(new_iban)
    
    except:
        # ako ne postoji possible_ibans, stvori ga
        company_data['possible_ibans'] = [[1, iban]] 
            
    return company_data   
                   
def update_company_iban(iban, company_data):
    company_ibans = company_data['iban'] # format: company_ibans = [[broj_pojava, iban], [3, HR012345678512]]
    
    is_found = False
    # Pronadi iban i povecaj ucestalost za +1
    for index, cur_iban in enumerate(company_ibans):
        if cur_iban[1] == iban:
            company_ibans[index][0] += 1
            is_found = True
            break
    
    # Ako ne pronades, pretrazi u mogucim iban brojvima
    if not is_found:
        company_data = compare_possible_ibans(iban, company_data)

    company_ibans = sorted(company_ibans, key = lambda sub_list: sub_list[0])
    db.update_company(company_data)
    
    return company_data

def compare_user_iban(iban_list):
    with open('current_user.json', 'r') as fp:
        user = json.load(fp)   
    
    aliases = user['alias']
    alias_ibans = [alias['iban'] for alias in aliases]

    for index, iban in enumerate(iban_list):
        if iban in alias_ibans:
            iban_list.pop(index)
            break

    return iban_list    

def check_iban(iban_list, company_data):
    company_ibans = company_data['iban'] # format: company_ibans = [[broj_pojava, iban], [3, HR012345678512]]
    company_ibans = [iban[1] for iban in company_ibans]
        
    # Edge case handling
    if not iban_list:
        print("ERROR! - No iban found from scanning, returning most used one!")        
        return company_ibans[0]
    elif len(iban_list) == 1:
        return iban_list[0]
    
    # Standardno pretrazivanje   
    for iban in iban_list:
        if iban in company_ibans:
            return iban
    
    # Ako nije do sad pronadeno
    iban_list = compare_user_iban(iban_list)
    if len(iban_list) >= 1:
        iban = iban_list[0]
    else: 
        iban = company_ibans[0]
            
    return iban       
   
# POŠTANSKI BROJ ###########################
def get_pc_dict():
    try:
        with open('postal_codes.json', 'r') as fp:
            data = json.load(fp)        
    except FileNotFoundError:
        data = None
        
    return data
               
def check_pc_dict(p_codes):
    pc_dict = get_pc_dict()
    
    result = None 
    # try/catch zbog mogucih junk podataka
    for pc in p_codes:
        try:
            result = pc_dict[pc]
            break
        except KeyError:
            continue
    
    return result

def check_user_pc(p_codes):
    with open('current_user.json', 'r') as fp:
        user = json.load(fp)   
    
    aliases = user['alias']
    alias_codes = [alias['postal_code'] for alias in aliases]

    for index, p_code in enumerate(p_codes):
        if p_code in alias_codes:
            p_codes.pop(index)
            break
    
    return p_codes

def check_postal_code(p_codes):
    p_codes = [str(pc) for pc in p_codes]
    
    if len(p_codes) > 1:
        p_codes = check_user_pc(p_codes)
    
    return check_pc_dict(p_codes)
    

# TEST
def test_update_iban(test_company):
    update_company_iban('HR012345678519', test_company)
    
def test_check_iban(test_company):
    test_iban = ['HR012345678512', 'HR012322678912', 'HR123456789012']
    print("IBAN:", check_iban(test_iban, test_company))   

def test_check_postal_code():
    p_codes = [10110, 51304]
    print(check_postal_code(p_codes))
     
if __name__ == "__main__":
    test_company = db.get_company(db.connect_to_db(), '16962783514')
    
    #test_update_iban(test_company)
    #test_check_iban(test_company)
    
    #test_check_postal_code()