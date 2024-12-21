import requests
import hashlib
import sys

def req_api_data(query_char):
    res = requests.get(f'https://api.pwnedpasswords.com/range/{query_char}')
    if res.status_code != 200:
        print(f'Api doesnot exists : {res.status_code}, \ncheck the api and try again!!!')
    return res

def passwords_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def main(args):
    for password in args:
        count = pewend_api_check(password)
        if count:
            print(f'{password} was found in {count} times.... you should')
        else:
            print(f'{password} was NOT FOUND. carry on!')
    return 'done'

def pewend_api_check(password):
    m = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    frist5_char , tail= m[:5], m[5:]
    response = req_api_data(frist5_char)
    print(response)
    return passwords_leaks(response, tail)



main(sys.argv[1:])




