#This module has the animations and cutscenes inside
import time
import os
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

def terror(inp):
    print("Error:\n#'%s' is not a valid command!" % inp)
    return

def lockinfo():
    print("###########################################")
    print("Lockdown Help:")
    print("Command "lockdown" alows you to initilaise/deactivate a system lockdown.\n")
    print("Type "lockdown_int" to activate the lockdown sequence.\n")
    print("Type "lockdown_dis" to deactivate a current lockdown.\n")
    print("Type "lockdown" to see this page.\n")
    print("###########################################")
    print("What is a lockdown?:")
    print("If you activate a system lockdown, all electrical or computerised systems will be put into lockdown")
    print("This means mechanical doors, terminals, radio, ect.")
    print("###########################################")
    print("What do I need to do?:")
    print("Activating a lockdown will prompt you for a password, and conformation.")
    print("PLEASE KEEP THIS PASSWORD AS THE ONLY OTHER WAY TO LIFT A LOCKDOWN IS TO ENTER SECURITY OVERIDE PASSWORD")
    print("The system will reboot, and it will promt you with a password screen to lift the system lockdown.")
    print("###########################################")
    print("How do I deactivate a lockdown?:")
    print("To deactivate a lockdown, enter the password you have set, or enter the security overide password.")
    print("If you enter the security overide password, then you will be logged into the security administrators account.")
    print("If you enter the set password, the security lockdown will be deactivated.")
    print("###########################################")
    return

def lockcon(lockpass, lockconf):
    print("###########################################")
    print("ATTENTION:")
    print("Activating lockdown means access to electrical or computerised systems will be revoked")
    print("The only way to lift a lockdown is to enter password, or security overide password\n")
    print("Please set your security lockdown password below.")
    print("(REMEMBER THIS!!)")
    lockpass=input("Password:")
    print("\nAre you sure?")
    lockconfd=input("(Y/N):")
    if lockconf=='Y' or 'yes' or 'y':
        lockconf=True
        return lockconf lockpass
    if lockconf=='N' or 'n' or 'no':
        return

def lockint(suc):
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    time.sleep(2)
    print("Accessing hardrive...")
    time.sleep(2)
    print(suc)
    print("Initiating lockdown...")
    print("#Editing boot files...")
    time.sleep(2)
    print("#Placing account safeguards...")
    time.sleep(3)
    print("#Sending 'LOCKDOWN' signal to all machinery...")
    time.sleep(4)
    print("#Changing settings...")
    time.sleep(2)
    print(suc)
    print("Encrypting filesystem(this will take awile)...")
    print("#0%")
    time.sleep(2)
    print("#10%")
    time.sleep(3)
    print("#20%")
    time.sleep(1)
    print("#30%")
    time.sleep(4)
    print("#40%")
    time.sleep(1)
    print("#50%")
    time.sleep(1)
    print("#60%")
    time.sleep(5)
    print("#70%")
    time.sleep(2)
    print("#80%")
    time.sleep(3)
    print("#90%")
    time.sleep(4)
    print("#100%")
    print(suc)
    print("Complete. The system will now reboot.")
    time.sleep(2)
    print("############################################")
    print("(END LOCKDOWN.SH)")
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
    print("Are you sure you want to disable lockdown?")
    return

def lockdis(suc):
    print("############################################")
    print("                FROM .BASH")
    print("Starting...")
    time.sleep(2)
    print("Accessing hardrive...")
    time.sleep(2)
    print(suc)
    print("Disabling lockdown...")
    print("#Editing boot files...")
    time.sleep(1)
    print("#Removing account safeguards...")
    time.sleep(3)
    print("#Sending 'DIS_LOCKDOWN' signal to all machinery...")
    time.sleep(4)
    print("#Changing settings...")
    time.sleep(2)
    print(suc)
    print("De-crypting filesystem(this will take awile)...")
    print("#0%")
    time.sleep(2)
    print("#10%")
    time.sleep(3)
    print("#20%")
    time.sleep(1)
    print("#30%")
    time.sleep(4)
    print("#40%")
    time.sleep(1)
    print("#50%")
    time.sleep(1)
    print("#60%")
    time.sleep(5)
    print("#70%")
    time.sleep(2)
    print("#80%")
    time.sleep(3)
    print("#90%")
    time.sleep(4)
    print("#100%")
    print(suc)
    print("Complete. The system will now reboot.")
    time.sleep(2)
    print("############################################")
    print("(END LOCKDOWN_DIS.SH)")
    time.sleep(1)
    return

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

