import requests
import json

blockfrost = ''

    

#headers
header = {'project_id': blockfrost}
    
#address
address = ''

def get_stake(a):

#addresses
    addy = a
#endpoint
    getstake = 'https://cardano-mainnet.blockfrost.io/api/v0/addresses/'+addy
#call
    r = requests.get(getstake,headers=header)
#parse
    data = json.loads(r.text)
#stake
    stake = data['stake_address']
#return
    return(stake)

def get_concats(stake):

#initialize
    l = []
    x = 0
    page = 1
#pass
    stakeAddress = stake

    for num in range(1,8):
        page = num
#endpoint
        point = 'https://cardano-mainnet.blockfrost.io/api/v0/accounts/'+stakeAddress+'/addresses/assets?page='+str(page)
#call
        r = requests.get(point,headers=header) 
#parse
        data = json.loads(r.text)
#loop
        for d in data:
            l.append(data[x]['unit'])
            x += 1
        x=0
#return
    return(l)


def get_policies(cons):

#initialize
    p = []
#loop
    for i, con in enumerate(cons):
#endpoint
        ep = 'https://cardano-mainnet.blockfrost.io/api/v0/assets/'+con
#call
        r = requests.get(ep,headers=header) 
#parse
        data = json.loads(r.text)
#append
        p.append(data['policy_id'])
#return
    return p

def get_floors(policies):

#initialize
    counter = 0
    price = 0
    n = 0
    floor = 'floor_price'


    for pol in policies:
#endpoint
        oep = 'https://api.opencnft.io/1/policy/'+pol+'/floor_price'
#call    
        r = requests.get(oep)
#parse
        data = json.loads(r.text)
#sum    
        if floor in data.keys():
            print(data['floor_price'])
            price += data['floor_price']
        else:
            n += 1
            
#increment
        counter += 1
#calculate
    price = price/1000000
#print
    print('\n\nTotal NFTs in wallet : '+ str(counter))
    print('\nFloor price evaluation of entire wallet : ' + str(price)+ " ADA \n")
    print('\n n = ' +str(n))
#return
    return("Operation Successful\n")




print(get_floors(get_policies(get_concats(get_stake(a)))))
