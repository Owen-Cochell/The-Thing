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
lockconf=False
lockpass='test123'
logg=False
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
    while norm==False:
        while lockconf==True:
            clear()
            lockout()
            lockinp=input("Please enter password or security overide code:")
            if lockinp==lockpass:
                lockconf2()
                lockconf2==input("(Y/N):")
                if lockconf2 in ('Y', 'y', 'yes'):
                    print("Starting 'LOCKDOWN_DIS.SH(C:/SYS/SECURITY')...")
                    time.sleep(1)
                    clear()
                    lockdis(suc)
                    norm=True
                    lockconf=False
                    lockpass='test123'
                    continue
                if lockconf2 in ('N', 'n', 'no'):
                    continue
            if lockinp==wepp:
                lockconf2()
                lockconf2==input("(Y/N):")
                if lockconf2=='Y' or 'y' or 'yes':
                    print("Starting 'LOCKDOWN_DIS.SH(C:/SYS/SECURITY')...")
                    time.sleep(1)
                    clear()
                    lockdis(suc)
                    norm=True
                    lockconf=False
                    lockpass='test123'
                    continue
                if lockcon2=='N' or 'n' or 'no':
                    continue
            else:
                clear()
                lerror(lockinp)
                continue
                
    while norm==True:    
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
            inp=input("C:/Users/%s>>>" % usern)
            if inp=='help':
                help(usern, wep, pio, bio, tec)
                continue
            if inp=='logout':
                print("Starting 'LOGOUT.SH(C:/SYS/ACCOUNT)'...")
                time.sleep(1)
                interm=False
                authe=False
                clear()
                logout(suc)
                continue
            if inp=='music':
                print("Starting 'MUSIC.SH(C:/USR/WINDOWS)'")
                time.sleep(1)
                clear()
                musics(suc)
                clear()
                music()
                musicinp=input("Please select a number:")
                if musicinp==1:
                    clear()
                    tecmus(tec)
                    continue
                if musicinp==2:
                    clear()
                    biomus(bio)
                    continue
            if inp=='file':
                print("Starting 'FILE.SH(C:/SYS/FILEMAN)'...")
                time.sleep(1)
                clear()
                files(suc)
                clear()
                file()
                print("No files yet at this time")
                fileinp=("Please enter a file number here:")
                continue
            if inp=='radio':
                print("This feature is not yet implemented.")
                continue
            if inp=='gen_config':
                print("This feature is not yet implemented.")
                continue
            if inp=='info':
                print("This feature is under development.")
                uinfo(usern, logg, tec, bio, pio, wep)
                continue
            if inp=='clear':
                clear()
                continue
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
                    lockcon(lockpass, lockconf)
                    lockpass=lockcon(lockpass, lockconf)
                    lockconf=lockcon(lockpass, lockconf)
                    if lockconf==True:
                        print("Starting 'LOCKDOWN.SH(C:/SYS/SECURITY)'...")
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
                c   ontinue
            if inp=='fridge_config':
                print("This feature is not yet implemented.")
                continue
            else:
                terror(inp)
                  
            
    
