from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 


#master_pwd = input("What is the master password? " )
key = load_key() #+ master_pwd.encode()
fer = Fernet(key)


#key + password + text to encrypt = random text 
#random text + key + password = text to encrypt

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
write_key() # comment after first usage if you want.'''

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # "hello|tim|yes|2" -> ["hello", "tim", "yes", "2"]
            print("User:", user, "| Password: ", fer.decrypt(passw.encode()).decode())
    
    
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("password.txt", "a") as f: #'with' automatically open AND close the file... 'a'-> append to file / create new file if it doesn't exist...
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    
    
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? [q to quit] ")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    
    elif mode == "add":
        add()
    
    else:
        print("Invalid mode.")
        continue 