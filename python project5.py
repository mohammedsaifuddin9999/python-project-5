master_pwd = input("What is the master password? ")

def view():
    with open('password.txt', 'r') as f:
        
def add():
    name = input("Account Mame: ")
    pwd = input("passwod: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new passward or view a existing one or would you like to quit (view/add/q)?")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")


  