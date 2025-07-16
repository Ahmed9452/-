print("           the main page")
print("hello")
name = input("Please Enter your name : \n ").lower()
pass_user = input("Please Enter anew password : \n ").upper()

print("  ")
print ( "                   login")
name2 = input("Please Enter your name : \n ").lower()
old_pass = input("Please Enter your old password : \n ").upper()
if old_pass == pass_user and name == name2:
    print("Welcome " + name)
else :
  print ("error password or name")
