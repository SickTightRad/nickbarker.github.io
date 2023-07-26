#This is a comment

star = '*****'

print(star + " Welcome to the Funky Buncher " + star)
#print("WELCOME TO THE FUNKY BUNCHER!")

username = input("enter your name here :")

if username == "Marky Mark" or  " Marky Mark":
    print("Ah yes, Marcus, I shall name you:" )
    username = "Marky Mark and the Funky Bunch!"
    print(username)
else:
    print("Username is: " + username)