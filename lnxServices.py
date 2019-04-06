import re
import datetime
import os
from subprocess import Popen, PIPE
import fileHandler
from threads import *
import time




class LnxServices:
    
    def listServices(self,file,action):
        cmd1 = Popen(["service","--status-all"],stdout=PIPE,stderr=PIPE)
        stdout = cmd1.communicate()[0]
        cmd1.stdout.close()
        now = datetime.datetime.now()

        services = stdout.split('\n')
        
        with open(file, action) as f:
            f.write("________________________________________________________________________________________________________\n")
            f.write("Check time: "+ str(now)[2:19]+"\n")
            f.write("________________________________________________________________________________________________________\n")
            for item in services[:-1]:
                if item[3]=="+":
                    print >> f, (item+"\n")
    
   
        

class lnxMonitor:
    def lnxMonitorState(self,x):
        myThread=inputThread()
        myThread.start()
        l=LnxServices()
        a=fileHandler.actions()
        temp=x
        while myThread.is_alive:
                    x=temp
                    l.listServices("new.txt","w")
                    a.detectChanges("new.txt","old.txt",True)
                    while x>0:
                            if myThread.is_alive==False:
                                    return
                            time.sleep(1)
                            x-=1
                    l.listServices("old.txt","w")
                    a.detectChanges("old.txt","new.txt",True)












