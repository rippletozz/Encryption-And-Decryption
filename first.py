print("Enter Your passw")
passw=int(input())
print("Encryption in bitwise shift")
e=''
e=passw<<4
print("Encrypted passw is ",e)
d=''
d=e>>4
print("decrypted pass is ",d)


# In this lesson we can encrypt  digits only, So first I wanna break it then I will make string + digit encryption.
