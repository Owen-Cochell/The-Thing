#This file is where all code will be executed
import time
import os
from animate import *
#Code for passwords here
suc='#Success!'
authe=False
interm=False
on=True
norm=True
lockcon=False
lockpass='test123'
temp=20
tec='Windows'
pio='Mcrege'
wep='Gary'
bio='Blair'

while on==True:
    #Boot up procedure
    clear()
    boot(suc)
    #Check to see which version to boot
    if norm==False:
        if lockcon==True:
            clear()
            lockout()
            lockinp=input("Please enter password or security overide code:")
            if lockinp==lockpass:
                p
            if lockinp==wepp:
                p
            else:
                clear()
                lerror(lockinp)
                continue
                
    if norm==True:    
        #Usernames and passwords
        while authe==False:
            clear()
            print("Welcome to Outpost Interface Manager login(ver. 1.73.48)")
            print("Please login:")
            usern=input("Username:")
            passw=input("Password:")
            auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop, usern, passw)
            authe=auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop, usern, passw)
            if authe==False:
                clear()
                print("Error: \n#Incorect username/Password!")
            if authe==True:
                break
    #Login procedure
    clear()
    login(suc)
    interm=True
    #Code for Terminal welcome screen
    clear()
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
            clear()
            logout(suc)
        if inp=='file':
            print("Starting 'FILE.SH(C:\SYS\FILEMAN)'...")
            time.sleep(1)
            clear()
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
            clear()
        if inp=='lockdown':
            if usern==wep:
                lockinfo()
                continue
            else:
                terror(inp)
                continue
        if inp=='lockdown_int':
            print("This feature is currently in development")
            if usern==wep:
                lockcon()
                lockpass=lockcon(lockpass, lockconf)
                lockconf=lockcon(lockpass, lockconf)
                if lockconf==True:
                    print("Starting 'LOCKDOWN.SH(C:\SYS\SECURITY)'...")
                    time.sleep(1)
                    clear()
                    lockint(suc)
                    norm=False
                    interm=False
                    auth=False
                    continue
                if lockconf==False:
                    continue
            else:
                terror(inp)
                continue
        if inp=='lockdown_dis':
            print("This feature is not yet implemented.")
        if inp=='fridge_config':
            print("This feature is not yet implemented.")
        else:
            terror(inp)
                  
            
    
