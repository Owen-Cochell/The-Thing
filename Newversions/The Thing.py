#This file is where all code will be executed
import time
import os
from animate import *
import itertools
import threading
import sys
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
#Code for frequency here
tec='Windows'
pio='Mcrege'
wep='Gary'
bio='Blair'
optiony = ('Y', 'y', 'Yes', 'yes', 'Ye', 'ye')
optionn = ('N', 'n', 'No', 'no')

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
                lockconf2=input("(Y/N):")
                if lockconf2 in optiony:
                    print("Starting 'LOCKDOWN_DIS.SH(C:/SYS/SECURITY')...")
                    time.sleep(1)
                    clear()
                    lockdis(suc)
                    norm=True
                    lockconf=False
                    lockpass='test123'
                    authe=False
                    continue
                if lockconf2 in optionn:
                    continue
            if lockinp==wepp:
                lockconf2()
                lockconf2==input("(Y/N):")
                if lockconf2 in optiony:
                    print("Starting 'LOCKDOWN_DIS.SH(C:/SYS/SECURITY')...")
                    time.sleep(1)
                    clear()
                    lockdis(suc)
                    norm=True
                    lockconf=False
                    lockpass='test123'
                    continue
                if lockconf2 in optionn:
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
            if usern==tec and passw==tecp:
                authe=True
            if usern==pio and passw==piop:
                authe=True
            if usern==wep and passw==wepp:
                authe=True
            if usern==bio and passw==biop:
                authe=True
            else:
                authe=False
            if authe==False:
                clear()
                print("Error: \n#Incorect Username/Password!")
                x=input("Press any key to continue...")
                continue
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
                musics(suc, tec)
                clear()
                music(tec, bio, pio, wep)
                musicinp=input("Please select a number:")
                if musicinp=='1':
                    clear()
                    tecmus(tec)
                    continue
                if musicinp=='2':
                    clear()
                    biomus(bio)
                    continue
                if musicinp=='3':
                    clear()
                    piomus(pio)
                    continue
                if musicinp=='4':
                    clear()
                    wepmus(wep)
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
                print("This feature is under development")
                print("Starting 'RADIO.SH(C:/SYS/RADIO/)'...")
                time.sleep(1)
                clear()
                radios(suc)
                clear()
                radio(freq, optiony, optionn)
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
                    lockpass=input("Password:")
                    print("\nAre you sure?")
                    lockconfd=input("(Y/N):")
                    if lockconfd in optiony:
                        lockconf=True
                        return lockconf, lockpass
                    if lockconfd in optionn:
                        lockconf=False
                        return lockconf
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
                continue
            if inp=='fridge_config':
                print("This feature is not yet implemented.")
                continue
            else:
                terror(inp)
                  
            
    
