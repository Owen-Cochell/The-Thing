#This module has the animations and cutscenes inside
import time
import os
import itertools
import threading
import sys
suc='#Success!'
def boot(suc, corrupt):
    #Code for boot up procedure
    lpass=False
    print("                __         __                   __     __ __  __       \n              / __ \__  __/ /_____  ____  _____/ /_   / // /^/ /\n             / / / / / / / __/ __ \/ __ \/ ___/ __/  / // /_/ / \n            / /_/ / /_/ / /_/ /_/ / /_/ (__  ) /_   /__  __/ /  \n            \____/\____/\__/ .___/\____/____/\__/     /_/ /_/   \n                          /_/     ")                          
    print("                        United States Research Divison    \n                             O.I.M ver. 1.73.48")
    print("+===================+")
    print("|Starting system... |")
    print("+===================+")
    end=False
    var1="#Accessing boot files(C:/SYS/boot/)..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#Loading modules..."
    ltime=40
    load(var1, suc, ltime, end, lpass)
    var1="#Initializing P.E.E(Protected Execution Environment)..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#Loading G.U.I(Graphical User Interface)..."
    ltime=40
    end=True
    load(var1, suc, ltime, end, lpass)
    print("\n+=======================+")
    print("|Running diagnostics... |")
    print("+=======================+")
    lpass=True
    end=False
    var1="#CPU test..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#Disk test..."
    ltime=40
    load(var1, suc, ltime, end, lpass)
    var1="#RAM test..."
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#System integrety check..."
    if corrupt==True:
        loadf()
        print("\nErrors detected. Booting to 'FAILSAFE_PARTITION'...")
        time.sleep(3)
        return
    ltime=50
    end=True
    load(var1, suc, ltime, end, lpass)
    time.sleep(1)
    lpass=False
    return

def load(var1, suc, ltime, end, lpass):
    intime=0
    passv='PASS'
    sys.stdout.write("\n")
    for m in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write("{}{}\r".format(var1, m))
        sys.stdout.flush()
        time.sleep(0.1)
        intime=intime+1
        if intime==ltime:
            if end==True:
                if lpass==True:
                    sys.stdout.write("{}{}\r".format(var1, passv))
                    sys.stdout.flush()
                if lpass==False:
                    m=' '
                    sys.stdout.write("{}{}\r".format(var1, m))
                    sys.stdout.flush()
                print("\n{}".format(suc))
                return
            if end==False:
                if lpass==True:
                    sys.stdout.write("{}{}\r".format(var1, passv))
                    return
                if lpass==False:
                    m=' '
                    sys.stdout.write("{}{}\r".format(var1, m))
                    sys.stdout.flush()
                    return

def loadf():
    ltime=40
    intime=0
    passv='FAIL'
    sys.stdout.write("\n")
    for m in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write("#System integrety check...{}\r".format(m))
        sys.stdout.flush()
        time.sleep(0.1)
        intime=intime+1
        if intime==ltime:
            sys.stdout.write("#System integrety check...{}\r".format(passv))
            return

def loadff():
    ltime=70
    intime=0
    passv='FAIL'
    sys.stdout.write("\n")
    for m in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write("#Checking system image...{}\r".format(m))
        sys.stdout.flush()
        time.sleep(0.1)
        intime=intime+1
        if intime==ltime:
            sys.stdout.write("#Checking system image...{}\r".format(passv))
            return

def auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop, usern, passw):
    #authentication backend
    if usern==tec and passw==tecp:
        authe=True
        return authe
    if usern==pio and passw==piop:
        authe=True
        return authe
    if usern==wep and passw==wepp:
        authe=True
        return authe
    if usern==bio and passw==biop:
        authe=True
        return authe
    else:
        authe=False
        return authe

def login(suc):
    #Code for starting terminal
    lpass=False
    print("############################################################\n                     FROM .BASH                     ")
    print("Starting...")
    end=False
    var1="Accessing harddrive..."
    ltime=10
    load(var1, suc, ltime, end, lpass)
    lpass=True
    var1="#Testing 'READ'..."
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#Testing 'WRITE'..."
    end=True
    ltime=10
    load(var1, suc, ltime, end, lpass)
    lpass=False
    var1="Accessing 'USERS.SH'(C:/SYS/USR)..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="Finalising..."
    ltime=40
    load(var1, suc, ltime, end, lpass)
    print("###########################################################")
    print("(END LOGIN.SH)")
    time.sleep(1)
    return

def startt(usern):
    #Cod for terminal welcome screen
    print("#############################################")
    print("O.I.M Terminal Interface System ver 3.1.74")
    print("@1986 All rights reserved ENTech LLC.")
    print(" ")
    print("Welcome user %s!" % usern)
    print("Type 'help' for a list of commands")
    return

def help(usern, wep, pio, bio, tec):
    #Code for help command
    print("#####################################")
    print("List of commands:")
    print(" ")
    print("'help' displays this list")
    print("'logout' logs out of user account")
    print("'music' starts music player")
    print("'file' accesses filesystem")
    print("'radio' opens radio app")
    print("'info' to see info on account")
    print("'clear' clears the terminal screen")
    if usern==wep:
        print("'lockdown_int' to initiate a security lockdown. Type 'lockdown' for more info")
        print(" ")
        print("####################################")
        return
    if usern==tec:
        print("'log[enable][disable]' to enable/disable logg collection. Type 'log' for more info")
        print("'syscheck' to check/repair corrupted files.")
        print(" ")
        print("####################################")
        return
    if usern==bio:
        #print("'fridge_config' to access fridge configuration menu")
        print("'GENOME_MATCHER' <Err: No definition found>")
        print(" ")
        print("####################################")
        return
    print("####################################")
    return

def logout(suc):
    lpass=False
    end=True
    print("##############################################")
    print("               FROM .BASH                     ")
    print("Starting...")
    var1="Stopping terminal session 'TERM.SH(C:\SYS\ACCOUNT)...'"
    ltime=40
    load(var1, suc, ltime, end, lpass)
    end=False
    print("Clearing temporary data...")
    var1="#Clearing cach..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#Clearing variables..."
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#Clearing user data..."
    ltime=10
    end=True
    load(var1, suc, ltime, end, lpass)
    var1="Loading 'LOGINSCREEN.SH(C:/SYS/ACCOUNT)'..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    print("#############################################")
    print("(END LOGOUT.SH)")
    time.sleep(1)
    return

def files(suc):
    end=False
    lpass=False
    print("############################################")
    print("                FROM .BASH                 ")
    print("Starting...")
    var1="Acessing harddrive..."
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#Testing READ..."
    ltime=10
    lpass=True
    load(var1, suc, ltime, end, lpass)
    var1="#Testing WRITE..."
    ltime=20
    end=True
    load(var1, suc, ltime, end, lpass)
    print("############################################")
    print("(END FILE.SH)")
    time.sleep(1)
    return
    
def file(bio, wep, pio, tec, biop, wepp, piop, tecp, biopl, weppl, piopl, tecpl, logpass, emover, freq):
    while True:
        clear()
        print("###########################################")
        print("File Manager System ver. 1.74.52")
        print("@1987 All rights reserved ENTech LLC.\n")
        print("Welcome to File Manager!")
        print("Below are files that can be veiwed. Enter the file number to view it.")
        print("'.txt' files can be veiwed, but '.enc' are encrypted and can't be viewed without decrypting them first\n")
        print("\nPlease select a directory to view:")
        print("1. SYSTEM_LOGS")
        print("2. AUDIO_LOGS")
        print("3. User-Logs")
        print("4. Quit")
        fiinp=input(">>")
        if fiinp=='SYSTEM_LOGS':
            clear()
            print("###########################################")
            print("SYSTEM_LOGS")
            print("Type 'back' to return to previous directory")
            print("Files:")
            print("\n1. LOG_1.txt")
            print("2. LOG_2.enc")
            print("3. LOG_3.txt\n")
            fiinp=input(">>")
            if fiinp=='LOG_1.txt':
                print("\n########################<<SYSTEM_LOG>>#######################")
                print("time: 07:78:91")
                print("Date: 10/3/1986")
                print("#################################")
                print("#TYPE: {}".format(bio))
                print("#TYPE: {}".format(biop))
                print("#SYSTEM: Setting user to --> {}".format(bio))
                print("#SYSTEM: Starting login procedure...")
                print("#SYSTEM: Login procedure complete!")
                print("#USER.{}.TYPE: notepad".format(bio))
                print("#SYSTEM: Starting notepad.sh...")
                print("#SYSTEM: Started notepad.sh!")
                print("#SYSTEM: Saved file as --> GENOME_MATCHER.SH")
                print("#USER.{}.TYPE: GENOME_MATCHER".format(bio))
                print("#SYSTEM: Starting GENOME_MATCHER.SH...")
                print("#SYSTEM.WARNING: FILE(GENOME_MATCHER.SH) HAS FAILED INTEGRETY CHECK!")
                print("#SYSTEM.WARNING: RUNNING THIS FILE IS NOT RECOMMENDED!")
                print("#SYSTEM.WARNING: Displaying warning message...")
                print("#USER.{}.TYPE: y".format(bio))
                print("#SYSTEM: Ignoring unstable files...")
                print("#SYSTEM: Starting GENOME_MATCHER.sh...")
                print("#SYSTEM.ERROR: BAD_VARIABLE")
                print("#SYSTEM.ERROR: BAD_VARIABLE")
                print("#SYSTEM.ERROR: BAD_VARIABLE")
                print("#SYSTEM: (Surpressing identical messages)")
                print("#SYSTEM.WARNING: SYSTEM_FAILSAFE ACTIVATED!")
                print("#SYSTEM.WARNING: Restarting...")
                print("#######################<<END_SYSTEM_LOG>>########################")
                x=input("\nPress any key to continue...")
                continue
            if fiinp=='LOG_2.enc':
                print("This file requires a password to open:")
                lopass=input("\nPassword:")
                if lopass==logpass:
                    print("\n##############################<<SYSTEM_LOG>>#################################")
                    print("Time: 09:24:37")
                    print("Date: 10/3/1986")
                    print("####################################")
                    print("#SYSTEM: Starting boot procedures...")
                    print("#SYSTEM: Boot procedures complete!")
                    print("#SYSTEM.ERROR: ERRORS DETECTED! Booting to FAILSAFE_PARTITION....")
                    print("#SYSTEM: Booted to FAILSAFE_PARTITION!")
                    print("#TYPE: {}".format(emover))
                    print("#SYSTEM: Authenticating...")
                    print("#SYSTEM: Authenticated!")
                    print("#SYSTEM: Loggining into {}...".format(tec))
                    print("#SYSTEM: Logged into {} account!".format(tec))
                    print("#USER.{}.TYPE: syscheck".format(tec))
                    print("#SYSTEM: Starting SYSCHECK.sh...")
                    print("#SYSTEM: Started SYSCHECK.sh!")
                    print("#USER.{}.TYPE: y".format(tec))
                    print("#SYSTEM: Handing all services to 'SYSCHECK.SH'...")
                    print("#SYSTEM: Released system to 'SYSCHECK.sh'!(logg collection might be disabled for a short while)")
                    print("#SYSTEM: Rebooting...")
                    print("##########################<<END_SYSTEM_LOG>>###################################")
                    x=input("\nPress any key to continue...")
                    continue
                else:
                    print("Incorrect password.")
                    x=input("\nPress any key to continue...")
                    continue
            if fiinp=='LOG_3.txt':
                print("\n##############################<<SYSTEM_LOG>>#################################")
                print("Time: 29:48:17")
                print("Date: 2/3/1986")
                print("####################################")
                print("#SYSTEM: Enabling log collection...")
                print("#SYSTEM: Log collection enabled!")
                print("#USER.{}.TYPE: logout".format(wep))
                print("#SYSTEM: Logging out...")
                print("#SYSTEM: Setting user to --> NULL")
                print("#SYSTEM: Loading login_screen...")
                print("#SYSTEM: Loaded login_screen!")
                print("#TYPE: {}".format(tec))
                print("#TYPE: {}".format(tecp))
                print("#SYSTEM: Setting user to --> bio")
                print("#SYSTEM: Starting login procedure...")
                print("#SYSTEM: Login procedure complete!")
                print("#USER.{}.TYPE: file".format(tec))
                print("#SYSTEM: Starting 'FILE.SH'...")
                print("#SYSTEM: Started 'FILE.SH'!")
                print("#USER.{}.TYPE: User-Logs".format(tec))
                print("#USER.{}.TYPE: tec-Log.enc".format(tec))
                print("#SYSTEM: Password requried. Prompting...")
                print("#USER.{}.TYPE: {}".format(tec, tecpl))
                print("#USER.{}.TYPE: Quit".format(tec))
                print("#USER.{}.TYPE: log_disable".format(tec))
                print("#SYSTEM: Disabling log collection...")
                print("#SYSTEM: Disabled log collection!")
                print("########################<<END_SYSTEM_LOG>>####################################")
                x=input("\nPress any key to continue...")
                continue
            
            if fiinp=='back':
                continue
            else:
                print("Invalid file.")
                x=input("Press any key to continue...")
                continue
        if fiinp=='AUDIO_LOGS':
            clear()
            print("###########################################")
            print("AUDIO_LOGS")
            print("Type 'back' to return to previous directory")
            print("Files:")
            print("\n1. AUDIO_LOG_1.txt")
            print("2. AUDIO_LOG_2.txt")
            print("3. AUDIO_LOG_3.txt")
            fiinp=input(">>")
            if fiinp=='AUDIO_LOG_1.txt':
                print("\n####################<<BEGIN_AUDIO_LOG>>##########################")
                print("Time: 14:38:34")
                print("Date: 10/2/1986")
                print("#####################################")
                print("#VOICE.1: Hey {}".format(tec))
                print("#VOICE.2: What?")
                print("#VOICE.1: What's the [REDACATED] for the [REDACATED]?")
                print("#VOICE.2: Oh, it's {} gigahertz".format(freq))
                print("#VOICE.1: Thanks.")
                print("#################<<END_AUDIO_LOG>>###############################")
                x=input("\nPress any key to continue...")
                continue
            if fiinp=='AUDIO_LOG_2.txt':
                print("\n####################<<BEGIN_AUDIO_LOG>>##########################")
                print("Time: 12:48:64")
                print("Date: 10/4/1986")
                print("#####################################")
                print("VOICE.1: {}!".format(tec))
                print("VOICE.2: What is it, {}?".format(bio))
                print("VOICE.1: What the hell are you listing to?")
                print("VOICE.2: My favorite song, let's do the time warp again.")
                print("VOICE.1: Is that the only song you have on your playlist?")
                print("VOICE.2: Yes.")
                print("VOICE.1: Turn that shit off! It's very unsophistucated!")
                print("<SPEAKER_VOlUME_INCREACE>")
                print("VOICE.1: [REDACATED]!")
                print("##################<<END_AUDIO_LOG>>#############################")
                x=input("\nPress any key to continue...")
                continue
            if fiinp=='AUDIO_LOG_3.txt':
                print("\n####################<<BEGIN_AUDIO_LOG>>##########################")
                print("Time: 15:56:24")
                print("Date: 10/5/1986")
                print("#####################################")
                print("#VOICE.1: Holy shit, {}! What the hell is that?".format(pio))
                print("#VOICE.2: Don't know. Found it at the site. With the distress beacon.")
                print("#VOICE.3: What...")
                print("#VOICE.4: DON't TOUCH it! Do you know how many safety prodocals we are breaking?")
                print("#VOICE.2: Relax, {}. I just thought {} would like to have a look at it.".format(wep, bio))
                print("#VOICE.3: You assumed correctly. Let's take a gander...")
                print("<No voice captures detected for 3 minutes>")
                print("#VOICE.3: Well, by the looks of it, it's obviously a [REDICATED].")
                print("#VOICE.4: What the hell is that supposed to mean?")
                print("#VOICE.3: It has [REDICATED] amount of [REDICATED]. Very uncanny biology. Never seen anything like this before...")
                print("#VOICE.1: English, {}.".format(bio))
                print("#VOICE.3: This thing's not from around here. None of these organs seem to [REDICATED].")
                print("#VOCIE.4: We need to keep an eye on this, thing, and report it to HQ.")
                print("#VOICE.1 Roger. I'll get to it.")
                print("#VOICE.4: {}}, keep this thing in the freezer until further notice.".format(bio))
                print("#VOICE.3: Roger that, {}.".format(wep))
                print("####################<<END_AUDIO_LOG>>###########################")
                x=input("\nPress any key to continue...")
                continue
            if fiinp=='back':
                continue
            else:
                print("Invalid file.")
                x=input("\nPress any key to continue...")
                continue
        if fiinp=='User-Logs':
            clear()
            print("###########################################")
            print("User-Logs")
            print("Type 'back' to return to previous directory")
            print("Files:")
            print("\n1. {}-Log.enc".format(bio))
            print("2. {}-Log.txt".format(pio))
            print("3. {}-Log.enc".format(wep))
            print("4. {}-Log.enc".format(tec))
            fiinp=input(">>")
            if fiinp==bio + '-Log.enc':
                print("This file requires a password to open:")
                lopass=input("\nPassword:")
                if lopass==biopl:
                    print("\n########################################################")
                    print("Secure log system ver 3.24.8:")
                    print("(DATE AND TIME DISABLED)\n")
                    print("ENTRY 1:\n")
                    print("    This is {}, head biologyst of Outpost 41. This place seems, quiet. I'm not gonna be doing much around here besides checking the samples in the freezer. Gonna be a hellava boring 9 months. at least I have this computer to write down my thoughts.\n".format(bio))
                    print("ENTRY 2:\n")
                    print("    I hate {}. He's an annoying piece of shit. He keeps 'messing around' with my logs, and constantly screws up the testing environment. He compromised 3 microganism colonies already! And he keeps playing that same, goddamn song. Jesus, if I have to put up with his shit much longer, i'll take my chances out in the frozen wasteland. Better than being copped up with {}.\n".format(tec, tec))
                    print("ENTRY 3:\n")
                    print("    We found... something. {} came back from a scouting mission investigating another research outpost emitting a distress call. He found this... strange lifeform. It appears to have human organs, but dose not appear to be human. It has mutiple limbs(perhapps 'appendages' would be more accurate), and appears, to have... dog fur. Also, upon further genetic testing, I found that some cells are still alive. They are in some form of hibernation, most likely from the cold. I saved a few samples for analysis. Perhapps this will give me something to pass the time.\n".format(pio))
                    print("########################################################")
                    x=input("\nPress any key to continue...")
                    continue
                else:
                    print("Incorrect password.")
                    x=input("\nPress any key to continue...")
                    continue
            if fiinp==pio + '-Log.txt':
                print("\n########################################################")
                print("Secure log system ver 3.24.8")
                print("(DATE AND TIME DISABLED)\n")
                print("ENTRY 1:\n")
                print("    This is stupid. I'm not using this shit.\n")
                print("########################################################")
                x=input("\nPress any key to continue...")
                continue
            if fiinp==wep + '-Log.enc':
                print("This file requires a password to open:")
                lopass=input("\nPassword:")
                if lopass==weppl:
                    print("\n########################################################")
                    print("Secure log system ver 3.24.8")
                    print("(DATE AND TIME DISABLED)\n")
                    print("ENTRY 1:\n")
                    print("    The men under my command are, well, interesting to say the least. They range from ignorant and immature, to arrogant and pompus. Keeping these men under control will be a challenge.\n")
                    print("ENTRY 2:\n")
                    print("    I need to find a safe place to keep my gun key. {} has been asking to distribute them, so the men can defend themselves in an emergency. I don't know what could possibly happen out here, but arming the entire staff of this facility is NOT a good idea.\n".format(pio))
                    print("ENTRY 3:\n")
                    print("    I took the liberty of securing logs with sensitive info inside. Don't want my boys to get into something they shouldn't be seeing. For future refrence, the password is: {}.\n".format(logpass))
                    print("ENTRY 4:\n")
                    print("    {} brought back something interesting from his scouting mission. According to {}, it's a lifeform hes never seen before. Well, it disappeared from the freezer. We found it outside the facility, crawling around. It seemed like it didn't know how to use it's body, like it was still learning. It was stumbling around and falling over its self. We torched it. It died immediatly. Everyone is on edge now, nobody knows what to think anymore.\n".format(pio, bio))
                    print("########################################################")
                    x=input("\nPress any key to continue...")
                    continue
                else:
                    print("Incorrect password.")
                    x=input("\nPress any key to continue...")
                    continue
            if fiinp==tec + '-Log.enc':
                print("This file requires a password to open:")
                lopass=input("\nPassword:")
                if lopass==tecpl:
                    print("\n########################################################")
                    print("Secure log system ver 3.24.8")
                    print("(DATE AND TIME DISABLED)\n")
                    print("ENTRY 1:\n")
                    print("	Wow. A shitty journal app on a shitty computer in a shitty outpost in the middle of fucking nowhere. This is gonna be the most boring job yet. And that's saying something! You shoulda seen it when I was the system administrator for some company I was working with. All I did was change the ink on the photo copier. Now, i'm gonna be using this computer system to manage an outpost with litle to no intrest to anybody at D.C. Woopie.\n")
                    print("ENTRY 2:\n")
                    print("	Goddamn it, little bastards are smarter than I thought. {}, the biologist, somehow managed to figure out how to make scripts with 'notepad.sh'. Unfortunatly, he has no idea what he's doing. His app isn't correctly compiled, which leads to memory leakedge from invalid variables created by the script. He crashed the whole system. Had to do a complete reinstall. It's a wonder that I was able to recover all of our data. Gonna have to tighten up security on P.E.E(Protected Execution Environment. A unfortunate nickname, I know), disable 'notepad.sh', and give a stern talking to to {}. Little shit managed to waste a good 4 hours of my time.\n".format(bio, bio))
                    print("ENTRY 3:\n")
                    print("	They did it again. {} somehow managed to get in my account, enable log collection, and get the credentls to unlock most of the encrypted documents. I am guessing he just wanted to keep a better eye on us. A little tyranical though, don't you think? I mean, I know he's the boss and all, but dosen't he have any respect for privacy? Anyway, I disabled log collection on the files app and restricted log control to my account. But not before I get some passwords for payback ;)\n".format(wep))
                    print("ENTRY 4:\n")
                    print("	List of log credentials:")
                    print("	#pio:N/A")
                    print("	#wep: {}".format(weppl))
                    print("	#bio: {}\n".format(biopl))
                    print("ENTRY 5:\n")
                    print("	So I managed to make a music player for the guys. They like the fact that they can play their own songs. Thought it would boost moral a bit.\n")
                    print("ENTRY 6:\n")
                    print("	OH SHIT OH GOD HOLY FUCK I WENt IntO THE FREEZER AND IT WAS GONE! THE FUCKINg BODY IS FUCKINg gONE!!! HOLY SHIt I thOUGHT IT WAS DEAD... I gotta tell somebody about this...\n")
                    print("##################################################")
                else:
                    print("Incorrect password.")
                    x=input("\nPress any key to continue...")
                    continue
            if fiinp=='back':
                continue
        if fiinp=='Quit':
            print("Exiting...")
            time.sleep(1)
            return
    

def uinfo(usern, logg, tec, bio, pio, wep):
    print("#####################################")
    print("Username: %s" % usern)
    if usern==wep:
        role='Security Administrator'
    if usern==bio:
        role='Biologist'
    if usern==pio:
        role='Pilot'
    if usern==tec:
        role='System Administrator'
    print("Role: %s" % role)
    print("System Version: 1.73.48")
    if usern==wep:
        logt='10/28/1986'
    if usern==bio:
        logt='10/29/1986'
    if usern==pio:
        logt='6/14/1986'
    if usern==tec:
        logt='10/29/1986'
    print("Last Login: %s" % logt)
    print("System Managment: United States Research Division")
    if logg==True:
        print("(Logg collection is ON!)")
    print("#####################################")
    return
    
def terror(inp, log, path):
    if log==True:
        logf=open(path, "a")
        logf.write("\n#SYSTEM: Invalid command!")
        logf.close()
    print("Error:\n#'%s' is not a valid command!" % inp)
    return

def lockinfo():
    print("###########################################")
    print("Lockdown Help:")
    print("Command 'lockdown' alows you to initilaise/deactivate a system lockdown.\n")
    print("Type 'lockdown_int' to activate the lockdown sequence.\n")
    print("Type 'lockdown' to see this page.\n")
    print("###########################################")
    print("What is a lockdown?:")
    print("If you activate a system lockdown, all electrical and computerised systems will be put into lockdown")
    print("This means mechanical doors, terminals, radio, ect.")
    print("They will maintain their current configurations, but they can't be changed")
    print("###########################################")
    print("How do I activate a lockdown?:")
    print("Activating a lockdown will prompt you for a password, and conformation.")
    print("PLEASE KEEP THIS PASSWORD AS THE ONLY OTHER WAY TO LIFT A LOCKDOWN IS TO ENTER SECURITY OVERIDE PASSWORD")
    print("The system will reboot, and it will prompt you with a password screen to lift the system lockdown.")
    print("###########################################")
    print("How do I deactivate a lockdown?:")
    print("To deactivate a lockdown, enter the password you have set, or enter the security overide password.")
    print("If you enter the security overide password, then you will be able to deactivate the security lockdown.")
    print("If you enter the set password, the security lockdown will be deactivated.")
    print("###########################################")
    return

def lockcon(lockpass, lockconf):
    print("###########################################")
    print("ATTENTION:")
    print("Activating lockdown means access to electrical and computerised systems will be revoked")
    print("The only way to lift a lockdown is to enter set password, or security overide password\n")
    print("Please set your security lockdown password below.")
    print("(REMEMBER THIS!!)")
    
def lockint(suc):
    end=True
    lpass=False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1="Accessing hardrive..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    end=False
    print("Initiating lockdown...")
    var1="#Editing boot files..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#Placing account safeguards..."
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#Sending 'LOCKDOWN' signal to all machinery..."
    ltime=40
    load(var1, suc, ltime, end, lpass)
    var1="#Changing settings..."
    ltime=20
    end=True
    load(var1, suc, ltime, end, lpass)
    end=False
    print("Encrypting filesystem(this will take awile)...")
    var1="#0%"
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#10%"
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#20%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#30%"
    ltime=40
    load(var1, suc, ltime, end, lpass)
    var1="#40%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#50%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#60%"
    ltime=50
    load(var1, suc, ltime, end, lpass)
    var1="#70%"
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#80%"
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#90%"
    ltime=40
    load(var1, suc, ltime, end, lpass)
    print("#100%")
    print(suc)
    print("Complete. The system will now reboot.")
    time.sleep(2)
    print("############################################")
    print("(END LOCKDOWN.SH)")
    time.sleep(1)
    os.system("color 0c")
    return

def lockout():
    print("    ___ ")  
    print(" .'/   \ ") 
    print("  / /     \ ")
    print("^| ^|     ^| ")
    print("^| ^|     ^| ") 
    print("^|/`.   .' ")
    print("  `.^|   ^|  ")
    print("  ^|^|___^|  ")
    print("  ^|/___/  ")
    print("  .'.--.  ")
    print(" ^| ^|    ^| ")
    print(" \_\    / ")
    print("  `''--'  ")
    print(" ")
    print("Attention:\n")
    print("A system lockdown has been initiated by your security administrator.")
    print("All electrical and computerised equipment are now in lockdown, and are now inaccessable.")
    print("Please contact your security administrator for more info.\n")
    return

def lerror(lockinp):
    print("Error:\n#Incorrect password.\n#Please contact your security administrator for more info.")
    x=input("Press any key to continue...")
    return

def lockconf2():
    print("\nAre you sure you want to disable lockdown?")
    return

def lockdis(suc):
    end=True
    lpass=False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    time.sleep(2)
    var1="Accessing hardrive..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    end=False
    print("Disabling lockdown...")
    var1="#Editing boot files..."
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#Removing account safeguards..."
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#Sending 'DIS_LOCKDOWN' signal to all machinery..."
    ltime=40
    load(var1, suc, ltime, end, lpass)
    var1="#Changing settings..."
    ltime=20
    end=True
    load(var1, suc, ltime, end, lpass)
    end=False
    print("De-crypting filesystem(this will take a wile)...")
    var1="#0%"
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#10%"
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#20%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#30%"
    ltime=40
    load(var1, suc, ltime, end, lpass)
    var1="#40%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#50%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#60%"
    ltime=50
    load(var1, suc, ltime, end, lpass)
    var1="#70%"
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#80%"
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#90%"
    ltime=40
    load(var1, suc, ltime, end, lpass)
    print("#100%")
    print(suc)
    print("Complete. The system will now reboot.")
    time.sleep(2)
    print("############################################")
    print("(END LOCKDOWN_DIS.SH)")
    time.sleep(1)
    os.system("color 0a")
    return

def musics(suc, tec):
    end=True
    lpass=False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1="Accessing music player directory(C:/USR/TECHNICAL/MUSIC_PLAY)..."
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="Loading libraries into P.E.E(Protected Execution Environment)..."
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="Finding music directory(C:/USR/TECHNICAL/MUSIC)..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    print("############################################")
    print("(END MUSIC.SH)")
    time.sleep(1)
    return
    
def music(tec, bio, pio, wep):
    print("############################################")
    print("Music Player Ver. 2.7.5")
    print("Welcome to the music player fellas.\nThis app was made by %s(you're welcome)\nPeoples songs are seperated by directores.\nJam on boys!" % tec)
    print("")
    print("Please select a directory:")
    print("1.{}'s Jams\n2.{}'s Bores\n3.{} Songs\n4.{} Songs".format(tec, bio, pio, wep))
    return

def tecmus(tec):
    end=False
    lpass=False
    print("############################################")
    print("%s Jams" % tec)
    print("1.Let's do the time warp again")
    musicinp2=input("Select a number:")
    if musicinp2=='1':
        var1="Playing 'Lets do the time warp again'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        #Code for playing music here
        return
    else:
        print("Invalid option!")
        return

def biomus(bio):
    end=False
    lpass=False
    print("############################################")
    print("%s Bores" % bio)
    print("1. The fair at Sorochyntsi\n2. Samson and Delila Bacchanale")
    musicinp2=input("Select a number:")
    if musicinp2=='1':
        var1="Playing 'The fair at Sorochyntsi'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #code for playing music here
        return
    if musicinp2=='2':
        var1="Playing 'Samson and Delila Bacchanale'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    else:
        print("Invalid option!")
        return
    
def piomus(pio):
    end=False
    lpass=False
    print("############################################")
    print("%s Music" % pio)
    print("1. Jailhouse Rock\n2. If you leave me now\n3. Messaround\n4. Anything goes\n5. Orange sky")
    musicinp2=input("Select a number:")
    if musicinp2=='1':
        var1="Playing 'Jailhouse Rock'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='2':
        var1="Playing 'If you leave me now'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='3':
        var1="Playing 'Messaround'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='4':
        var1="Playing 'Anything goes'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='5':
        var1="Playing 'Orange Sky'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    else:
        print("Invalid option!")
        return
    
def wepmus(wep):
    end=False
    lpass=False
    print("############################################")
    print("{} Music".format(wep))
    print("1. Video Killed the radio star\n2. September\n3. You make my dreams come true\n4. Don't you forget about me\n5. Wild Wild Life\n6. Jump")
    musicinp2=input("Select a number:")
    if musicinp2=='1':
        var1="Playing 'Video killed the radio start'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='2':
        var1="Playing 'September'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='3':
        var1="Playing 'You make my dreams come true'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='4':
        var1="Playing 'Don't you forget about me'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='5':
        var1="Playing 'Wild Wild Life'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    if musicinp2=='6':
        var1="Playing 'Jump'..."
        ltime=20
        load(var1, suc, ltime, end, lpass)
        clear()
        #Code for playing music here
        return
    else:
        print("Invalid option!")
        return
           
def signalsearch(var1):
    intime=0
    for m in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write("\r{}{}".format(var1, m))
        sys.stdout.flush()
        time.sleep(0.1)
        intime=intime+1
        if intime==20:
            print("\n")
            break
        
def radios(suc):
    end=True
    lpass=False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1="Accessing disk..."
    ltime=10
    load(var1, suc, ltime, end, lpass)
    end=False
    print("Prepping system...")
    var1="#Loading radio firmware(C:/SYS/FIM/RAD/)..."
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#Finding and configuring broadcast equipment..."
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#Testing connection..."
    ltime=30
    end=True
    lpass=True
    load(var1, suc, ltime, end, lpass)
    print("############################################")
    print("(END RADIO.SH)")
    time.sleep(1)
    return

def radio(freq, optiony, optionn, log, usern, path):
    print("############################################")
    print("Radio Interface System ver. 3.3.8")
    print("@1986 All Rights Reserved ENTech LLC.")
    print("Welcome to the Radio Interface System!")
    print("Please Enter a frequency below to start broadcasting:\n")
    freqinp=input("Enter a frequency:")
    if freqinp==freq:
        if log==True:
            logf=open(path, "a")
            logf.write("\n#USER.{}.TYPE: {}".format(usern, freqinp))
            logf.write("\n#SYSTEM: Signal accuired!")
            logf.close()
        var1='Searching...'
        clear()
        print("Searching for signals...")
        signalsearch(var1)
        print("Signal accuired!")
        print("Connection to 'Automated Relay Station 1156' established!")
        print("Are you sure you want to broadcast a 'SOS' alert?")
        sosinp=input("(Y/N):")
        if sosinp in optiony:
            if log==True:
                logf=open(path, "a")
                logf.write("\n#USER.{}.TYPE: {}".format(usern, sosinp))
                logf.write("\n#SYSTEM: Broadcasting SOS alert...")
                logf.write("\n#SYSTEM: Accuired response!")
                logf.write("\n#SYSTEM: Displaying 'PROTOCAL_1194'")
                logf.close()
            #Code for radio backend here
            end=False
            lpass=False
            var1="Broadcasting 'SOS' alert..."
            ltime=40
            load(var1, suc, ltime, end, lpass)
            print("\nAccuired response!")
            print("Displaying response:")
            print("\n(BEGIN MESSAGE:)")
            print("+==========================================+")
            print("|(5/19/1986, 05:27:06)                     |")
            print("|Automated Relay Station 1156              |")
            print("|This is a automated message(CODE 1194)    |")
            print("|Reinforcments inbound. Arriving in 2 days.|")
            print("|Evacuating all crew and staff upon arrival|")
            print("+==========================================+")
            print("(END MESSAGE)")
            x=input("\nPress any key to continue...")
            print("This message has been sent with a protocal code(1194).\nDisplaying instructions below:")
            print("\n############################################")
            print("Protocal code: 1194\nProtocal name: Evacuation protocal")
            print("Instructions:\n1. Gather all research doucuments/specimins(IF POSSIBLE).")
            print("2. Inform/prepare all crew and staff for evacuation.")
            print("3. Gather all class C and above materials(IF POSSIBLE). Personal belongins are NOT to be brought.")
            print("4. Prepare landing pad")
            print("The evacuation team will be arriving in TWO DAYS.\nPlease have these tasks completed upon arrival.")
            print("############################################")
            x=input("Press any key to continue...")
            print("Exiting...")
            time.sleep(1)
            clear()
            return
            
        if sosinp in optionn:
            if log==True:
                logf=open(path, "a")
                logf.write("\n#USER.{}.TYPE: {}".format(usern, sosinp))
                logf.write("\n#SYSTEM: Exiting 'RADIO.SH'...")
                logf.close()
            print("Exiting...")
            time.sleep(1)
            clear()
            return
    else:
        if log==True:
            logf=open(path, "a")
            logf.write("\n#USER.{}.TYPE: {}".format(usern, sosinp))
            logf.write("\n#SYSTEM: No signals found.")
            logf.write("\n#SYSTEM: Exiting 'RADIO.SH'...")
            logf.close()
        var1='Searching...'
        clear()
        print("Searching for signals...")
        signalsearch(var1)
        print("No signals found. Exiting...")
        time.sleep(2)
        clear()
        return

def GMS():
    clear()
    print("############################################")
    print("ATTENTION:\n")
    print("This application has been deemed unstable by the S.I.C(Script Integrety Checker)")
    print("Running this script can AND WILL cause serious system corrpution. Run this file at your own risk.")
    return

def GMB():
    clear()
    print("############################################")
    print("                FROM .BASH")
    end=True
    lpass=False
    print("Starting...")
    var1='Accessing GENOME_MATHCER directory(C:/USR/BIO/GM)...'
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="Loading libraries into P.E.E(Protected Execution Environment)..."
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1='Accessing GENOME_MATCHER assets(C:/USR/BIO/GM/ASSETS)...'
    ltime=20
    load(var1, suc, ltime, end, lpass)
    print("Complete")
    print("############################################")
    print("(END GENOME_MATCHER.SH)")
    time.sleep(1)
    return

def GM():
    clear()
    print("Enter Genome below:")
    x=input("Enter Genome here:")
    time.sleep(3)
    os.system("color 0c")
    print("Error: BAD_VARIABLE")
    time.sleep(2)
    print("Error: BAD_VARIABLE")
    time.sleep(1)
    for x in range(40):
        time.sleep(0.1)
        print("Error: BAD_VARIABLE")
    print("!<_HALTING_ALL_PROCESSES_>!")
    time.sleep(2)
    print("Automated failsafe activated. Memory corruption detected.")
    print("This system will now reboot. Please contact your System Administrator.")
    x=input("Press any key to continue...")
    print("REBOOTING...")
    time.sleep(3)
    return

def fridges():
    end=True
    lpass=False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1='Accessing hard drive...'
    ltime=20
    load(var1, suc, ltime, end, lpass)
    end=False
    print("Starting app...")
    var1='Testing connection(DOOR.FIRM)...'
    ltime=20
    lpass=True
    load(var1, suc, ltime, end, lpass)
    lpass=False
    var1='#Starting "FRIDGE_CONFIG.SH(C:/SYS/UTIL)...'
    ltime=30
    end=True
    load(var1, suc, ltime, end, lpass)
    print("############################################")
    print("(END FRIDGE_CONFIG.SH)")
    time.sleep(1)
    return

def fridge():
    clear()
    print("#############################################")
    print("Freezer Interface System ver 3.1.74")
    print("@1987 All rights reserved ENTech LLC.\n")
    print("Welcome to freezer configuration menu!")
    print("To see more info, select an option\n")
    print("Please select an option:")
    print("1.Freezer temperature")
    print("2.Door lock")
    print("3.Air purification")
    print("4.Help")
    return

def fridgetemp(temp):
    print("############################################")
    print("Please select a temperature:\n")
    print("Temp > 30 will spoil all food/samples in one cycle")
    print("Temp <30 can not support living creatures\n")
    print("Current temperature:\n{} degress".format(temp))
    return

def syscorp():
     print("    ___ ")  
     print(" .'/   \ ") 
     print("  / /     \ ")
     print("^| ^|     ^| ")
     print("^| ^|     ^| ") 
     print("^|/`.   .' ")
     print("  `.^|   ^|  ")
     print("  ^|^|___^|  ")
     print("  ^|/___/  ")
     print("  .'.--.  ")
     print(" ^| ^|    ^| ")
     print(" \_\    / ")
     print("  `''--'  ")
     print(" ")
     print("ATTENTION:")
     print("A fatal error has occured. see below for details:")
     print("############################################")
     print("<RAW DATA>\n\nERROR: FATAL_MEMORY_LEAK\nERROR CODE: 0x00491")
     print("-------------BEGIN_MEMORY_DUMP-----------")
     print("HJSNdjbnKJW(8dw88UWNUJN2undjnjww,dWJnjndw")
     print("JNWEJDN7hbchjbIWHUnk3hnbunhOIEWHO*H#IJnkj")
     print("WMNDOU#omoeicjo8jewD465463516#WD454dwda@f")
     print("KLWJNUnhi39jd993inJN#(@(JNkjfnkjenloKMkmw")
     print("KIMWKJLDNKNoujkj3n kjJOJD)jOIn34fo@JDOJnd")
     print("-------------END_MEMORY_DUMP-------------")
     print("MESG:PLEASE CONTACT SYSTEM ADMINISTRATOR FOR MORE ASSISTANCE")
     print("############################################")
     print("\nThis system is unaccessable to protect from further damage.")
     print("Enter your emergency overide code below to start repairs.")
     print("Please contact your security administrator for more info.")
     return

def corp():
    print("ATTENTION:")
    print("This command is currently unavailable due to system corruption.")
    print("Contact your system administrator for assistance.")
    return

def syss():
    clear()
    end=False
    lpass=False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1='Accessing validated system image(C:/SYS/BACKUP)...'
    ltime=20
    end=True
    load(var1, suc, ltime, end, lpass)
    end=False
    print("Shutting down all non-essental processes...")
    var1='#Ending terminal session...'
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1='#Terminating connections....'
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1='#Ending G.U.Is(Graphical User Interface)...'
    ltime=40
    load(var1, suc, ltime, end, lpass)
    var1='#Ending misc. processes...'
    ltime=50
    end=True
    load(var1, suc, ltime, end, lpass)
    var1='Unmounting Local drive(C:)...'
    ltime=50
    load(var1, suc, ltime, end, lpass)
    print("Complete.")
    print("############################################")
    print("(END SYSCHECK.SH)")
    time.sleep(1)
    return

def syscheck():
    clear()
    end=False
    lpass=True
    print("############################################")
    print("System File Checker ver. 3.23.1")
    print("@1987 All rights reserved ENTech LLC.\n")
    print("Diagnossing...")
    print("Hardware Diagnostics...")
    var1='#Disk test...'
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1='#RAM test...'
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1='#CPU test...'
    ltime=30
    load(var1, suc, ltime, end, lpass)
    lpass=False
    var1='Circut connectivity test...'
    ltime=1
    load(var1, suc, ltime, end, lpass)
    lpass=True
    var1='#Loop 1...'
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1='#Loop 2...'
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1='Loop 3...'
    ltime=10
    end=True
    load(var1, suc, ltime, end, lpass)
    print("Hardware Diagnostics completed with:\n#0 Errors")
    print("Software Diagnostics...")
    var1='Checking system image...'
    ltime=70
    loadff()
    print("\nErrors found:")
    print("Memory leakage. Code: 0x00491")
    print("Begening repair...")
    print("Reinstalling system(THIS WILL TAKE A WHILE)...")
    end=False
    lpass=False
    var1="#0%"
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#10%"
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#20%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#30%"
    ltime=40
    load(var1, suc, ltime, end, lpass)
    var1="#40%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#50%"
    ltime=10
    load(var1, suc, ltime, end, lpass)
    var1="#60%"
    ltime=50
    load(var1, suc, ltime, end, lpass)
    var1="#70%"
    ltime=20
    load(var1, suc, ltime, end, lpass)
    var1="#80%"
    ltime=30
    load(var1, suc, ltime, end, lpass)
    var1="#90%"
    ltime=40
    load(var1, suc, ltime, end, lpass)
    print("#100%")
    print(suc)
    print("System has been repaired. This system will now reboot.")
    print("############################################")
    print("(END SYSCHECK.SH)")
    time.sleep(1)
    os.system("color 0a")
    return

def loggh():
    print("###########################################")
    print("Logg collection help:")
    print("\n'log_enable' to enable system wide log collection.")
    print("\n'log_disable' to disable system wide log collection.")
    print("\n'log' to see this message")
    print("###########################################")
    print("What is a log?")
    print("A log is a collection of all inputs and commands inputed on a system.")
    print("Any input and command WILL be inputed to the LOG.txt file.")
    print("Please be aware that this is a MAJOR SECURITY RISK.")
    print("Passwords can be STOLEN this way, so please be carefull.")
    print("Contact your system administrator for more info.")
    print("AND PLEASE RESPECT THE PRIVACY OF YOUR PEERS!")
    print("###########################################")
    return

def logstart(logf):
    logf.write("    ")
    return

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

