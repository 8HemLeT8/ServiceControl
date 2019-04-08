import datetime
import os,stat
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
        sl=open("serviceList.txt","a")

        services = stdout.split('\n')
        
        
        with open(file, action) as f:

            f.write("________________________________________________________________________________________________________\n")
            f.write("Check time: "+ str(now)[2:19]+"\n")
            f.write("________________________________________________________________________________________________________\n")
            
            sl.write("________________________________________________________________________________________________________\n")
            sl.write("Check time: "+ str(now)[2:19]+"\n")
            sl.write("________________________________________________________________________________________________________\n")

            for item in services[:-1]:
                if item[3]=="+":
                    print >> f,  ("Service:"+item[7:]+" | Status: Running"+"\n")
                    print >> sl, ("Service:"+item[7:]+" | Status: Running"+"\n")
            
            os.chmod(f.name,stat.S_IREAD)
            print(sl.name)
            os.chmod(sl.name,stat.S_IREAD)
            f.close()
            sl.close()
    
   
        

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
        












