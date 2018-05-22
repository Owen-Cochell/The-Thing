#This file is where all code will be executed
import time
from animate import *
#Code for passwords here
suc='#Success!'
authe=False
interm=False
on=True
norm=True
temp=20
tec='Windows'
pio='Mcrege'
wep='Gary'
bio='Blair'

while on==True:
    #Boot up procedure
    boot(suc)
    #Check to see which version to boot
    if norm==True:    
        #Usernames and passwords
        while authe==False:
            print("Welcome to Outpost Interface Manager login(ver. 1.73.48)")
            print("Please login:")
            usern=input("Username:")
            passw=input("Password:")
            auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop, usern, passw)
            authe=auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop, usern, passw)
            if authe==False:
                print("Error: \n#Incorect username/Password!")
            if authe==True:
                break
    #Login procedure
    login(suc)
    interm=True
    #Code for Terminal welcome screen
    startt(usern)
    while interm==True:
        inp=input("C:\Users\%s>>>" % usern)
        if inp=='help':
            help(usern)
        if inp=='logout':
            print("Starting 'LOGOUT.SH(C:\SYS\ACCOUNT)'...")
            time.sleep(1)
            interm=False
            authe=False
            logout(suc)
        if inp=='file':
            print("Starting 'FILE.SH(C:\SYS\FILEMAN)'...")
            time.sleep(1)
            files(suc)
            file()
            print("No files yet at this time")
            fileinp=("Please enter a file number here:")
        if inp=='radio':
            print("This feature is not yet implemented.")
        if inp=='gen_config':
            print("This feature is not yet implemented.")
        if inp=='info':
            print("This feature is not yet implemented.")
        if inp=='clear':
            print("This feature is not yet implemented.")
        if inp=='lockdown':
            print("This feature is not yet implemented.")
        if inp=='lockdown_int':
            print("This feature is not yet implemented.")
        if inp=='lockdown_dis':
            print("This feature is not yet implemented.")
        if inp=='fridge_config':
            print("This feature is not yet implemented.")
        else:
            print("Error:\n#'%s' is not a valid command!" % inp)
                  
            
    
