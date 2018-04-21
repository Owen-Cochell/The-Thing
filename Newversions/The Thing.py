#This file is where all code will be executed
import time
import animate.py as ani
#Code for passwords here
authe=False
interm=True
temp=20
tec='Windows'
pio='Mcrege'
wep='Gary'
bio='Blair'

#Boot up procedure
ani.boot()
#Usernames and passwords
while authe==False:
    print("Welcome to Outpost Interface Manager login(ver. 1.73.48)")
    print("Please login:")
    usern=input("Username:")
    passw=input("Password:")
    ani.auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop)
    if authe==False:
        print("Error: \n #Incorect username/Password!")
    if authe==True:
        break
#Login procedure
ani.login()
#Code for Terminal welcome screen
ani.startt(usern)
while interm==True:
    inp=input("C:\Users\%s>>>")(usern)
    if inp=='help':
        ani.help(usern)
    if inp=='logout':
        print("Starting 'LOGOUT.SH(C:\SYS\ACCOUNT)'...")
        ani.logout()

    