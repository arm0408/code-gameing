import hashlib
import json
# import menu
import ChooseGame
from unicodedata import name
def Register():
    usn = input("Enter Username: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("user.json", "r") as f:
            user_data = json.load(f)
            for i in range(len(user_data)) :
                if user_data[i]['name'] == usn:
                    print('Register failed try again!')
                    Register()
                    break
            else:
                data = {'name' : usn, 'pass' : hash1 }
                user_data.append(data)
                with open("user.json", "w") as f:
                    json.dump(user_data, f, indent=4)
        f.close() 
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")

def login():
    usn = input("Enter Username: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("user.json", "r") as f:
        dict = json.load(f)
        for i in range(len(dict)) : 
            if usn == dict[i]['name'] : 
                if auth_hash == dict[i]['pass'] :
                    print("Login success!!!")
                    print("================================================================================")
                    return usn
        else:
            print("Login failed, Please Try again")
    f.close()
    
def Register_main():
    while 1:
        print("\t\t********** Login System **********")
        print("1.Register")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            Register()
        elif ch == 2:
            global user_name
            user_name = login()
            if user_name == None:
                continue
            else:
                ChooseGame.playgame()
        elif ch == 3:
            break
        else:
            print("Wrong Choice!")

    