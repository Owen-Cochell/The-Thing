#This file is where all code will be executed
import time
import animate.py as ani
#Code for passwords here
authe=False
interm=True
on=True
norm=True
temp=20
tec='Windows'
pio='Mcrege'
wep='Gary'
bio='Blair'

while on==True:
#Boot up procedure
boot()
#Check to see which version to boot
    if norm==True:    
    #Usernames and passwords
    while authe==False:
        print("Welcome to Outpost Interface Manager login(ver. 1.73.48)")
        print("Please login:")
        usern=input("Username:")
        passw=input("Password:")
        auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop)
        if authe==False:
            print("Error: \n #Incorect username/Password!")
        if authe==True:
            break
    #Login procedure
    login()
    #Code for Terminal welcome screen
    startt(usern)
    while interm==True:
        inp=input("C:\Users\%s>>>")(usern)
        if inp=='help':
            help(usern)
        if inp=='logout':
            print("Starting 'LOGOUT.SH(C:\SYS\ACCOUNT)'...")
            logout()
    
    
