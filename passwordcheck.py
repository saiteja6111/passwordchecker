import requests
import hashlib
def req_api_data(query_char):
    res = requests.get(f'https://api.pwnedpasswords.com/range/{query_char}')
    if res.status_code != 200:
        print(f'Api doesnot exists : {res.status_code}, \ncheck the api and try again!!!')
    return res

def passwords_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        print(h, count)



def pewend_api_check(password):
    m = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    frist5_char = m[:5] 
    tail = m[5:]
    response = req_api_data(frist5_char)
    print(response)
    return passwords_leaks(frist5_char, tail)

# print(req_api_data('21BD1'))

pewend_api_check('123')




