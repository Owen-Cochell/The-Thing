#This file is where all code will be executed
import time
import os
from animate import *
import itertools
import threading
import sys
os.system("color 0a")
path= 'system path here'
logf=open(path, "w")
logstart(logf)
logf=open(path, "a")
logf.write("#######################################################################")
logf.write("\n                            <BEGIN_LOG>                             ")
logf.close()
#Code for passwords here
suc='#Success!'
authe=False
interm=False
on=True
norm=True
lockconf=False
lockpass='test123'
log=True
temp=20
corrupt=False
#Code for frequency here
freq='2500'
#Code for emergency overide code here
logpass='test'
emover='0x5567'
tec='Windows'
pio='Mcrege'
wep='Gary'
bio='Blair'
tecp='test'
piop='test'
wepp='test'
biop='test'
tecpl='test'
piopl='test'
weppl='test'
biopl='test'

optiony = ('Y', 'y', 'Yes', 'yes', 'Ye', 'ye')
optionn = ('N', 'n', 'No', 'no')

while on==True:
    #Boot up procedure
    if log==True:
        logf=open(path, "a")
        logf.write("\n#SYSTEM: Starting boot procedures...")
        logf.write("\n#SYSTEM: Boot procedure complete!")
        logf.close()
    clear()
    boot(suc, corrupt)
    #Check to see which version to boot
    while norm==False:
        while lockconf==True:
            if log==True:
                logf=open(path, "a")
                logf.write("\n#SYSTEM.WARNING: LOG COLLECTION TEMPORARILY DISABLED DUE TO SECURITY PROTOCALS!")
                logf.close()
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
        while corrupt==True:
            clear()
            syscorp()
            corpinp=input("\nPlease enter emergency overide code:")
            if corpinp==emover:
                print("Rebooting and logging into '{}' account...".format(tec))
                time.sleep(1)
                norm=True
                usern=tec
                authe=True
                interm=True
                if log==True:
                    logf=open(path, "a")
                    logf.write("\n#SYSTEM.ERROR: ERRORS DETECTED! Booting to FAILSAFE_PARTITION....")
                    logf.write("\n#SYSTEM: Booted to FAILSAFE_PARTITION!")
                    logf.write("\n#TYPE: {}".format(corpinp))
                    logf.write("\n#SYSTEM: Authenticating...")
                    logf.write("\n#SYSTEM: Authenticated!")
                    logf.write("\n#SYSTEM: Loggining into tec...")
                    logf.write("\n#SYSTEM: Logged into tec!")
                    logf.close()
                break
            else:
                clear()
                print("ERROR:\n#INCORRECT CODE")
                x=input("Press any key to continue...")
                continue
                
                
    while norm==True:    
        #Usernames and passwords
        while authe==False:
            if log==True:
                logf=open(path, "a")
                logf.write("\n#SYSTEM: Loading Login_Screen...")
                logf.write("\n#SYSTEM: Loaded Login_screen!")
                logf.close()
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
            if authe==False:
                if log==True:
                    logf=open(path, "a")
                    logf.write("\n#TYPE: {}".format(usern))
                    logf.write("\n#TYPE: {}".format(passw))
                    logf.write("\n#SYSTEM.ERROR: Incorrect login credentials!")
                    logf.close()
                clear()
                print("Error: \n#Incorect Username/Password!")
                x=input("Press any key to continue...")
                continue
            if authe==True:
                if log==True:
                    logf=open(path, "a")
                    logf.write("\n#TYPE: {}".format(usern))
                    logf.write("\n#TYPE: {}".format(passw))
                    logf.write("\n#SYSTEM: Credentials accepted!")
                    logf.write("\n#SYSTEM: Setting user to --> {}".format(usern))
                    logf.write("\n#SYSTEM: Starting loggin procedure...")
                    logf.write("\n#SYSTEM: Login procedure complete!")
                    logf.close()
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
            if log==True:
                logf=open(path, "a")
                logf.write("\n#USER.{}.TYPE: {}".format(usern, inp))
                logf.close
            if inp=='help':
                if logf==True:
                    logf=open(path, "a")
                    logf.write("\n#SYSTEM: Loading help_menu...")
                    logf.write("\n#SYSTEM: Loaded help_menu!")
                    logf.close
                help(usern, wep, pio, bio, tec)
                continue
            if inp=='logout':
                if corrupt==True:
                    if log==True:
                        logf=open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: 'LOGOUT.SH' not found :(")
                        logf.close()
                    corp()
                    continue
                if log==True:
                    logf=open(path, "a")
                    logf.write("#SYSTEM: Logging out...")
                    logf.write("#SYSTEM: Setting user to --> NULL")
                    logf.write("#SYSTEM: Loading login_screen...")
                    logf.write("#SYSTEM: Loaded login_screen!")
                    logf.close()
                print("Starting 'LOGOUT.SH(C:/SYS/ACCOUNT)'...")
                time.sleep(1)
                interm=False
                authe=False
                clear()
                logout(suc)
                continue
            if inp=='music':
                if corrupt==True:
                    if log==True:
                        logf=open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: 'MUSIC.SH' not found :(")
                        logf.close()
                    corp()
                    continue
                if log==True:
                    logf=open(path, "a")
                    logf.write("\n#SYSTEM: Loading 'MUSIC.SH'...")
                    logf.write("\n#SYSTEM: Loaded 'MUSIC.SH'!")
                    logf.write("\n#SYSTEM.WARNING: 'MUSIC.SH' dose not support log collection. Any input/system event will NOT be recorded!")
                    logf.close()
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
                if corrupt==True:
                    if log==True:
                        logf=open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: 'FILE.SH' not found :(")
                        logf.close()
                    corp()
                    continue
                if log==True:
                    logf=open(path, "a")
                    logf.write("\n#SYSTEM: Loading 'FILE.SH'...")
                    logf.write("\n#SYSTEM: Loaded 'FILE.SH'!")
                    logf.write("\n#SYSTEM.WARNING: Log collection disbled by administrator on 'FILE.SH'.")
                    logf.write("\n#SYSTEM.MESSAGE: This will keep people out of my damn files!")
                    logf.close()
                print("Starting 'FILE.SH(C:/SYS/FILEMAN)'...")
                time.sleep(1)
                clear()
                files(suc)
                clear()
                file(bio, wep, pio, tec, biop, wepp, piop, tecp, biopl, weppl, piopl, tecpl, logpass, emover, freq)
                print("No files yet at this time")
                fileinp=("Please enter a file number here:")
                continue
            if inp=='radio':
                if corrupt==True:
                    if log==True:
                        logf=open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: 'RADIO.SH' not found :(")
                        logf.close()
                    corp()
                    continue
                if log==True:
                    logf=open(path, "a")
                    logf.write("\n#SYSTEM: Loading 'RADIO.SH'...")
                    logf.write("\n#SYSTEM: Loaded 'RADIO.SH'!")
                    logf.close()
                print("This feature is under development")
                print("Starting 'RADIO.SH(C:/SYS/RADIO/)'...")
                time.sleep(1)
                clear()
                radios(suc)
                clear()
                radio(freq, optiony, optionn, log, usern, path)
                continue
            if inp=='info':
                if log==True:
                    logf=open(path, "a")
                    logf.write("\n#SYSTEM: Displaying account_info.")
                    logf.close()
                print("This feature is under development.")
                uinfo(usern, logg, tec, bio, pio, wep)
                continue
            if inp=='clear':
                if log==True:
                    logf=open(path, "a")
                    logf.write("\n#SYSTEM: Clearing screen...")
                    logf.close
                clear()
                continue
            if inp=='lockdown':
                if usern==wep:
                    if log==True:
                        logf=open(path, "a")
                        logf.write("\n#SYSTEM: Displaying LOCKDOWN_HELP")
                        logf.close()
                    lockinfo()
                    continue
                else:
                    if log==True:
                        logf=open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: {} is not a valid command!".format(inp))
                        logf.close()
                    terror(inp, log, path)
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
                    if lockconfd in optionn:
                        lockconf=False
                        if log==True:
                            logf=open(path, "a")
                            logf.write("\n#SYSTEM: Displaying lockdown_config")
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, lockpass))
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, lockconfd))
                            logf.close()
                    if lockconf==True:
                        print("Starting 'LOCKDOWN.SH(C:/SYS/SECURITY)'...")
                        time.sleep(1)
                        clear()
                        lockint(suc)
                        norm=False
                        interm=False
                        auth=False
                        if log==True:
                            logf=open(path, "a")
                            logf.write("\n#SYSTEM: Displaying lockdown_config")
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, lockpass))
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, lockconfd))
                            logf.write("\n#SYSTEM: Starting 'LOCKDOWN.SH'...")
                            logf.write("Rebooting...")
                            logf.close()
                        continue
                    if lockconf==False:
                        continue
                else:
                    terror(inp, log)
                continue
            if inp=='GENOME_MATCHER':
                if usern==bio:
                    print("Starting 'GENOME_MATCHER.SH(C:/USR/{}/GM)'...".format(bio))
                    time.sleep(1)
                    GMS()
                    print("\nAre you sure you want to run this script?")
                    gminp=input("(Y/N):")
                    if gminp in optiony:
                        print("\nContinuing startup...")
                        time.sleep(1)
                        GMB()
                        GM()
                        authe=False
                        norm=False
                        corrupt=True
                        interm=False
                        if log==True:
                            logf=open(path, "a")
                            logf.write("\n#SYSTEM: Starting GENOME_MATCHER.SH...")
                            logf.write("\n#SYSTEM.WARNING: FILE(GENOME_MATCHER.SH) HAS FAILED INTEGRETY CHECK!")
                            logf.write("\n#SYSTEM.WARNING: RUNNING THIS FILE IS NOT RECOMMENDED!")
                            logf.write("\n#SYSTEM.WARNING: Displaying warning message...")
                            logf.write("\n#USER.{}.TYPE: y".format(usern))
                            logf.write("\n#SYSTEM: Ignoring unstable files...")
                            logf.write("\n#SYSTEM: Starting GENOME_MATCHER.sh...")
                            logf.write("\n#SYSTEM.ERROR: BAD_VARIABLE")
                            logf.write("\n#SYSTEM.ERROR: BAD_VARIABLE")
                            logf.write("\n#SYSTEM.ERROR: BAD_VARIABLE")
                            logf.write("\n#SYSTEM: (Surpressing identical messages)")
                            logf.write("\n#SYSTEM.WARNING: SYSTEM_FAILSAFE ACTIVATED!")
                            logf.write("\n#SYSTEM.WARNING: Restarting...")
                            logf.close()
                        continue
                    if gminp in optionn:
                        print("Exiting...")
                        if log==True:
                            logf=open(path, "a")
                            logf.write("\n#SYSTEM: Starting GENOME_MATCHER.SH...")
                            logf.write("\n#SYSTEM.WARNING: FILE(GENOME_MATCHER.SH) HAS FAILED INTEGRETY CHECK!")
                            logf.write("\n#SYSTEM.WARNING: RUNNING THIS FILE IS NOT RECOMMENDED!")
                            logf.write("\n#SYSTEM.WARNING: Displaying warning message...")
                            logf.write("\n#USER.{}.TYPE: n".format(usern))
                            logf.write("\n#SYSTEM: Canceling...")
                            logf.close()
                        continue
                else:
                    terror(inp, log, path)
            if inp=='syscheck':
                if usern==tec:
                    print("Are you sure you want to run a system integrety check?\n(THIS WILL TAKE A LONG TIME!)")
                    checkinp=input("\n(Y/N):")
                    if checkinp in optiony:
                        print("Starting 'SYSCHECK.SH(C:/SYS/TOOLS/SYSCHECK)'...")
                        syss()
                        syscheck()
                        norm=True
                        authe=False
                        interm=False
                        corrupt=False
                        if log==True:
                            logf=open(path, "a")
                            logf.write("\n#SYSTEM: Starting SYSCHECK.sh...")
                            logf.write("\n#SYSTEM: Started SYSCHECK.sh!")
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, checkinp))
                            logf.write("\n#SYSTEM: Handing all services to 'SYSCHECK.SH'...")
                            logf.write("\n#SYSTEM: Released system to 'SYSCHECK.sh'!(logg collection might be disabled for a short while)")
                            logf.write("\n#SYSTEM: Rebooting...")
                            logf.close()
                    if checkinp in optionn:
                        if log==True:
                            logf=open(path, "a")
                            logf.write("\n#SYSTEM: Starting SYSCHECK.sh...")
                            logf.write("\n#SYSTEM: Started SYSCHECK.sh!")
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, checkinp))
                            logf.write("\n#SYSTEM: Canceling...")
                            logf.close()
                        continue
                else:
                    terror(inp, log, path)
                    continue
            if inp=='log':
                if usern==tec:
                    loggh()
                else:
                    terror(inp, log, path)
                    continue
            if inp=='log_enable':
                if usern==tec:
                    if log==True:
                        logf=open(path, "a")
                        logf.write("\n#SYSTEM: Enabling log collection...")
                        logf.write("\n#SYSTEM: Log collection enabled!")
                        logf.close()
                    print("LOG COLLECTION ENABLED!")
                    log=True
                    continue
                else:
                    terror(inp, log, path)
                    continue
            if inp=='log_disable':
                if usern==tec:
                    if log==True:
                        logf=open(path, "a")
                        logf.write("\n#SYSTEM: Disabling log collection...")
                        logf.write("\n#SYSTEM: Log collection disabled!")
                        logf.close()
                    print("LOG COLLECTION DISABLED!")
                    log=False
                    continue
                else:
                    terror(inp, log, path)
                    continue
            #ALL CODE BELOW IS UNFINISHED. MAY BE CHANGED IN THE FUTURE.
            #if inp=='fridge_config':
                #print("This feature is not yet implemented.")
                #print("Starting 'FRIDGE_CONFIG.SH(C:\SYS\UTIL')...")
                #fridges()
                #clear()
                #fridges()
                #finp=input("Please enter a number:")
                #if finp=='1':
                    #fridgetemp(temp)
                    #tempinp=input("Please enter a temperature(or enter 'no' to keep current temperature):")
                    #var1="Saving settings..."
                    #ltime=30
                    #end=False
                    #lpass=False
                    #load(var1, suc, ltime, end, lpass)
                    #time.sleep(3)
                    #print("Complete. Temperature set to:\n{} degress".format(temp))
                    #temp=tempinp
                    #if int(temp)>=30:
                        #print("ATTENTION:\nAll food will spoil in 1 cycle if you don't change the temperature.")
                        #x=input("Press any key to continue...")
                    #if int(temp)<30:
                        #print("ATTENTION:\nAny living creatures inside will DIE in 1 cycle")
                continue
            else:
                terror(inp, log)
                continue
                  
            
    
