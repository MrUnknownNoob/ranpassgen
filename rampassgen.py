print('''
 _    _  ____        _   _  _   _  _   _  _   _   ___   _   _  _   _ 
| \  / ||  _ \      | | | || \ | || | | || \ | | / _ \ | | | || \ | |
|  \/  || |_| |     | | | ||  \| || |/ / |  \| || | | || |_| ||  \| |
|      ||    /      | | | || |\  ||   /  | |\  || | | || / \ || |\  |
| |\/| || |\ \      | | | || | | ||   \  | | | || | | ||  _  || | | |
| |  | || | | | _   | |_| || | | || |\ \ | | | || |_| || / \ || | | |
|_|  |_||_| |_||_|   \___/ |_| |_||_| |_||_| |_| \___/ |/   \||_| |_|
****** Tool Name ::This Tool Is Random Password Genarator ******
       Why This tool :: This tool Is Made for Random Password Genarator. You can Use This Password. It is Safe.
       Contact with Me :


''')

print( '''
01. Random Password Genarator Type Only password Length
02. Random Password Genarator Type Only Number
03. Random Password Genarator Type Only password Length
''')

a = int(input("Choose Your Option :"))

if (a == 1):
    import random

    lower  = "abcdefghijklmnopqrstuvwxyz"
    upper  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "!@#$%^&*(),./;'\][<>?:|}{"

    string = lower + upper + number + symbol
    length = int(input("Password Length :"))

    password = "".join(random.sample(string,length))

    print("Your New Password is :", password)


elif (a == 2):
    import random

    a = input("Enter your Some character :")
    b = list(str(a))
    random.shuffle(b)
    print(''.join(b))



elif(a == 3):
    import random
    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,./;'\][<>?:|{}!@#$%^&*()_+=-"
    passlen = int(input("Enter the Length of the password::"))
    a = "".join(random.sample(password,passlen))
    print("Your Password is:",a)


else:
    print("Syntax Error")
