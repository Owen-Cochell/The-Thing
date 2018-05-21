#This module has the animations and cutscenes inside
import time
suc='#Success!'
def boot(suc):
    #Code for boot up procedure
    print("    ____        __                   __     __ __ ___\n              / __ \__  __/ /_____  ____  _____/ /_   / // /^<  /\n             / / / / / / / __/ __ \/ __ \/ ___/ __/  / // /_/ / \n            / /_/ / /_/ / /_/ /_/ / /_/ (__  ) /_   /__  __/ /  \n            \____/\__,_/\__/ .___/\____/____/\__/     /_/ /_/   \n                          /_/     ")                          
    print("                United States Research Divison    \n                          O.I.M ver. 1.73.48")
    print("Starting system...")
    time.sleep(3)
    print(suc)
    print("Running diagnostics...")
    print("#POST test...")
    time.sleep(2)
    print("#Disk test...")
    time.sleep(3)
    print("#RAM test...")
    time.sleep(1)
    print("#Corrupted file scan...")
    time.sleep(4)
    print(suc)
    time.sleep(1)
    return

def auth(authe, tec, pio, wep, bio, tecp, piop, wepp, biop, usern, passw):
    #authentication backend
    if usern==tec and passw==tecp:
        return authe=True
    if usern==pio and passw==piop:
        return authe=True
    if usern==wep and passw==wepp:
        return authe=True
    if usern==bio and passw==biop:
        return authe=True

def login(suc):
    #Code for starting terminal
    print("############################################################\n                     FROM .BASH                     ")
    print("Starting...")
    print("Accessing harddrive...")
    time.sleep(1)
    print("#Testing 'READ'")      
    time.sleep(1)
    print("Testing 'WRITE'")
    time.sleep(1)
    print(suc)
    print("Accessing 'USERS.SH'(C:\SYS\USR)")
    time.sleep(2)
    print(suc)
    print("Finalising...")
    time.sleep(3)
    print(suc)
    print("###########################################################")
    print("(END LOGIN.SH)")
    time.sleep(1)
    return

def startt(usern):
    #Cod for terminal welcome screen
    print("#############################################")
    print("O.I.M Terminal Interface System ver 3.1.74")
    print("@1987 All rights reserved ENTech LLC.")
    print(" ")
    print("Welcome user %s!")(usern)
    print("Type 'help' for a list of commands")
    return

def help(usern):
    #Code for help command
    print("#####################################")
    print("List of commands:")
    print(" ")
    print("'help' displays this list")
    print("'logout' logs out of user account")
    print("'file' accesses filesystem")
    print("'radio' opens radio app")
    print("'gen_config' opens generator config menu")
    print("'info' to see info on account")
    print("'clear' clears the terminal screen")
    if usern==wep:
        print("'lockdown[int][dec]' to initiate/deactivate security lockdown. Type 'lockdown' for more info")
        print(" ")
        print("####################################")
        return
    if usern==tec:
        print("'logg[enable][disable]' to enable/disable logg collection. Type 'logg' for more info")
        print(" ")
        print("####################################")
        return
    if usern==bio:
        print("'fridge_config' to access fridge configuration menu")
        print(" ")
        print("####################################")
        return
    print("####################################")
    return

def logout(suc):
    print("##############################################")
    print("               FROM .BASH                     ")
    print("Starting...")
    print("Stopping terminal session TERM.SH(C:\SYS\ACCOUNT)")
    time.sleep(3)
    print(suc)
    print("Clearing temporary data...")
    print("#Clearing cach...")
    time.sleep(2)
    print("#Clearing variables...")
    time.sleep(1)
    print("#Clearing user data...")
    time.sleep(1)
    print(suc)
    print("Loading LOGINSCREEN.SH(C:\SYS\ACCOUNT)")
    time.sleep(2)
    print(suc)
    print("#############################################")
    print("(END LOGOUT.SH)")
    return

def files(suc):
    print("############################################")
    print("                FROM .BASH                 ")
    print("Starting...")
    print("Acessing harddrive...")
    print("#Testing READ")
    time.sleep(1)
    print("Testing WRITE")
    time.sleep(2)
    print(suc)
    print("############################################")
    print("(END FILE.SH)")
    time.sleep(1)
    return
    
def file():
    print("###########################################")
    print("File Manager System ver. 1.74.52")
    print("@1987 All rights reserved ENTech LLC.\n")
    print("Welcome to File Manager!")
    print("Below are files that can be veiwed. Enter the file number to view it.")
    print("'.txt' files can be veiwed, but '.enc' are encrypted and can't be viewed without decrypting them first\n")
    return
