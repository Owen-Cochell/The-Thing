#This file is where all code will be executed
import time
import os
from animate import *
import itertools
import threading
import sys
import winsound
os.system("color 0a")
os.chdir("resources")
path = 'SYS_LOG.txt'
logstart(path)
logf = open(path, "a")
logf.write("#######################################################################")
logf.write("\n                         <BEGIN_LOG>                             ")
logf.write("\n#SYSTEM.WARNING: Log collection is disabled!")
logf.close()
# Code for passwords here
suc = '#Success!'
authe = False
interm = False
on = True
norm = True
lockconf = False
lockpass = 'test123'
log = False
corrupt = False
# Code for frequency here
freq = '2500'
# Code for emergency override code here
logpass = 'test'
emover = '0x5567'
tec = 'tec'
pio = 'pio'
wep = 'wep'
bio = 'bio'
tecp = 'test'
piop = 'test'
wepp = 'test'
biop = 'test'

optiony = ('Y', 'y', 'Yes', 'yes', 'Ye', 'ye')
optionn = ('N', 'n', 'No', 'no')

print(os.getcwd())
x = input("Press enter to start the game!")
clear()

while on:
    # Boot up procedure

    if log:
        logf = open(path, "a")
        logf.write("\n#SYSTEM: Starting boot procedures...")
        logf.write("\n#SYSTEM: Boot procedure complete!")
        logf.close()

    clear()
    boot(suc, corrupt)
    # Check to see which version to boot

    while not norm:

        while lockconf:

            if log:

                logf = open(path, "a")
                logf.write("\n#SYSTEM.WARNING: LOG COLLECTION TEMPORARILY DISABLED DUE TO SECURITY PROTOCOLS!")
                logf.close()

            clear()
            lockout()
            lockinp = input("Please enter password or security override code:")

            if lockinp == lockpass:

                lockconf2()
                lockconf2 = input("(Y/N):")

                if lockconf2 in optiony:

                    print("Starting 'LOCKDOWN_DIS.SH(C:/SYS/SECURITY')...")
                    time.sleep(1)
                    clear()
                    lockdis(suc)
                    norm = True
                    lockconf = False
                    lockpass = 'test123'
                    authe = False
                    boot(suc, corrupt)
                    continue

                if lockconf2 in optionn:

                    continue

            if lockinp == wepp:

                lockconf2()
                lockconf2 = input("(Y/N):")

                if lockconf2 in optiony:

                    print("Starting 'LOCKDOWN_DIS.SH(C:/SYS/SECURITY')...")
                    time.sleep(1)
                    clear()
                    lockdis(suc)
                    norm = True
                    lockconf = False
                    lockpass = 'test123'
                    boot(suc, corrupt)
                    continue

                if lockconf2 in optionn:

                    continue

            if lockinp == '!log_display!':

                logdis(path, log)
                continue

            else:

                lerror(lockinp)
                continue

        while corrupt:

            if log:
                logf = open(path, "a")
                logf.write("\n#SYSTEM.ERROR: ERRORS DETECTED! Booting to FAIL-SAFE_PARTITION....")
                logf.write("\n#SYSTEM: Booted to FAIL-SAFE_PARTITION!")
                logf.close()

            while corrupt:

                clear()
                syscorp()
                corpinp = input("\nPlease enter emergency override code:")

                if corpinp == emover:
                    print("Rebooting and logging into '{}' account...".format(tec))
                    time.sleep(1)
                    norm = True
                    usern = tec
                    authe = True
                    interm = True

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#TYPE: {}".format(corpinp))
                        logf.write("\n#SYSTEM: Authenticating...")
                        logf.write("\n#SYSTEM: Authenticated!")
                        logf.write("\n#SYSTEM: Setting user to --> {}...".format(tec))
                        logf.write("\n#SYSTEM: Logged into {}!".format(tec))
                        logf.write("\n#SYSTEM.WARNING: System is unstable. some features may be unavailable!")
                        logf.close()

                    break

                if corpinp == '!log_display!':

                    logdis(path, log)
                    continue

                else:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#TYPE: {}".format(corpinp))
                        logf.write("\n#SYSTEM: Authenticating...")
                        logf.write("\n#SYSTEM: INCORRECT CODE!")
                        logf.close()

                    print("INCORRECT CODE!")
                    x = input("Press enter to continue...")
                    continue

            break

    while norm:

        # Usernames and passwords

        if log:

            if corrupt:

                continue

            logf = open(path, "a")
            logf.write("\n#SYSTEM: Loading Login_Screen...")
            logf.write("\n#SYSTEM: Loaded Login_screen!")
            logf.close()

        while not authe:

            clear()
            print("Welcome to Outpost Interface Manager login(ver. 1.73.48)")
            print("Please login:\n")
            usern = input("Username:")
            passw = input("Password:")

            if usern == tec and passw == tecp:

                authe = True

            if usern == pio and passw == piop:

                authe = True

            if usern == wep and passw == wepp:

                authe = True

            if usern == bio and passw == biop:

                authe = True

            if not authe:

                if log:

                    logf=open(path, "a")
                    logf.write("\n#TYPE: {}".format(usern))
                    logf.write("\n#TYPE: {}".format(passw))
                    logf.write("\n#SYSTEM.ERROR: Invalid login credentials!")
                    logf.close()

                print("\nIncorrect Username/Password!")
                x = input("Press enter to continue...")
                continue

            if authe:

                if log:

                    logf = open(path, "a")
                    logf.write("\n#TYPE: {}".format(usern))
                    logf.write("\n#TYPE: {}".format(passw))
                    logf.write("\n#SYSTEM: Credentials accepted!")
                    logf.write("\n#SYSTEM: Setting user to --> {}".format(usern))
                    logf.write("\n#SYSTEM: Starting login procedure...")
                    logf.write("\n#SYSTEM: Login procedure complete!")
                    logf.close()

                break

        # Login procedure
        clear()
        login(suc)
        interm = True
        # Code for Terminal welcome screen
        clear()
        startt(usern)

        while interm:

            inp = input("C:/Users/{}>>>" .format(usern))

            if log:

                logf = open(path, "a")
                logf.write("\n#USER.{}.TYPE: {}".format(usern, inp))
                logf.close()

            if inp == 'help':

                if log:

                    logf = open(path, "a")
                    logf.write("\n#SYSTEM: Loading help_menu...")
                    logf.write("\n#SYSTEM: Loaded help_menu!")
                    logf.close()

                help(usern, wep, pio, bio, tec)
                continue

            if inp == 'logout':

                if corrupt:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: 'LOGOUT.SH' not found :(")
                        logf.close()

                    corp()
                    continue

                if log:

                    logf = open(path, "a")
                    logf.write("\n#SYSTEM: Logging out...")
                    logf.write("\n#SYSTEM: Setting user to --> NULL")
                    logf.close()

                print("Starting 'LOGOUT.SH(C:/SYS/ACCOUNT)'...")
                time.sleep(1)
                interm = False
                authe = False
                clear()
                logout(suc)
                continue

            if inp == 'music':

                if corrupt:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: 'MUSIC.SH' not found :(")
                        logf.close()

                    corp()
                    continue

                if log:

                    logf = open(path, "a")
                    logf.write("\n#SYSTEM: Loading 'MUSIC.SH'...")
                    logf.write("\n#SYSTEM: Loaded 'MUSIC.SH'!")
                    logf.write("\n#SYSTEM.WARNING: 'MUSIC.SH' dose not support log collection. "
                               "Any input/system event will NOT be recorded!")
                    logf.close()

                print("Starting 'MUSIC.SH(C:/USR/WINDOWS)...'")
                time.sleep(1)
                clear()
                musics(suc, tec)
                clear()

                while True:

                    music(tec, bio, pio, wep)
                    musicinp = input("Please select a number:")

                    if musicinp == '1':

                        clear()
                        tecmus(tec)
                        continue

                    if musicinp == '2':

                        clear()
                        biomus(bio)
                        continue

                    if musicinp == '3':

                        clear()
                        piomus(pio)
                        continue

                    if musicinp == '4':

                        clear()
                        wepmus(wep)
                        continue

                    if musicinp == '5':

                        winsound.PlaySound(None, winsound.SND_ASYNC)
                        continue

                    else:

                        if musicinp == '6':

                            print("Exiting...")
                            time.sleep(1)
                            clear()
                            break

                        print("Invalid option!")
                        x = input("\nPress enter to continue...")
                        continue

                continue

            if inp == 'file':

                if corrupt:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: 'FILE.SH' not found :(")
                        logf.close()

                    corp()
                    continue

                if log:

                    logf = open(path, "a")
                    logf.write("\n#SYSTEM: Loading 'FILE.SH'...")
                    logf.write("\n#SYSTEM: Loaded 'FILE.SH'!")
                    logf.write("\n#SYSTEM.WARNING: Log collection disabled by administrator on 'FILE.SH'!")
                    logf.write("\n#SYSTEM.MESSAGE: This will keep people out of my damn files!")
                    logf.close()

                print("Starting 'FILE.SH(C:/SYS/FILEMAN)'...")
                time.sleep(1)
                clear()
                files(suc)
                clear()
                file(bio, wep, pio, tec, biop, wepp, piop, tecp, emover, freq, logpass)
                continue

            if inp == 'radio':

                if corrupt:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: 'RADIO.SH' not found :(")
                        logf.close()

                    corp()
                    continue

                if log:

                    logf = open(path, "a")
                    logf.write("\n#SYSTEM: Loading 'RADIO.SH'...")
                    logf.write("\n#SYSTEM: Loaded 'RADIO.SH'!")
                    logf.close()

                print("Starting 'RADIO.SH(C:/SYS/RADIO/)'...")
                time.sleep(1)
                clear()
                radios(suc)
                clear()
                radio(freq, optiony, optionn, log, usern, path)
                continue

            if inp == 'info':
                if log:

                    logf = open(path, "a")
                    logf.write("\n#SYSTEM: Displaying account_info.")
                    logf.close()

                uinfo(usern, log, tec, bio, pio, wep)
                continue

            if inp == 'clear':

                if log:

                    logf=open(path, "a")
                    logf.write("\n#SYSTEM: Clearing screen...")
                    logf.close()

                clear()
                continue

            if inp == 'lockdown':

                if usern == wep:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM: Displaying LOCKDOWN_HELP")
                        logf.close()

                    lockinfo()
                    continue

                else:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM.ERROR: {} is not a valid command!".format(inp))
                        logf.close()

                    terror(inp, log, path)
                    continue

            if inp == 'lockdown_int':

                if usern == wep:

                    lockcon(lockpass, lockconf)
                    lockpass = input("\nPassword:")
                    print("\nAre you sure?")
                    lockconfd = input("(Y/N):")

                    if lockconfd in optiony:

                        lockconf = True

                    if lockconfd in optionn:

                        lockconf = False

                        if log == True:

                            logf = open(path, "a")
                            logf.write("\n#SYSTEM: Displaying lockdown_config")
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, lockpass))
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, lockconfd))
                            logf.write("\n#SYSTEM: Canceling...")
                            logf.close()

                    if lockconf:

                        print("Starting 'LOCKDOWN.SH(C:/SYS/SECURITY)'...")
                        time.sleep(1)
                        clear()
                        lockint(suc)
                        norm = False
                        interm = False
                        auth = False

                        if log:

                            logf = open(path, "a")
                            logf.write("\n#SYSTEM: Starting 'LOCKDOWN.SH'...")
                            logf.write("\n#SYSTEM: Rebooting...")
                            logf.close()

                        continue

                    if not lockconf:

                        continue

                else:

                    terror(inp, log, path)

                continue

            if inp == 'GENOME_MATCHER':

                if usern == bio:

                    print("Starting 'GENOME_MATCHER.SH(C:/USR/{}/GM)'...".format(bio))
                    time.sleep(1)
                    GMS()
                    print("\nAre you sure you want to run this script?")
                    gminp = input("(Y/N):")

                    if gminp in optiony:

                        print("\nContinuing startup...")
                        time.sleep(1)
                        GMB()
                        GM()
                        authe = False
                        norm = False
                        corrupt = True
                        interm = False

                        if log:

                            logf = open(path, "a")
                            logf.write("\n#SYSTEM: Starting GENOME_MATCHER.SH...")
                            logf.write("\n#SYSTEM.WARNING: FILE(GENOME_MATCHER.SH) HAS FAILED INTEGRITY CHECK!")
                            logf.write("\n#SYSTEM.WARNING: RUNNING THIS FILE IS NOT RECOMMENDED!")
                            logf.write("\n#SYSTEM.WARNING: Displaying warning message...")
                            logf.write("\n#USER.{}.TYPE: y".format(usern))
                            logf.write("\n#SYSTEM: Ignoring unstable files...")
                            logf.write("\n#SYSTEM: Starting GENOME_MATCHER.sh...")
                            logf.write("\n#SYSTEM.ERROR: BAD_VARIABLE")
                            logf.write("\n#SYSTEM.ERROR: BAD_VARIABLE")
                            logf.write("\n#SYSTEM.ERROR: BAD_VARIABLE")
                            logf.write("\n#SYSTEM: (Suppressing identical messages)")
                            logf.write("\n#SYSTEM.WARNING: SYSTEM_FAIL-SAFE ACTIVATED!")
                            logf.write("\n#SYSTEM.WARNING: Restarting...")
                            logf.close()

                        continue

                    if gminp in optionn:

                        print("Exiting...")

                        if log:

                            logf = open(path, "a")
                            logf.write("\n#SYSTEM: Starting GENOME_MATCHER.SH...")
                            logf.write("\n#SYSTEM.WARNING: FILE(GENOME_MATCHER.SH) HAS FAILED INTEGRITY CHECK!")
                            logf.write("\n#SYSTEM.WARNING: RUNNING THIS FILE IS NOT RECOMMENDED!")
                            logf.write("\n#SYSTEM.WARNING: Displaying warning message...")
                            logf.write("\n#USER.{}.TYPE: n".format(usern))
                            logf.write("\n#SYSTEM: Canceling...")
                            logf.close()

                        clear()
                        continue

                else:

                    terror(inp, log, path)

            if inp == 'syscheck':

                if usern == tec:

                    print("Are you sure you want to run a system integrity check?\n(THIS WILL TAKE A LONG TIME!)")
                    checkinp = input("\n(Y/N):")

                    if checkinp in optiony:

                        print("Starting 'SYSCHECK.SH(C:/SYS/TOOLS/SYSCHECK)'...")
                        time.sleep(1)
                        syss()
                        syscheck(corrupt)

                        if not corrupt:

                            if log:

                                logf = open(path, "a")
                                logf.write("\n#SYSTEM: Starting SYSCHECK.sh...")
                                logf.write("\n#SYSTEM: Started SYSCHECK.sh!")
                                logf.write("\n#USER.{}.TYPE: {}".format(usern, checkinp))
                                logf.write("\n#SYSTEM: Handing all services to 'SYSCHECK.SH'...")
                                logf.write("\n#SYSTEM: Released system to 'SYSCHECK.sh'!"
                                           "(log collection might be disabled for a short while)")
                                logf.write("\n#SYSTEM: SYSCHECK.sh complete!")
                                logf.close()

                            clear()
                            continue

                        norm = True
                        authe = False
                        interm = False
                        corrupt = False

                        if log:

                            logf = open(path, "a")
                            logf.write("\n#SYSTEM: Starting SYSCHECK.sh...")
                            logf.write("\n#SYSTEM: Started SYSCHECK.sh!")
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, checkinp))
                            logf.write("\n#SYSTEM: Handing all services to 'SYSCHECK.SH'...")
                            logf.write("\n#SYSTEM: Released system to 'SYSCHECK.sh'!"
                                       "(log collection might be disabled for a short while)")
                            logf.write("\n#SYSTEM: Rebooting...")
                            logf.close()

                            boot(suc, corrupt)

                    if checkinp in optionn:

                        if log:

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

            if inp == 'log':

                if usern == tec:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM: Displaying LOG_INFO!")
                        logf.close()

                    loggh()
                    continue

                else:

                    terror(inp, log, path)
                    continue

            if inp == 'log_enable':

                if usern == tec:

                    logf = open(path, "a")
                    logf.write("\n#SYSTEM: Enabling log collection...")
                    logf.write("\n#SYSTEM: Log collection enabled!")
                    logf.write("\n#SYSTEM.MESSAGE: Please respect the privacy of your peers!")
                    logf.close()

                    print("LOG COLLECTION ENABLED!")
                    print("Please respect the privacy of your peers!")
                    log = True
                    continue

                else:

                    terror(inp, log, path)
                    continue

            if inp == 'log_disable':

                if usern == tec:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM: Disabling log collection...")
                        logf.write("\n#SYSTEM: Log collection disabled!")
                        logf.close()

                    print("LOG COLLECTION DISABLED!")
                    log = False
                    continue

                else:

                    terror(inp, log, path)
                    continue

            if inp == 'log_clear':

                if usern == tec:

                    if log:

                        logf = open(path, "a")
                        logf.write("\n#SYSTEM: Prompting user...")
                        logf.close()

                    print("Are you sure you want to clear the logs?")
                    print("THIS WILL DELETE ALL LOG CONTENT!")
                    loginp = input("\n(Y/N):")

                    if loginp in optiony:

                        logstart(path)
                        print("Logs cleared!")

                        if log:

                            logf = open(path, "a")
                            logf.write("\n#SYSTEM: Logs cleared!")
                            logf.close()

                        continue

                    else:

                        if log:

                            logf = open(path, "a")
                            logf.write("\n#USER.{}.TYPE: {}".format(usern, loginp))
                            logf.write("\n#SYSTEM: Canceling...")
                            logf.close()

                        continue

                else:

                    terror(inp, log, path)
                    continue

            if inp == 'log_display':

                logdis(path, log)
                continue

            else:

                terror(inp, log, path)
                continue
