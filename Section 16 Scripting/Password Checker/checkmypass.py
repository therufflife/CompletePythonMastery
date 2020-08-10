import requests
import hashlib          #able to do SHA1 hashing with built-in lib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:      # if there is a match, return the number of times it was found
            return count
    return 0            # if nothing has been matched, return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()   # password encryption to SHA1
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'"{password}" was found {count} times; you should probably change your password.')
        else:
            print(f'"{password}" was NOT found. Easy money baby.')
    return 'All done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))