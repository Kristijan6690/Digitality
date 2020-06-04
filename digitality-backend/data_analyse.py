import mongodb as db

# IBAN ##########################################
# UPDATE ###############
def compare_possible_ibans(iban, company_data):
    try:
        #Pokusamo dohvatiti atribut 'possible_ibans' iz rijecnika koji sadrzi podatke izdavacu te postavimo
        #   ukoliko ne uspijemo, tj. taj atribut ne postoji, izvrsava se exception
        possible_ibans = company_data['possible_ibans']
        boundary = 5 #Koliko se puta mora iban pojaviti da bi se validirao
        upgrade_index = -1 #Ako je boundary dosegnut validiramo iban na indexu kojeg spremamo u ovu varijablu
        is_found = False
        
        #Provjervamo ako se proslijeđeni iban nalazi u polju mogućih iban-a
        #   ako se nalazi njegova ucestalost se povecava za +1 te se provjerava upgrade_index 
        for index, cur_iban in enumerate(possible_ibans):
            if cur_iban[1] == iban: 
                cur_iban[0] += 1
                
                if cur_iban[0] >= boundary:
                    upgrade_index = index
                else:
                    possible_ibans[index] = cur_iban
                    
                break
        
        #Ako iban nije pronađen, dodajemo ga u listu mogucih ibana
        if not is_found:
            new_iban = [1, iban]
            company_data['possible_ibans'].append(new_iban)
            
        #Ukoliko je boundary zadovoljen premjestamo taj iban iz 'possible_ibans' u 'iban'
        if upgrade_index >= 0:
            new_iban = possible_ibans.pop(upgrade_index)
            company_data['iban'].append(new_iban)
    except:
        company_data['possible_ibans'] = [] #Ako ne postoji taj atribut u trenutnom dictionary-u stvaramo ga kao praznu listu
        
        #U tu praznu listu dodajemo novi element sa brojem ucestalosti postavljenim na 1
        new_iban = [1, iban] 
        company_data['possible_ibans'].append(new_iban)
            
    return company_data   
                   
def update_company_iban(iban, company_data):
    company_ibans = company_data['iban']
    is_found = False
    
    #Provjeravamo ako se iban nalazi u listi, te ako se nalazi njegovu ucestalost povecavamo za +1
    for index, cur_iban in enumerate(company_ibans):
        if cur_iban[1] == iban:
            cur_iban[0] += 1
            company_ibans[index] = cur_iban
            
            is_found = True    
            break
    
    #Ako se ne nalazi u listi, provjeravamo u listi mogucih ibana
    #   moguci ibani su oni ibani koji su se pojavili nedovoljno puta da bi se mogli smatrati vazecim 
    if not is_found:
        company_data = compare_possible_ibans(iban, company_data)

    #Pokusavamo sortirati listu ibana po broju ucestalosti, ako jedan od ibana nije pravilnog formata dolazi do greske i polje se ne sortira
    try:
        company_ibans = sorted(company_ibans, key = lambda sub_list: sub_list[0])
    except:
        print("List of iban numbers contains an element that is not a sub list and can not be sorted!")
    
    #Sa novo obradenim podacima updateamo izdavaca racuna na bazi
    db.update_company(company_data)
    
    return company_ibans

# CHECK ################
#Funkcija izbacuje iz liste iban trenutnog korisnika
def compare_user_iban(iban_list):
    # TEST DATA #################################
    user = {
        '_id': '1',
        'email': 'john@smith.com',
        'personal_arhive': '7',
        'archive_ids': ['7', '8'],
        'alias': [
            {
                'ime': 'John',
                'prezime': 'Smith',
                'oib': '12345678901',
                'iban': 'HR123456789012',
                'postal_code': '10000',
            },
            {
                'ime': 'Jane',
                'prezime': 'Smith',
                'oib': '10987654321',
                'iban': 'HR210987654321',
                'postal_code': '10000',
            }
        ], 
    }
    #############################################
    
    aliases = user['alias']
    
    for index, iban in enumerate(iban_list):
        found = False
        
        for alias in aliases:
            if iban == alias['iban']:
                found = True
                break #Break iz nested loop-a
        
        if found:
            iban_list.pop(index)
            break #Break iz glavnog loop-a
    
    return iban_list    

#Funkcija kao argumente prima listu ibana koji su se pronasli na slici te dobiva podatke o izdavacu racuna
def check_iban(iban_list, company_data):
    company_ibans = company_data['iban']

    if not iban_list:
        print("ERROR! - No iban found from scanning, returning most used one!")        
        return company_ibans[0][1]
    elif len(iban_list) == 1:
        return iban_list[0]
    
    iban = None
    is_found = False
    for u_iban in iban_list:
        for c_iban in company_ibans:
            if u_iban == c_iban[1]:
                is_found = True
                iban = u_iban[1]
                break
        break
    
    if not is_found:
        iban_list = compare_user_iban(iban_list)

        n_iban = len(iban_list)
        if n_iban >= 1:
            iban = iban_list[0][1]
        else: 
            iban = company_ibans[0][1]
            
    return iban       

    
# PC - POŠTANSKI BROJ ###########################
def check_user_pc(pc_nums):
    # TEST DATA #################################
    user = {
        '_id': '1',
        'email': 'john@smith.com',
        'personal_arhive': '7',
        'archive_ids': ['7', '8'],
        'alias': [
            {
                'ime': 'John',
                'prezime': 'Smith',
                'oib': '12345678901',
                'iban': 'HR123456789012',
                'postal_code': '10000',
            },
            {
                'ime': 'Jane',
                'prezime': 'Smith',
                'oib': '10987654321',
                'iban': 'HR210987654321',
                'postal_code': '10000',
            }
        ], 
    }
    #############################################
    
    #Dohvacamo aliase od korisnika te ih spremamo u zasebnu varijablu
    aliases = user['alias']

    #Iako je kompleksnost ovog koda n^2 nece biti vise od 20 usporedba pa zbog toga kod nece biti pre spor
    #Zelimo ukloniti sto vise postanskih brojeva koje cemo traziti u rijecniku da da bude sto veca vjerovatnost da je to 
    #   postanski broj sa kojeg je poslan racun, tj da je to mjesto izdavanja. Zbog toga iz polja izbacujemo postanski broj
    #   korisnika koji ce se takoder nalaziti na racunu.
    for pc in pc_nums:
        found = False
        
        for index, alias in enumerate(aliases):
            if pc == alias['postal_code']:
                found = True
                break
        
        if found:
            pc_nums.pop(index)
            break
    
    return pc_nums
               
def check_pc_dict(pc_nums):
    #Dohvati rijecnik postanskih brojeva sa baze
    pc_dict = db.get_pc_dict()
    
    #Ukoliko postanski broj nije naden u rijecniku(npr. nije pravilno skeniran sa racuna) funkcija ce vratiti None
    result = None
    
    #U slucaju da su se provukli jos neki podaci, prolazimo kroz njih sve
    #   posto postanski brojevi u RH nisu sekvencijalni(npr 10000-10001 vec 10000-10010)  velika je vjerovatnost 
    #   da se ti junk podaci nece pronaci u rijecniu sto ce izazvati gresku koju moramo obraditi na nacin da taj 
    #   broj jednostavno preskocimo u petlji
    for pc in pc_nums:
        try:
            result = pc_dict[pc]
            break
        except KeyError:
            continue
    
    return result

def check_postal_code(pc_nums):
    #Pretvaramo postanske brojeve u stringove da bi ih mogli pronaci u rijecniku
    pc_nums = [str(pc) for pc in pc_nums]
    
    #Ukoliko je samo jedan pc u listi(u slucaju da je racun poslan iz istog mjesta gdje se nalazi primatelj)
    #   ne zelimo izbaciti taj broj pa preskacemo ovaj korak
    if len(pc_nums) > 1:
        pc_nums = check_user_pc(pc_nums)
    
    #Mjesto izdavanja trazimo u rjecniku koji sadrzi sve postanske brojeve iz RH 
    place = check_pc_dict(pc_nums)
    
    return place 


if __name__ == "__main__":
    
    pc_nums = [10110, 51304]
    
    place = check_postal_code(pc_nums)
    print(place)
    
    """
    test_company = {
        '_id': '4',
        'naziv': 'Company A',
        'oib': '16962783514',

        'usluga': 'Internet', 
        'iban': [[1, 'HR012329678912'], [2, 'HR012345678512'], [3, 'HR765456278512']]    
    }
    test_iban = ['HR012345678512', 'HR012322678912', 'HR123456789012']
    
    iban = check_iban(test_iban, test_company)
    print("IBAN:", iban)
    """
