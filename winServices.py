import win32con
import win32service 
import os,stat
import fileHandler
import time
import datetime
from threads import *


class WinServices:    
        def ListServices(finto,action):

                actionOnFile = action
                accessSCM = win32con.GENERIC_READ
    
                #Open Service Control Manager
                hscm = win32service.OpenSCManager(None, None, accessSCM)

                #Enumerate Service Control Manager DB
                typeFilter = win32service.SERVICE_WIN32
                stateFilter = win32service.SERVICE_STATE_ALL

                statuses = win32service.EnumServicesStatus(hscm, typeFilter, stateFilter)
                now = datetime.datetime.now()
                f=open(finto,actionOnFile)
                sl=open("serviceList.txt","a")

                f.write("________________________________________________________________________________________________________\n")
                f.write("Check time: "+ str(now)[2:19]+"\n")
                f.write("________________________________________________________________________________________________________\n")
                
                sl.write("________________________________________________________________________________________________________\n")
                sl.write("Check time: "+ str(now)[2:19]+"\n")
                sl.write("________________________________________________________________________________________________________\n")

                for (status) in statuses:
                        if status[2][1]==1:
                                continue
                               #    print("Service:",status[1],"| Status: Paused")
                              #  f.write("Service: "+status[1]+"| Status: Paused\n")
                              #  sl.write("Service: "+status[1]+"| Status: Paused\n")
        
                        elif status[2][1]==4:
                               # print("Service:",status[1],"| Status: Running")
                                f.write("Service: "+status[1]+"| Status: Running\n") 
                                sl.write("Service: "+status[1]+"| Status: Running\n") 

                        else:
                                print ("Service: "+status[1]+"| Status: "+str(status[2][1])+"\n")        
                
                os.chmod(sl.name,stat.S_IREAD)
                os.chmod(sl.name,stat.S_IREAD)

                f.close()
                sl.close()

class winMonitor:
    def winMonitorState(x):
        myThread=inputThread()
        myThread.start()
        a=fileHandler.actions()
        temp=x
        while myThread.is_alive:
                x=temp
                WinServices.ListServices("file2.txt","w")
                a.detectChanges("file2.txt","file1.txt",True)
                while x>0:
                        if myThread.is_alive==False:
                                return
                        time.sleep(1)
                        x-=1
                WinServices.ListServices("file1.txt","w")
                a.detectChanges("file1.txt","file2.txt",True)