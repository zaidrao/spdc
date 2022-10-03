import os, platform, time
#os.system("clear")
#print(" updating ")
#exit()
#os.system("cd $HOME/")
#os.system("termux-setup-storage")
#os.system("xdg-open https://www.facebook.com/groups/660205018582939")
#time.sleep(5)
#os.system("xdg-open https://www.facebook.com/aahilrana4072")
try:
    import requests
except(ImportError):
    os.system("pip install requests")

rana=platform.architecture()[0]
try:
    if rana=="32bit":
        exit(' 32 bit not executeble ')
        __import__("tok32").aahil_main_menu()
    elif rana=="64bit":
        #exit(' 32 bit not executeble ')
        __import__("spd").rsa_defence_system()
    else:
        print(" We have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if rana == "32bit":
        exit(' 32 bit not executeble ')
        import tok32
        tok32.aahil_main_menu
    elif rana == "64bit":
        import spd
        spd.rsa_defence_system()
    else:
        print(" We have issue to launch script")
        exit()
