from __future__ import print_function
import manualMode,fileHandler,os

class main:
    a=fileHandler.actions()
    mm=manualMode.manual()

    while 1:
        print("Hello and Welcome!\n", end="__________________________\n")

        inp=raw_input("Choose mode: \n\
[ * ] for monitor mode press (1)\n\
[ * ] for manual mode press (2)\n\
[ * ] to exit the program type EXIT\n")
       
        if inp=="EXIT":
            exit()
        if inp=="1" :
            x=raw_input("Choose the interval time between scans (In seconds):")
            if x=="EXIT":
                exit()
            try:
                val=float(x)
            except:
                print("Error: not a number!")
            print("monitor mode:")
            if os.name=='nt':
                import winServices
                winServices.winMonitor.winMonitorState(val)
            elif os.name=='posix':
                import lnxServices
                m=lnxServices.lnxMonitor()
                m.lnxMonitorState(val)

        if inp=="2":
            ts1=raw_input("Enter first dateTime in format of \'DD-MM-YY HOUR:MIN:SEC\'\n")
            if ts1=="EXIT":
                exit()
            ts2=raw_input("Enter second dateTime in format of \'DD-MM-YY HOUR:MIN:SEC\'\n")
            if ts2=="EXIT":
                exit()
            mm.manualState(ts1,ts2)

       
            
