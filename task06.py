usernames = 'ali:12345, vali:43144, sami:432, gani:89534'

def authenticate(username: str, password: str) -> bool:
    pairs = usernames.split(',')
    for pair in pairs:
        user, a = pair.split(':')
        if username == user and password == a:
            return True
    return False

def login(username: str, password: str) -> bool:
    return authenticate(username, password)

