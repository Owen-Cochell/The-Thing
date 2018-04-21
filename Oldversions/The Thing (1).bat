@echo off
::ENTech System solutions @2018
::This is a beta version of the app
title Outpost 41 Interface system
color 0a
::code for passwords here
::code for lockdown check here
set lock=1
::code for temperature check here
set temp=20
set tec=Windows
set pio=Mcrege
set wep=Gary
set bio=Blair
goto start

:start

::Dialog for boot up procedure(Feel free to put some matinence code here if it affects preformance elseware)
echo    ____        __                   __     __ __ ___
echo   / __ \__  __/ /_____  ____  _____/ /_   / // /^<  /
echo  / / / / / / / __/ __ \/ __ \/ ___/ __/  / // /_/ / 
echo / /_/ / /_/ / /_/ /_/ / /_/ (__  ) /_   /__  __/ /  
echo \____/\__,_/\__/ .___/\____/____/\__/     /_/ /_/   
echo               /_/                               
echo          United States Research Divison    
echo               O.I.M ver. 1.73.48
echo Starting system...
timeout /t 3 >nul
echo #Success!
echo Running diagnostics...
echo #POST test...
timeout /t 2 >nul
echo #Disk test...
timeout /t 3 >nul
echo #RAM Test...
timeout /t 1 >nul
echo #Corrupted file scan...
timeout /t 4 >nul
echo #Success!
echo Establishing connection to server...
timeout /t 2 >nul
echo #Success!
echo Finalising boot procedure...
timeout /t 3 >nul
echo #Success!
timeout /t 1 >nul
goto login

:login

::Login Dialog/code for username validation
if %lock%==2 goto lockdown
cls
echo Please login:
set /p user=Username:
set /p pass=Password:
if %user%==%tec% goto t2
if %user%==%wep% goto t2
if %user%==%pio% goto t2
if %user%==%bio% goto t2
goto lerror

:t2

::code for password validation(Potential security violation more testing required)
if %pass%==%tpass% goto lpros
if %pass%==%wpass% goto lpros
if %pass%==%bpass% goto lpros
if %pass%==%ppass% goto lpros
goto lerror

:lockdown

::code for lockdown dialog
cls
color 0c
echo     ___   
echo  .'/   \  
echo / /     \ 
echo ^| ^|     ^| 
echo ^| ^|     ^| 
echo ^|/`.   .' 
echo  `.^|   ^|  
echo   ^|^|___^|  
echo   ^|/___/  
echo   .'.--.  
echo  ^| ^|    ^| 
echo  \_\    / 
echo   `''--'  
echo.
echo Attention:
echo.
echo A system lockdown has been initiated by your security administrator.
echo All electrical and computerised equipment are now in lockdown, and are not accessable.
echo Please contact your security administrator for more info.
echo.
echo Please enter password or security overide code:
set /p lockp=Password:
if %lockp%==%lpass% goto lockd
if %lockp%==%seco% goto seco
goto loerror

:loerror

::code for incorrect password
cls
echo Error:
echo Incorect password
echo.
echo Please contact your security administrator for more info
pause
goto lockdown

:seco

::code for configuring security account
set user=%wep%
goto lpros

:lpros

::Login Dialog
cls
echo ############################################################
echo                      FROM .BASH
echo Starting...
echo Accessing harddrive...
timeout /t 1 >nul
echo #Testing "READ"
timeout /t 1 >nul
echo #Testing "WRITE"
timeout /t 1 >nul
echo #Success!
echo Accessing "USERS.SF"(C:\SYS\USR)
timeout /t 2 >nul
echo #Success!
echo Finalising...
timeout /t 3 >nul
echo #Success!
echo ###########################################################
echo (END LOGIN.SH)
timeout /t 1 >nul
cls
echo #############################################
echo O.I.M Terminal Interface System ver 3.1.74
echo @1987 All rights reserved ENTech LLC.
echo.
echo Hello user %user%!
echo Type "help" for a list of commands
goto term

:term

::Code for inputing commands
set /p inp=C:\Users\%user%^>^>^>
echo.
goto com

:com

::Master command choice list
if %inp%==help goto help
if %inp%==logout goto logout
if %inp%==file goto file
if %inp%==radio goto radio
if %inp%==gen config goto gen
if %inp%==info goto info
if %inp%==clear goto clear
if %inp%==lockdown goto lock
if %inp%==lockdown_int goto locki
if %inp%==lockdown_dis goto lockd
if %inp%==fridge_config goto fc
goto terror

:help

::Help list
echo #####################################
echo List of commands:
echo.
echo "help" displays this list
echo "logout" logs out of user account
echo "file" accesses filesystem
echo "radio" opens radio app
echo "gen config" opens generator config menu
echo "info" to see info on account
echo "clear" clears the terminal screen
if %user%==%wep% goto weph
if %user%==%tec% goto tech
if %user%==%bio% goto bioh
goto nh

:nh

::Code for if account contains no special commands
echo.
echo ####################################
goto term

:weph

:Code for security commands
echo "lockdown[int][dec]" to initiate/deactivate security lockdown. Type "lockdown" for more info.
echo.
echo ####################################
goto term

:tech

::Code for tech commands
echo "logg[enable][disable]" to enable/disable logg collection. Type "logg" for more info.
echo "syscheck" to run a system check. Will automaticly fix any issues and reboot the system.
echo.
echo ####################################
goto term

:bioh

::Code for biologyst commands
echo "fridge_config" to access fridge configuration menu
echo.
echo ####################################
goto term

:logout

echo Starting "LOGOUT.SH(C:\SYS\ACCOUNT)"...
timeout /t 1 >nul
cls
echo ##############################################
echo                FROM .BASH
echo Starting...
echo Stopping terminal session TERM.SH(C:\SYS\ACCOUNT)
timeout /t 3 >nul
echo #Success!
echo Clearing temporary data...
echo #Clearing cash...
timeout /t 2 >nul
echo #Clearing variables...
timeout /t 1 >nul
echo #Clearing user data...
timeout /t 1 >nul
echo #Success!
echo Loading LOGINSCREEN.SH(C:\SYS\ACCOUNT)...
timeout /t 2 >nul
echo #Success!
echo #############################################
echo (END LOGOUT.SH)
timeout /1 >nul
goto login

:file

echo Starting "FILE.SH(C:\SYS\FILEMAN)"...
timeout /t 1 >nul
cls
echo ############################################
echo                 FROM .BASH
echo Starting...
echo Acessing harddrive...
echo #Testing READ
timeout /t 1 >nul
echo Testing WRITE
timeout /t 2 >nul
echo #Success!
echo ############################################
echo (END FILE.SH)
timeout /t 1 >nul
goto file2

:file2

cls
echo ###########################################
echo File Manager System ver. 1.74.52
echo @1987 All rights reserved ENTech LLC.
echo.
echo Welcome to File Manager!
echo Below are files that can be veiwed. Enter the file number to view it.
echo ".txt" files can be veiwed, but ".enc" are encrypted and can't be viewed without decrypting them first
echo.
echo No files yet
set /p file=Select a number:
::Insert file code here
goto term

:dooro

echo Acessing "DOOR.FIRM"...
echo #Success!

:clear

::code for clearing terminal screen
cls
goto term

:lock

::Lockdown help page
if %user% neq %wep% goto terror
echo ###########################################
echo Lockdown Help:
echo Command "lockdown" alows you to initilaise/deactivate a system lockdown.
echo.
echo Type "lockdown_int" to activate the lockdown sequence.
echo.
echo Type "lockdown_dis" to deactivate a current lockdown.
echo.
echo Type "lockdown" to see this page.
echo.
echo ###########################################
echo What is a lockdown?:
echo If you activate a system lockdown, all electrical or computerised systems will be put into lockdown
echo This means mechanical doors, terminals, radio, ect.
echo ###########################################
echo What do I need to do?:
echo Activating a lockdown will prompt you for a password, and conformation.
echo PLEASE KEEP THIS PASSWORD AS THE ONLY OTHER WAY TO LIFT A LOCKDOWN IS TO ENTER SECURITY OVERIDE PASSWORD
echo The system will reboot, and it will promt you with a password screen to lift the system lockdown.
echo ###########################################
echo How do I deactivate a lockdown?:
echo To deactivate a lockdown, enter the password you have set, or enter the security overide password.
echo If you enter the security overide password, then you will be logged into the security administrators account.
echo If you enter the set password, the security lockdown will be deactivated.
echo ###########################################
goto term

:locki

::Code for activating lockdown procedure
if %user% neq %wep% goto terror
echo ###########################################
echo ATTENTION:
echo Activating lockdown means access to electrical or computerised systems will be revoked
echo The only way to lift a lockdown is to enter password, or security overide password
echo.
echo Enter you security lockdown password below
echo (REMEMBER THIS!!)
set /p lpass=Password: 
echo.
echo Are you sure?
set /p lcon=(Y/N):
if %lcon%==y goto locka
if %lcon%==Y goto locka
if %lcon%==n goto term
if %lcon%==N goto term

:locka

::code for lockdown procedure
echo Starting "LOCKDOWN.SH(C:\SYS\SECURITY")...
timeout /t 1 >nul
cls
echo ############################################
echo                 FROM .BASH
echo Starting...
timeout /t 2 >nul
echo Accessing hardrive...
timeout /t 2 >nul
echo #Success!
echo Initiating lockdown...
echo #Editing boot files...
timeout /t 1 >nul
echo #Placing account safeguards...
timeout /t 3 >nul
echo #Sending "LOCKDOWN" signal to all machinery...
timeout /t 4 >nul
echo #Changing settings...
timeout /t 2 >nul
echo #Success!
echo Encrypting filesystem(this will take awile)...
echo #0%
timeout /t 2 >nul
echo #10%
timeout /t 3 >nul
echo #20%
timeout /t 1 >nul
echo #30%
timeout /t 4 >nul
echo #40%
timeout /t 1 >nul
echo #50%
timeout /t 1 >nul
echo #60%
timeout /t 5 >nul
echo #70%
timeout /t 2 >nul
echo #80%
timeout /t 3 >nul
echo #90%
timeout /t 4 >nul
echo #100%
echo #Success!
echo Complete. The system will now reboot.
timeout /t 2 >nul
echo ############################################
set lock=2
::Code for lockdown here
echo (END LOCKDOWN.SH)
timeout /t 1 >nul
cls
color 0c
goto start

:lockd

::code for disabling lockdown
echo.
echo Are you sure you want to disable lockdown?
set /p dlock=(Y/N):
if %dlock%==Y goto lockdis
if %dlock%==y goto lockdis
if %user%==%wep% goto term
goto lockdown

:lockdis

::Dialog for diabling lockdown
echo Starting "LOCKDOWN_DIS.SH(C:\SYS\SECURITY")...
timeout /t 1 >nul
cls
echo ############################################
echo                 FROM .BASH
echo Starting...
timeout /t 2 >nul
echo Accessing hardrive...
timeout /t 2 >nul
echo #Success!
echo Disabling lockdown...
echo #Editing boot files...
timeout /t 1 >nul
echo #Removing account safeguards...
timeout /t 3 >nul
echo #Sending "DIS_LOCKDOWN" signal to all machinery...
timeout /t 4 >nul
echo #Changing settings...
timeout /t 2 >nul
echo #Success!
echo De-crypting filesystem(this will take awile)...
echo #0%
timeout /t 2 >nul
echo #10%
timeout /t 3 >nul
echo #20%
timeout /t 1 >nul
echo #30%
timeout /t 4 >nul
echo #40%
timeout /t 1 >nul
echo #50%
timeout /t 1 >nul
echo #60%
timeout /t 5 >nul
echo #70%
timeout /t 2 >nul
echo #80%
timeout /t 3 >nul
echo #90%
timeout /t 4 >nul
echo #100%
echo #Success!
echo Complete. The system will now reboot.
timeout /t 2 >nul
echo ############################################
set lock=1
::Code for lockdown here
echo (END LOCKDOWN_DIS.SH)
timeout /t 1 >nul
cls
color 0a
goto start

:fc

::Code for fridge dialog
if %user% neq %bio% goto terror
echo Starting "FRIDGE_CONFIG.SH(C:\SYS\UTIL")...
timeout /t 1 >nul
cls
echo ############################################
echo                 FROM .BASH
echo Starting...
timeout /t 2 >nul
echo Accessing hardrive...
timeout /t 2 >nul
echo #Success!
echo Starting app...
echo #Testing connection...
timeout /t 1 >nul
echo #Starting "FRIDGE_CONFIG.SH(C:\SYS\UTIL)"
timeout /t 2 >nul
echo #Success!
echo Complete
echo ############################################
echo (END FRIDGE_CONFIG.SH)
timeout /t 1 >nul
goto fc2

:fc2

:Code for fridge menu
cls
echo #############################################
echo Freezer Interface System ver 3.1.74
echo @1987 All rights reserved ENTech LLC.
echo.
echo Welcome to freezer configuration menu!
echo To see more info, select an option
echo.
echo Please select an option:
echo 1.Freezer temperature
echo 2.Door lock
echo 3.Air purification
echo 4.Help
echo.
set /p finp=Enter a number:
if %finp%==1 goto FT
if %finp%==2 goto DL
if %finp%==3 goto AP
if %finp%==4 goto FHELP
goto ferror

:FT

::Codefor freezer temperature
cls
echo ############################################
echo Please select a temperature:
echo.
echo Temp ^> 30 will spoil all food/samples in one cycle
echo Temp ^<30 can not support living creatures
echo.
echo Current temperature:
echo %temp% degrees
set /p temp=Please select a temperature:
if %temp% < 0 goto temperror
if %temp% > 50 goto temperror
if %temp% > 30 goto htemp
if %temp% <= 30 goto ltemp
goto temperror

:htemp

::Code for high temperatures
echo Saving settings...
::Code for savng settings
timeout /t 3 >nul
echo Complete. Temperature set to:
echo %temp%
echo Please be aware, after 1 cycle, all food/samples will spoil if you dont raise the temperature.
pause
goto fc2

:ltemp

::Code for low temperatures
echo Saving settings...
::Code for saving settings
timeout /t 3 >nul
echo Complete. Temperature set to:
echo %temp%
echo Please be aware, this temperature can not support life. Any living creatures inside will die.
pause
goto fc2

:DL

::Code for door locks
echo ############################################
echo Please select a option:
echo The door is currently:
::code for door state here
echo.
echo 1.Open door
echo 2.Close door
set /p doors=Please select a number:
if %doors%==1 goto dooro
if %doors%==3 goto doorc

:AP

::Code for air purification here
echo ############################################
echo please select a option:
echo.
echo 1.Purify
echo 2.Select chemical
set /p apure=Select a number:
if %apure%==1 goto pure
if %apure%==2 goto chem

:pure

::code for air purifiction
cls
echo Are you sure?
echo (This will cause burns on any livings subjects inside the freezer)
set /p purop=(Y/N
if %purop%==Y goto airpur
if %purop%==y goto airpur
goto AP

:airpur

::Code for sir purifucation dialog
echo Starting...
timeout /t 2 >nul
echo Loading chem("AIR_PURI")...
timeout /t 3 >nul
echo Spraying...
timeout /t 4 >nul
echo Complete!
pause
goto fc2

:FHELP

::Code for freezer help menu
cls
echo ############################################
echo What is a freezer?:
echo A freezer ia a temperatre controlled enviornment.
echo It is mainly used for storing food and samples, so they don't spoil.
echo ############################################
echo What is temperature control?:
echo This function alows users to change freezer temperature.
echo Anything under 30 degrees farenheight will keep anything from spoling
echo Please keep in mind, a living creature CAN NOT survive in temperatures lower that 20 degrees
echo Anything over 30 degrees will result in spoiled food and samples
echo If food or samples are in over 30 degree temperature, then they will spoil in one cycle
echo Living creatures CAN surrvive in temperatures over 30 degrees
echo ############################################
echo What is Door lock?:
echo This function alows users to lock the freezer door
echo This is ideal for keeping samples and food safe from accidental contaminaion
echo ############################################
echo What is air purification?:
echo Air pirification alows you to spray any chemical(in chemical storage) into the air(inside the freezer only)
echo This is ideal, as using the "AIR_PURI" chemical will kill all bacteria without contaminating food or samples
echo You can spray other chemicals into the air, but this is not recomended, as this may lead to contamination.
echo ############################################
pause
goto fc2

:ferror

::Code for freezer errors
cls
Error:
#%finpu% is not a valid command
pause
goto fc2

:temperror

::Code for temperatur errors
cls
echo Error:
echo #%temp% is not a valid temperature
pause
goto FT

:lerror

::Code for incorect login
cls 
color 0c
echo Error:
echo Incorrect Username or Password
pause
color 0a
goto login

:terror:

::Code fo terminal error
echo Error:
echo "%inp%" is not a valid command
goto term
