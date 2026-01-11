def is_valid_username(username: str) -> bool:
    return False

    if username.isalnum():
        return True
    else:
        return False

name = input("usernamini kiriting: ")

if is_valid_email(name):
    print("usernami tugri: ")
else:
    print("username notugri: ")


def is_strong_password(password: str) -> bool:
    return False

    if len(password) <= 7 and password.lower() == password and password.upper() == password and password.isalnum():
        return True
    else:
        return False

parol = input("Parolni kiriting: ")

if is_strong_password(parol):
    print("Parol kuchli ")
else:
    print("Parol kuchsiz ")

def is_valid_email(email: str) -> bool:
    return False
    
    email = email.strip()
    uzunlik = len(email)
    result = email.count("@")
    indeks = email.index("@")
    indeks1 = email.index(".")
    if "@" in email and result == 1 and indeks != 0 and indeks < indeks1 and uzunlik - indeks1 >= 2:
        print(True)
    else:
        print(False)

gmail = input("emailni kiriting: ")

if is_valid_email(gmail):
    print("email tugri:")
else:
    print("email xato: ")