# This module has the animations and cutscenes inside
import time
import os
import itertools
import threading
import sys
import winsound
suc = '#Success!'
def boot(suc, corrupt):

    clear()
    # Code for boot up procedure
    lpass = False
    print("+=========================================================================================+\n")
    print("                __         __                   __     __ __  __       \n              / __ \__  __/ /_____  ____  _____/ /_   / // /^/ /\n             / / / / / / / __/ __ \/ __ \/ ___/ __/  / // /_/ / \n            / /_/ / /_/ / /_/ /_/ / /_/ (__  ) /_   /__  __/ /  \n            \____/\____/\__/ .___/\____/____/\__/     /_/ /_/   \n                          /_/     ")
    print("                        United States Research Division    \n                             O.I.M ver. 1.73.48")
    print("+===================+")
    print("|Starting system... |")
    print("+===================+")
    end = False
    var1 = "#Accessing boot files(C:/SYS/boot/)..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#Loading modules..."
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    var1 = "#Initializing P.E.E(Protected Execution Environment)..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#Loading G.U.I(Graphical User Interface)..."
    ltime = 40
    end = True
    load(var1, suc, ltime, end, lpass)
    print("\n+=======================+")
    print("|Running diagnostics... |")
    print("+=======================+")
    lpass = True
    end = False
    var1 = "#CPU test..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#Disk test..."
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    var1 = "#RAM test..."
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#System integrity check..."

    if corrupt:

        loadf()
        print("\nErrors detected. Booting to 'FAILSAFE_PARTITION'...")
        time.sleep(3)
        return

    ltime = 50
    end = True
    load(var1, suc, ltime, end, lpass)
    time.sleep(1)
    lpass = False
    return


def load(var1, suc, ltime, end, lpass):

    intime = 0
    passv = 'PASS'
    sys.stdout.write("\n")

    for m in itertools.cycle(['|', '/', '-', '\\']):

        sys.stdout.write("{}{}\r".format(var1, m))
        sys.stdout.flush()
        time.sleep(0.1)
        intime = intime+1

        if intime == ltime:

            if end:

                if lpass:

                    sys.stdout.write("{}{}\r".format(var1, passv))
                    sys.stdout.flush()

                if not lpass:

                    m = ' '
                    sys.stdout.write("{}{}\r".format(var1, m))
                    sys.stdout.flush()

                print("\n{}".format(suc))
                return

            if not end:

                if lpass:

                    sys.stdout.write("{}{}\r".format(var1, passv))
                    return

                if not lpass:

                    m = ' '
                    sys.stdout.write("{}{}\r".format(var1, m))
                    sys.stdout.flush()
                    return


def loadf():

    ltime = 40
    intime = 0
    passv = 'FAIL'
    sys.stdout.write("\n")

    for m in itertools.cycle(['|', '/', '-', '\\']):

        sys.stdout.write("#System integrity check...{}\r".format(m))
        sys.stdout.flush()
        time.sleep(0.1)
        intime = intime+1

        if intime == ltime:

            sys.stdout.write("#System integrity check...{}\r".format(passv))
            return


def loadff():

    ltime = 70
    intime = 0
    passv = 'FAIL'
    sys.stdout.write("\n")

    for m in itertools.cycle(['|', '/', '-', '\\']):

        sys.stdout.write("#Checking system image...{}\r".format(m))
        sys.stdout.flush()
        time.sleep(0.1)
        intime = intime+1

        if intime == ltime:

            sys.stdout.write("#Checking system image...{}\r".format(passv))
            return


def auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop, usern, passw):

    # authentication backend

    if usern == tec and passw == tecp:

        authe = True
        return authe

    if usern == pio and passw == piop:

        authe = True
        return authe

    if usern == wep and passw == wepp:

        authe = True
        return authe

    if usern == bio and passw == biop:

        authe = True
        return authe

    else:

        authe = False
        return authe


def login(suc):

    # Code for starting terminal
    lpass = False
    print("#########################################"
          "###################\n                     FROM .BASH                     ")
    print("Starting...")
    end = False
    var1 = "Accessing main drive..."
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    lpass = True
    var1 = "#Testing 'READ'..."
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#Testing 'WRITE'..."
    end = True
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    lpass = False
    var1 = "Accessing 'USERS.SH'(C:/SYS/USR)..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "Finalising..."
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    print("###########################################################")
    print("(END LOGIN.SH)")
    time.sleep(1)
    return


def startt(usern):

    # Code for terminal welcome screen
    print("#############################################")
    print("O.I.M Terminal Interface System ver 3.1.74")
    print("@1986 All rights reserved ENTech LLC.")
    print("\nWelcome user {}!".format(usern))
    print("Type 'help' for a list of commands")
    return


def help(usern, wep, pio, bio, tec):

    # Code for help command
    print("#####################################")
    print("List of commands:")
    print(" ")
    print("'help' displays this list")
    print("'logout' logs out of user account")
    print("'music' starts music player")
    print("'file' accesses filesystem")
    print("'radio' opens radio app")
    print("'info' displays info on user account")
    print("'clear' clears the terminal screen")

    if usern == wep:

        print("'log_display' displays the system log")
        print("'lockdown_int' to initiate a security lockdown. Type 'lockdown' for more info")
        print("'detonate_start' to start detonation sequence. Type 'detonate' for more help\n")
        print("####################################")
        return

    if usern == tec:

        print("'log' displays log tools")
        print("'syscheck' to check/repair corrupted files.\n")
        print("####################################")
        return

    if usern == bio:

        print("'log_display' displays the system log")
        # print("'fridge_config' to access fridge configuration menu")
        print("'GENOME_MATCHER' <Err: No definition found>\n")
        print("####################################")
        return
    if usern == pio:

        print("'log_display' displays the system log")
        print("\n####################################")
        return

    return


def logout(suc):

    lpass = False
    end = True
    print("##############################################")
    print("               FROM .BASH                     ")
    print("Starting...")
    var1 = "Stopping terminal session 'TERM.SH(C:\SYS\ACCOUNT)...'"
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    end = False
    print("Clearing temporary data...")
    var1 = "#Clearing cache..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#Clearing variables..."
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#Clearing user data..."
    ltime = 10
    end = True
    load(var1, suc, ltime, end, lpass)
    var1 = "Loading 'LOGINSCREEN.SH(C:/SYS/ACCOUNT)'..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    print("#############################################")
    print("(END LOGOUT.SH)")
    time.sleep(1)
    return


def files(suc):
    end = False
    lpass = False
    print("############################################")
    print("                FROM .BASH                 ")
    print("Starting...")
    var1 = "Accessing main drive..."
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#Testing READ..."
    ltime = 10
    lpass = True
    load(var1, suc, ltime, end, lpass)
    var1 = "#Testing WRITE..."
    ltime = 20
    end = True
    load(var1, suc, ltime, end, lpass)
    print("############################################")
    print("(END FILE.SH)")
    time.sleep(1)
    return


def file(bio, wep, pio, tec, biop, wepp, piop, tecp, emover, freq, logpass):

    while True:

        fiinp = ' '
        clear()
        print("###########################################")
        print("File Manager System ver. 1.74.52")
        print("@1987 All rights reserved ENTech LLC.\n")
        print("Welcome to File Manager!")
        print("Below are files that can be viewed. Enter the file number to view it.")
        print("'.txt' files can be viewed, but '.enc' are encrypted and can't be viewed without decrypting them first\n")
        print("\nPlease select a directory to view:")
        print("1. SYSTEM_LOGS")
        print("2. AUDIO_LOGS")
        print("3. USER_LOGS")
        print("4. Quit")
        fiinp1 = input(">>")

        while fiinp1 == 'SYSTEM_LOGS':

            clear()
            print("###########################################")
            print("SYSTEM_LOGS")
            print("Type 'back' to return to previous directory")
            print("Files:")
            print("\n1. LOG_1.txt")
            print("2. LOG_2.enc")
            print("3. LOG_3.txt\n")
            fiinp = input(">>")

            if fiinp == 'LOG_1.txt':

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
                print("#SYSTEM.WARNING: FILE(GENOME_MATCHER.SH) HAS FAILED INTEGRITY CHECK!")
                print("#SYSTEM.WARNING: RUNNING THIS FILE IS NOT RECOMMENDED!")
                print("#SYSTEM.WARNING: Displaying warning message...")
                print("#USER.{}.TYPE: y".format(bio))
                print("#SYSTEM: Ignoring unstable files...")
                print("#SYSTEM: Starting GENOME_MATCHER.sh...")
                print("#SYSTEM.ERROR: BAD_VARIABLE")
                print("#SYSTEM.ERROR: BAD_VARIABLE")
                print("#SYSTEM.ERROR: BAD_VARIABLE")
                print("#SYSTEM: (Suppressing identical messages)")
                print("#SYSTEM.WARNING: SYSTEM_FAILSAFE ACTIVATED!")
                print("#SYSTEM.WARNING: Restarting...")
                print("#######################<<END_SYSTEM_LOG>>########################")
                x = input("\nPress any key to continue...")
                continue

            if fiinp == 'LOG_2.enc':

                print("This file requires a password to open:")
                lopass = input("\nPassword:")

                if lopass == logpass:
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
                    x=input("\nPress enter to continue...")
                    continue

                else:
                    print("Incorrect password.")
                    x = input("\nPress any key to continue...")
                    continue

            if fiinp == 'LOG_3.txt':

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
                print("#SYSTEM: Setting user to --> {}".format(tec))
                print("#SYSTEM: Starting login procedure...")
                print("#SYSTEM: Login procedure complete!")
                print("#USER.{}.TYPE: file".format(tec))
                print("#SYSTEM: Starting 'FILE.SH'...")
                print("#SYSTEM: Started 'FILE.SH'!")
                print("#USER.{}.TYPE: USER_LOGS".format(tec))
                print("#USER.{}.TYPE: {}_LOG.enc".format(tec, tec))
                print("#SYSTEM: Password required. Prompting...")
                print("#USER.{}.TYPE: {}".format(tec, tecp))
                print("#USER.{}.TYPE: Quit".format(tec))
                print("#USER.{}.TYPE: log_disable".format(tec))
                print("#SYSTEM: Disabling log collection...")
                print("#SYSTEM: Disabled log collection!")
                print("########################<<END_SYSTEM_LOG>>####################################")
                x = input("\nPress any key to continue...")
                fiinp = 'SYSTEM_LOGS'
                continue

            else:

                if fiinp == 'back':

                    break

                print("\nInvalid file.\n")
                x = input("Press enter to continue...")
                continue

        while fiinp1 == 'AUDIO_LOGS':

            clear()
            print("###########################################")
            print("AUDIO_LOGS")
            print("Type 'back' to return to previous directory")
            print("Files:")
            print("\n1. AUDIO_LOG_1.txt")
            print("2. AUDIO_LOG_2.txt")
            print("3. AUDIO_LOG_3.txt")
            fiinp = input(">>")

            if fiinp == 'AUDIO_LOG_1.txt':

                print("\n####################<<BEGIN_AUDIO_LOG>>##########################")
                print("Time: 14:38:34")
                print("Date: 10/2/1986")
                print("#####################################")
                print("#VOICE.1: Hey {}".format(tec))
                print("#VOICE.2: What?")
                print("#VOICE.1: What's the [REDACTED] for the [REDACTED]?")
                print("#VOICE.2: Oh, it's {} gigahertz".format(freq))
                print("#VOICE.1: Thanks.")
                print("#################<<END_AUDIO_LOG>>###############################")
                x = input("\nPress enter to continue...")
                continue

            if fiinp == 'AUDIO_LOG_2.txt':

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
                print("VOICE.1: Turn that shit off! It's very unsophisticated!")
                print("<SPEAKER_VOlUME_INCREASE>")
                print("VOICE.1: [REDACTED]!")
                print("##################<<END_AUDIO_LOG>>#############################")
                x = input("\nPress enter to continue...")
                continue

            if fiinp == 'AUDIO_LOG_3.txt':
                print("\n####################<<BEGIN_AUDIO_LOG>>##########################")
                print("Time: 15:56:24")
                print("Date: 10/5/1986")
                print("#####################################")
                print("#VOICE.1: Holy shit, {}! What the hell is that?".format(pio))
                print("#VOICE.2: Don't know. Found it at the site. With the distress beacon.")
                print("#VOICE.3: What...")
                print("#VOICE.4: DON'T TOUCH IT! Do you know how many safety protocols we are breaking?")
                print("#VOICE.2: Relax, {}. I just thought {} would like to have a look at it.".format(wep, bio))
                print("#VOICE.3: You thought correctly. Let's take a gander...")
                print("<No voice captures detected for 3 minutes>")
                print("#VOICE.3: Well, by the looks of it, it's obviously a [REDACTED].")
                print("#VOICE.4: What the hell is that supposed to mean?")
                print("#VOICE.3: It has [REDACTED] amount of [REDACTED]. "
                      "Very uncanny biology. Never seen anything like this before...")
                print("#VOICE.1: English, {}.".format(bio))
                print("#VOICE.3: This thing's not from around here. None of these organs seem to [REDACTED].")
                print("#VOCIE.4: We need to keep an eye on this, thing, and report it to HQ.")
                print("#VOICE.1: Roger. I'll get to it.")
                print("#VOICE.4: {}, keep this thing in the freezer until further notice.".format(bio))
                print("#VOICE.3: Roger that, {}.".format(wep))
                print("####################<<END_AUDIO_LOG>>###########################")
                x = input("\nPress enter to continue...")
                continue

            else:

                if fiinp == 'back':

                    break

                print("\nInvalid file.")
                x = input("\nPress enter to continue...")
                continue

        while fiinp1 == 'USER_LOGS':

            clear()
            print("###########################################")
            print("User-Logs")
            print("Type 'back' to return to previous directory")
            print("Default security configurations are in effect.")
            print("The password to each log is the user password.")
            print("Files:")
            print("\n1. {}_LOG.enc".format(bio))
            print("2. {}_LOG.txt".format(pio))
            print("3. {}_LOG.enc".format(wep))
            print("4. {}_LOG.enc".format(tec))
            fiinp = input(">>")

            if fiinp == bio + '_LOG.enc':

                print("This file requires a password to open:")
                lopass = input("\nPassword:")

                if lopass == biop:

                    print("\n########################################################")
                    print("Secure log system ver 3.24.8:")
                    print("(DATE AND TIME DISABLED)\n")
                    print("ENTRY 1:\n")
                    print("    This is {}, head biologist of Outpost 41. This place seems, quiet. I'm not gonna be doing much around here besides checking the samples in the freezer. "
                          "\nGonna be a hellava boring 9 months. at least I have this computer to write down my thoughts.\n".format(bio))
                    print("ENTRY 2:\n")
                    print("    I hate {}. He's an annoying piece of shit. He keeps 'messing around' with my logs, and constantly screws up the testing environment. "
                          "\nHe compromised 3 microorganism colonies already! And he keeps playing that same, goddamn song. "
                          "\nJesus, if I have to put up with his shit much longer, i'll take my chances out in the frozen wasteland. Better than being copped up with {}.\n".format(tec, tec))
                    print("ENTRY 3:\n")
                    print("    We found... something. {} came back from a scouting mission investigating another research outpost emitting a distress call. He found this... strange lifeform. "
                          "\nIt appears to have human organs, but dose not appear to be human. "
                          "\nIt has multiple limbs(perhaps 'appendages' would be more accurate), and appears, to have... dog fur. Also, upon further genetic testing, I found that some cells are still alive. "
                          "\nThey are in some form of hibernation, most likely from the cold. I saved a few samples for analysis. Perhaps this will give me something to pass the time.\n".format(pio))
                    print("########################################################")
                    x = input("\nPress enter to continue...")
                    continue

                else:

                    print("\nIncorrect password.")
                    x = input("\nPress enter to continue...")
                    continue

            if fiinp == pio + '_LOG.txt':

                print("\n########################################################")
                print("Secure log system ver 3.24.8")
                print("(DATE AND TIME DISABLED)\n")
                print("ENTRY 1:\n")
                print("    This is stupid. I'm not using this shit.\n")
                print("########################################################")
                x = input("\nPress any key to continue...")
                continue

            if fiinp == wep + '_LOG.enc':

                print("\nThis file requires a password to open:")
                lopass = input("\nPassword:")

                if lopass == wepp:

                    print("\n########################################################")
                    print("Secure log system ver 3.24.8")
                    print("(DATE AND TIME DISABLED)\n")
                    print("ENTRY 1:\n")
                    print("    The men under my command are, well, interesting to say the least. They range from ignorant and immature, to arrogant and pompous. Keeping these men under control will be a challenge.\n")
                    print("ENTRY 2:\n")
                    print("    I need to find a safe place to keep my gun key. {} has been asking to distribute them, so the men can defend themselves in an emergency. "
                          "\nI don't know what could possibly happen out here, but arming the entire staff of this facility is NOT a good idea.\n".format(pio))
                    print("ENTRY 3:\n")
                    print("    I took the liberty of securing logs with sensitive info inside. Don't want my boys to get into something they shouldn't be seeing. "
                          "\nFor future reference, the password is: {}.\n".format(logpass))
                    print("ENTRY 4:\n")
                    print("    {} brought back something interesting from his scouting mission. According to {}, it's a lifeform he has never seen before. "
                          "\nWell, it disappeared from the freezer. We found it outside the facility, crawling around. It seemed like it didn't know how to use it's body, like it was still learning. "
                          "\nIt was stumbling around and falling over its self. We torched it. It died immediately. Everyone is on edge now, nobody knows what to think anymore.\n".format(pio, bio))
                    print("########################################################")
                    x = input("\nPress enter to continue...")
                    continue

                else:

                    print("\nIncorrect password.")
                    x = input("\nPress enter to continue...")
                    continue

            if fiinp==tec + '_LOG.enc':

                print("\nThis file requires a password to open:")
                lopass = input("\nPassword:")

                if lopass == tecp:

                    print("\n########################################################")
                    print("Secure log system ver 3.24.8")
                    print("(DATE AND TIME DISABLED)\n")
                    print("ENTRY 1:\n")
                    print("	Wow. A shitty journal app on a shitty computer in a shitty outpost in the middle of fucking nowhere. This is gonna be the most boring job yet. And that's saying something! "
                          "\nYou should have seen it when I was the system administrator for some company I was working with. All I did was change the ink on the photo copier. "
                          "\nNow, i'm going to be using this computer system to manage an outpost with little to no interest to anybody at D.C. Woopie.\n")
                    print("ENTRY 2:\n")
                    print("	Goddamn it, little bastards are smarter than I thought. {}, the biologist, somehow managed to figure out how to make scripts with 'notepad.sh'. "
                          "\nUnfortunately, he has no idea what he's doing. "
                          "\nHis app isn't correctly compiled, which leads to memory leakage from invalid variables created by the script. "
                          "\nHe crashed the whole system. Had to do a complete reinstall. It's a wonder that I was able to recover all of our data. "
                          "\nGonna have to tighten up security on P.E.E(Protected Execution Environment. A unfortunate nickname, I know), disable 'notepad.sh', and give a stern talking to to {}. Little shit managed to waste a good 4 hours of my time.\n".format(bio, bio))
                    print("ENTRY 3:\n")
                    print("	They did it again. {} somehow managed to get in my account, enable log collection, and get the credentials to unlock most of the encrypted documents. "
                          "\nI'm guessing he just wanted to keep a better eye on us. "
                          "\nA little tyrannical though, don't you think? I mean, I know he's the boss and all, but dosen't he have any respect for privacy? "
                          "\nAnyway, I disabled log collection on the files app and restricted log control to my account. But not before I get some passwords for payback ;)\n".format(wep))
                    print("ENTRY 4:\n")
                    print("	List of log credentials:")
                    print("	#pio:N/A")
                    print("	#wep: {}".format(wepp))
                    print("	#bio: {}\n".format(biop))
                    print("ENTRY 5:\n")
                    print("	So I managed to make a music player for the guys. They like the fact that they can play their own songs. Thought it would boost moral a bit.\n")
                    print("ENTRY 6:\n")
                    print("	OH SHIT OH GOD HOLY FUCK I WENt IntO THE FREEZER AND IT WAS GONE! THE FUCKINg BODY IS FUCKINg gONE!!! HOLY SHIt I thOUGHT IT WAS DEAD... I gotta tell somebody about this...\n")
                    print("##################################################")
                    x = input("\nPress enter to continue...")
                    continue

                else:

                    print("\nIncorrect password.")
                    x = input("\nPress enter to continue...")
                    continue

            else:

                if fiinp == 'back':

                    break

                print("\nInvalid file.")
                x = input("\nPress enter to continue...")
                continue

        if fiinp1 == 'Quit':

            print("Exiting...")
            time.sleep(1)
            clear()
            return

        else:

            if fiinp == 'back':

                continue

            print("\nInvalid file.")
            x = input("\nPress enter to continue...")
            continue


def uinfo(usern, log, tec, bio, pio, wep):

    print("#####################################")
    print("Username: {}".format(usern))

    if usern == wep:

        role = 'Security Administrator'

    if usern == bio:

        role = 'Biologist'

    if usern == pio:

        role = 'Pilot'

    if usern == tec:

        role = 'System Administrator'

    print("Role: {}".format(role))
    print("System Version: 1.73.48")

    if usern == wep:

        logt = '10/28/1986'

    if usern == bio:

        logt = '10/29/1986'

    if usern == pio:

        logt = '6/14/1986'

    if usern == tec:

        logt = '10/29/1986'

    print("Last Login: {}".format(logt))
    print("System Management: United States Research Division")

    if log:

        print("(Log collection is ON!)")
    print("#####################################")
    return


def terror(inp, log, path):

    if log:

        logf = open(path, "a")
        logf.write("\n#SYSTEM: Invalid command!")
        logf.close()

    print("Error:\n#'{}' is not a valid command!".format(inp))
    return


def lockinfo():
    print("###########################################")
    print("Lockdown Help:")
    print("Command 'lockdown' allows you to initiate/deactivate a system lockdown.\n")
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
    print("PLEASE KEEP THIS PASSWORD AS THE ONLY OTHER WAY TO LIFT A LOCKDOWN IS TO ENTER SECURITY OVERRIDE PASSWORD")
    print("The system will reboot, and it will prompt you with a password screen to lift the system lockdown.")
    print("###########################################")
    print("How do I deactivate a lockdown?:")
    print("To deactivate a lockdown, enter the password you have set, or enter the security override password.")
    print("If you enter the security overide password, then you will be able to deactivate the security lockdown.")
    print("If you enter the set password, the security lockdown will be deactivated.")
    print("###########################################")
    return


def lockcon(lockpass, lockconf):

    print("###########################################")
    print("ATTENTION:")
    print("Activating lockdown means access to electrical and computerised systems will be revoked")
    print("The only way to lift a lockdown is to enter set password, or security override password\n")
    print("Please set your security lockdown password below.")
    print("(REMEMBER THIS!!)")


def lockint(suc):

    end = True
    lpass = False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1 = "Accessing main drive..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    end = False
    print("Initiating lockdown...")
    var1 = "#Editing boot files..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#Placing account safeguards..."
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#Sending 'LOCKDOWN' signal to all machinery..."
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    var1 = "#Changing settings..."
    ltime = 20
    end = True
    load(var1, suc, ltime, end, lpass)
    end = False
    print("Encrypting filesystem(this will take a while)...")
    var1 = "#0%"
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#10%"
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#20%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#30%"
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    var1 = "#40%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#50%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#60%"
    ltime = 50
    load(var1, suc, ltime, end, lpass)
    var1 = "#70%"
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#80%"
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#90%"
    ltime = 40
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

    print("+=========================================================================+")
    print("                                  ___   ")
    print("                               .'/   \  ")
    print("                              / /     \ ")
    print("                              | |     | ")
    print("                              | |     | ")
    print("                              |/`.   .' ")
    print("                               `.|   |  ")
    print("                                ||___|  ")
    print("                               |/___/  ")
    print("                               .'.--.  ")
    print("                              | |    | ")
    print("                              \_\    / ")
    print("                               `''--' ")
    print("\nAttention:\n")
    print("A system lockdown has been initiated by your security administrator.")
    print("All electrical and computerised equipment are now in lockdown, and are now inaccessible.")
    print("To view system logs, enter '!log_display!' to display system logs")
    print("Please contact your security administrator for more info.\n")
    return


def lerror(lockinp):

    print("\nIncorrect password!\nPlease contact your security administrator for more info.")
    x = input("\nPress enter to continue...")
    return


def lockconf2():
    print("\nAre you sure you want to disable the lockdown?")
    return


def lockdis(suc):

    end = True
    lpass = False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    time.sleep(2)
    var1="Accessing main drive..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    end = False
    print("Disabling lockdown...")
    var1 = "#Editing boot files..."
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#Removing account safeguards..."
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#Sending 'DIS_LOCKDOWN' signal to all machinery..."
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    var1="#Changing settings..."
    ltime = 20
    end = True
    load(var1, suc, ltime, end, lpass)
    end = False
    print("Decrypting filesystem(this will take a while)...")
    var1 = "#0%"
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#10%"
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#20%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#30%"
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    var1 = "#40%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#50%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#60%"
    ltime = 50
    load(var1, suc, ltime, end, lpass)
    var1 = "#70%"
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#80%"
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#90%"
    ltime = 40
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

    end = True
    lpass = False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1="Accessing music player directory(C:/USR/TECHNICAL/MUSIC_PLAY)..."
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "Loading libraries into P.E.E(Protected Execution Environment)..."
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "Finding music directory(C:/USR/TECHNICAL/MUSIC)..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    print("############################################")
    print("(END MUSIC.SH)")
    time.sleep(1)
    return


def music(tec, bio, pio, wep):

    clear()
    print("############################################")
    print("Music Player Ver. 2.7.5")
    print("Welcome to the music player fellas.\nThis app was made by {}(you're welcome)\nPeople's songs are separated by directories.\nJam on boys!".format(tec))
    print("")
    print("Please select a directory:")
    print("1. {}'s Jams\n2. {}'s Songs\n3. {}'s Songs\n4. {}'s Songs\n5. Stop current song\n6. Quit".format(tec, bio, pio, wep))
    return


def tecmus(tec):

    end = False
    lpass = False

    while True:

        clear()
        print("############################################")
        print("{}'s Jams".format(tec))
        print("Type 'back' to return to the previous directory")
        print("\n1. Let's do the time warp again\n2. Lucy in the sky with diamonds")
        musicinp2 = input("Select a number:")

        if musicinp2 == '1':

            var1 = "Playing 'Let's do the time warp again'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            clear()
            winsound.PlaySound("time warp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            return

        if musicinp2 == '2':

            var1 = "Playing 'Lucy in the sky with diamonds'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("lucy in the sky with diamonds.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        else:

            if musicinp2 == 'back':

                return

            print("Invalid option!")
            x = input("\nPress enter to continue...")
            continue


def biomus(bio):

    end = False
    lpass = False

    while True:

        clear()
        print("############################################")
        print("{}'s Songs".format(bio))
        print("Type 'back' to return to the previous directory.")
        print("\n1. The fair at Sorochyntsi\n2. Samson and Delila Bacchanale\n3. Jupiter, Bringer of Jollity")
        musicinp2 = input("Select a number:")

        if musicinp2 == '1':

            var1 = "Playing 'The fair at Sorochyntsi'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("the fair at stroncoskey.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '2':

            var1 = "Playing 'Samson and Delila Bacchanal'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("bacchanel.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '3':

            var1 = "Playing 'Jupiter, Bringer of Jollity'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("jupiter.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        else:

            if musicinp2 == 'back':

                return

            print("Invalid option!")
            x = input("\nPress enter to continue...")
            continue


def piomus(pio):

    end = False
    lpass = False

    while True:

        clear()
        print("############################################")
        print("{}'s Songs".format(pio))
        print("Type 'back' to return to the previous directory\n")
        print("1. Jailhouse Rock\n2. If you leave me now\n3. Messaround\n4. Anything goes\n5. Orange sky\n6. Superstition")
        musicinp2 = input("Select a number:")

        if musicinp2 == '1':

            var1 = "Playing 'Jailhouse Rock'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("jailhouse rock.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '2':

            var1 = "Playing 'If you leave me now'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("if you leave me now.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '3':

            var1 = "Playing 'Messaround'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("messaround.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '4':

            var1 = "Playing 'Anything goes'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("anything goes.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '5':

            var1 = "Playing 'Orange Colored Sky'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("orange colored sky.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '6':

            var1 = "Playing 'Superstition'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("superstition.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        else:

            if musicinp2 == 'back':

                return

            print("Invalid option!")
            x = input("\nPress enter to continue...")
            continue


def wepmus(wep):

    end = False
    lpass = False

    while True:

        clear()
        print("############################################")
        print("{}'s Songs".format(wep))
        print("Type 'back' to return to the previous directory.\n")
        print("1. Video Killed the radio star\n2. September\n3. You make my dreams come true\n4. Don't you forget about me\n5. Wild Wild Life\n6. Jump")
        musicinp2 = input("Select a number:")

        if musicinp2=='1':

            var1 = "Playing 'Video killed the radio star'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("killed the radio star.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '2':

            var1 = "Playing 'September'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("September.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '3':

            var1 = "Playing 'You make my dreams come true'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("you make my dreams come true.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '4':

            var1 = "Playing 'Don't you forget about me'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("dont forget.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '5':

            var1 = "Playing 'Wild Wild Life'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("wild life.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            return

        if musicinp2 == '6':

            var1 = "Playing 'Jump'..."
            ltime = 20
            load(var1, suc, ltime, end, lpass)
            winsound.PlaySound("jump.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            clear()
            # Code for playing music here
            return

        else:

            if musicinp2 == 'back':

                return

            print("Invalid option!")
            x = input("Press enter to continue...")
            continue


def signalsearch(var1):
    intime = 0

    for m in itertools.cycle(['|', '/', '-', '\\']):

        sys.stdout.write("\r{}{}".format(var1, m))
        sys.stdout.flush()
        time.sleep(0.1)
        intime = intime+1

        if intime == 20:

            print("\n")
            break


def radios(suc):
    end = True
    lpass = False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1 = "Accessing disk..."
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    end = False
    print("Prepping system...")
    var1 = "#Loading radio firmware(C:/SYS/FIM/RAD/)..."
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#Finding and configuring broadcast equipment..."
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#Testing connection..."
    ltime = 30
    end = True
    lpass = True
    load(var1, suc, ltime, end, lpass)
    print("############################################")
    print("(END RADIO.SH)")
    time.sleep(1)
    return


def radio(freq, optiony, optionn, log, usern, path):

    while True:

        print("############################################")
        print("Radio Interface System ver. 3.3.8")
        print("@1986 All Rights Reserved ENTech LLC.")
        print("Welcome to the Radio Interface System!")
        print("Type 'Quit' to quit the application")
        print("Please Enter a frequency below to start broadcasting:\n")
        freqinp = input("Enter a frequency:")

        if log:

            logf = open(path, "a")
            logf.write("\n#USER.{}.TYPE: {}".format(usern, freqinp))
            logf.close()

        if freqinp == freq:

            if log:

                logf = open(path, "a")
                logf.write("\n#SYSTEM: Signal acquired!")
                logf.close()

            var1='Searching...'
            clear()
            print("Searching for signals...")
            signalsearch(var1)
            print("Signal acquired!")
            print("\nConnection to 'Automated Relay Station 1156' established!")
            print("Do you want to broadcast a 'SOS' alert?")
            sosinp = input("(Y/N):")

            if sosinp in optiony:

                if log:

                    logf = open(path, "a")
                    logf.write("\n#USER.{}.TYPE: {}".format(usern, sosinp))
                    logf.write("\n#SYSTEM: Broadcasting SOS alert...")
                    logf.write("\n#SYSTEM: Acquired response!")
                    logf.write("\n#SYSTEM: Displaying 'PROTOCOL_1194'")
                    logf.close()

                # Code for radio backend here
                end = False
                lpass = False
                var1 = "Broadcasting 'SOS' alert..."
                ltime = 40
                load(var1, suc, ltime, end, lpass)
                print("\nAcquired response!")
                print("Displaying response:")
                print("\n(BEGIN MESSAGE:)")
                print("+===========================================+")
                print("|(5/19/1986, 05:27:06)                      |")
                print("|Automated Relay Station 1156               |")
                print("|This is a automated message(CODE 1194)     |")
                print("|Reinforcements inbound. Arriving in 2 days.|")
                print("|Evacuating all crew and staff upon arrival |")
                print("+===========================================+")
                print("(END MESSAGE)")
                x = input("\nPress enter to continue...")
                print("This message has been sent with a protocol code(1194).\nDisplaying instructions below:")
                print("\n############################################")
                print("Protocol code: 1194\nProtocol name: Evacuation protocol")
                print("Instructions:\n1. Gather all research documents/specimens(IF POSSIBLE).")
                print("2. Inform/prepare all crew and staff for evacuation.")
                print("3. Gather all class C and above materials(IF POSSIBLE). Personal belongings are NOT to be brought.")
                print("4. Prepare landing pad")
                print("The evacuation team will be arriving in TWO DAYS.\nPlease have these tasks completed upon arrival.")
                print("############################################")
                x = input("Press enter to continue...")
                print("Exiting...")
                time.sleep(2)
                clear()
                return

            if sosinp in optionn:

                if log:

                    logf = open(path, "a")
                    logf.write("\n#USER.{}.TYPE: {}".format(usern, sosinp))
                    logf.write("\n#SYSTEM: Exiting 'RADIO.SH'...")
                    logf.close()

                print("Exiting...")
                time.sleep(1)
                clear()
                return

        else:

            if freqinp == 'Quit':

                if log:

                    logf = open(path, "a")
                    logf.write("\n#SYSTEM: 'Exiting RADIO.SH'...")
                    logf.close()

                print("Exiting...")
                time.sleep(3)
                clear()
                return

            if log:

                logf = open(path, "a")
                logf.write("\n#SYSTEM: No signals found.")
                logf.write("\n#SYSTEM: Prompting user...")
                logf.close()

            var1 = 'Searching...'
            clear()
            print("Searching for signals...")
            signalsearch(var1)
            print("No signals found.")
            print("\nDo you want to exit?:")
            radiox = input("(Y/N):")

            if radiox in optiony:

                if log:

                    logf = open(path, "a")
                    logf.write("\n#USER.{}.TYPE: {}".format(usern, sosinp))
                    logf.write("\n#SYSTEM: Exiting 'RADIO.SH'...")
                    logf.close()

                print("Exiting...")
                time.sleep(2)
                clear()
                return

            if radiox in optionn:

                if log:

                    logf = open(path, "a")
                    logf.write("\n#USER.{}.TYPE: {}".format(usern, sosinp))
                    logf.close()

                clear()
                continue


def GMS():

    clear()
    print("############################################")
    print("ATTENTION:\n")
    print("This application has been deemed unstable by the S.I.C(Script Integrity Checker)")
    print("Running this script can AND WILL cause serious system corruption. Run this file at your own risk.")
    return


def GMB():

    clear()
    print("############################################")
    print("                FROM .BASH")
    end = True
    lpass = False
    print("Starting...")
    var1 = 'Accessing GENOME_MATCHER directory(C:/USR/BIO/GM)...'
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "Loading libraries into P.E.E(Protected Execution Environment)..."
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = 'Accessing GENOME_MATCHER assets(C:/USR/BIO/GM/ASSETS)...'
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    print("Complete")
    print("############################################")
    print("(END GENOME_MATCHER.SH)")
    time.sleep(1)
    return


def GM():
    clear()
    print("Enter Genome below:")
    x = input("Enter Genome here:")
    time.sleep(3)
    os.system("color 0c")
    print("Error: BAD_VARIABLE")
    time.sleep(2)
    print("Error: BAD_VARIABLE")
    time.sleep(1)

    for x in range(40):
        time.sleep(0.01)
        print("Error: BAD_VARIABLE")

    print("!<_HALTING_ALL_PROCESSES_>!")
    time.sleep(2)
    print("Automated fail-safe activated. Memory corruption detected.")
    print("This system will now reboot. Please contact your System Administrator.")
    x = input("\nPress enter to continue...")
    print("REBOOTING...")
    time.sleep(3)
    return


def syscorp():
    print("+=========================================================================+")
    print("                                  ___   ")
    print("                               .'/   \  ")
    print("                              / /     \ ")
    print("                              | |     | ")
    print("                              | |     | ")
    print("                              |/`.   .' ")
    print("                               `.|   |  ")
    print("                                ||___|  ")
    print("                               |/___/  ")
    print("                               .'.--.  ")
    print("                              | |    | ")
    print("                              \_\    / ")
    print("                               `''--' ")
    print("\nATTENTION:")
    print("A fatal error has occurred. see below for details:\n")
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
    print("\n############################################")
    print("\nThis system is inaccessible to protect from further damage.")
    print("Enter your emergency override code below to access the system.")
    print("Enter '!log_display!' to display system logs.")
    print("Please contact your security administrator for more info.")
    return


def corp():
    print("ATTENTION:")
    print("This command is currently unavailable due to system corruption.")
    print("Contact your system administrator for assistance.")
    return


def syss():

    clear()
    end = False
    lpass = False
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    var1 = 'Accessing validated system image(C:/SYS/BACKUP)...'
    ltime = 20
    end = True
    load(var1, suc, ltime, end, lpass)
    end = False
    print("Shutting down all non-essential processes...")
    var1 = '#Ending terminal session...'
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = '#Terminating connections....'
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = '#Ending G.U.Is(Graphical User Interface)...'
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    var1 = '#Ending misc. processes...'
    ltime = 50
    end = True
    load(var1, suc, ltime, end, lpass)
    var1 = 'Unmounting Local drive(C:)...'
    ltime = 50
    load(var1, suc, ltime, end, lpass)
    print("Complete.")
    print("############################################")
    print("(END SYSCHECK.SH)")
    time.sleep(1)
    return


def syscheck(corrupt):

    clear()
    end = False
    lpass = True
    print("############################################")
    print("System File Checker ver. 3.23.1")
    print("@1987 All rights reserved ENTech LLC.\n")
    print("Diagnosing...")
    print("Hardware Diagnostics...")
    var1 = '#Disk test...'
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = '#RAM test...'
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = '#CPU test...'
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    lpass = False
    var1='Circuit connectivity test...'
    ltime = 1
    load(var1, suc, ltime, end, lpass)
    lpass = True
    var1 = '#Loop 1...'
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = '#Loop 2...'
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = '#Loop 3...'
    ltime = 10
    end = True
    load(var1, suc, ltime, end, lpass)
    print("Hardware Diagnostics completed with:\n#0 Errors")
    print("Software Diagnostics...")

    if not corrupt:

        var1 = '#Checking system image...'
        ltime = 70
        lpass = True
        end = True
        load(var1, suc, ltime, end, lpass)
        print("\nSoftware Diagnostics completed with:\n#0 Errors")
        x = input("\nPress enter to continue...")
        print("No errors found! Exiting...")
        time.sleep(3)
        return

    loadff()
    print("\nSoftware Diagnostics completed with:\n#1 Errors")
    print("\nErrors found:")
    print("Memory leakage. Code: 0x00491")
    print("Beginning repair...")
    print("Re-imaging system(THIS WILL TAKE A LONG TIME)...")
    end = False
    lpass = False
    var1 = "#0%"
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#10%"
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#20%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#30%"
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    var1 = "#40%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#50%"
    ltime = 10
    load(var1, suc, ltime, end, lpass)
    var1 = "#60%"
    ltime = 50
    load(var1, suc, ltime, end, lpass)
    var1 = "#70%"
    ltime = 20
    load(var1, suc, ltime, end, lpass)
    var1 = "#80%"
    ltime = 30
    load(var1, suc, ltime, end, lpass)
    var1 = "#90%"
    ltime = 40
    load(var1, suc, ltime, end, lpass)
    print("#100%")
    print(suc)
    print("System repair successful! The system will now reboot.")
    print("############################################")
    print("(END SYSCHECK.SH)")
    time.sleep(1)
    os.system("color 0a")
    return


def loggh():
    print("###########################################")
    print("Log collection help:")
    print("\n'log_display' to display the system log")
    print("\n'log_enable' to enable system wide log collection.")
    print("\n'log_disable' to disable system wide log collection.")
    print("\n'log_clear' to clear the system log")
    print("\n'log' to see this message")
    print("###########################################")
    print("What is a log?")
    print("A log is a collection of all inputs and commands inputted on a system.")
    print("Any input and command WILL be inputted to the LOG.txt file.")
    print("Please be aware that this is a MAJOR SECURITY RISK.")
    print("Passwords can be STOLEN this way, so please be careful.")
    print("Contact your system administrator for more info.")
    print("AND PLEASE RESPECT THE PRIVACY OF YOUR PEERS!")
    print("###########################################")
    return


def logstart(path):

    logf = open(path, "w")
    logf.write("")
    logf.close()
    return


def logdis(path, log):

    if log:

        logf = open(path, "a")
        logf.write("\n#SYSTEM: Displaying log...")
        logf.close()

    clear()
    print("+=========================================================================================+")
    print("                                -= System log: =-\n")
    logf = open(path, "r")
    contents = logf.read()
    print(contents)
    logf.close()
    x = input("\nPress enter to continue...")
    clear()
    return


def clear():

    os.system('cls' if os.name == 'nt' else 'clear')
    return

