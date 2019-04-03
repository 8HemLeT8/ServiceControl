import re
import datetime
import os
from subprocess import Popen, PIPE
import fileHandler
from threads import *
import time




class LnxServices:
    
    def listServices(file,action):
        cmd1 = Popen(["service","--status-all"],stdout=PIPE,stderr=PIPE)
        stdout = cmd1.communicate()[0]
        cmd1.stdout.close()
        services = stdout.split('\n')
        with open(file, action) as f:
            for item in services[:-1]:
                if item[3]=="+":
                    print >> f, (item+"\n")
    listServices("file1.txt","w")
        

class lnxMonitor:
    def lnxMonitorState(self,x):
        myThread=inputThread()
        myThread.start()
        
        print("Linuxxx")
        while myThread.is_alive:

                    print("???")
                    LnxServices.listServices("new.txt","w")
                    fileHandler.actions.detectChanges("new.txt","old.txt",True)
                    while x>0:
                            if myThread.is_alive==False:
                                    return
                            time.sleep(1)
                            x-=1
                    LnxServices.listServices("old.txt","w")
                    fileHandler.actions.detectChanges("old.txt","new.txt",True)












