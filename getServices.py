import win32con
import win32service
import datetime
import os

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
                f.write("Check time: "+ str(now)[:19]+"\n")
                f.write("________________________________________________________________________________________________________\n")
                
                sl.write("________________________________________________________________________________________________________\n")
                sl.write("Check time: "+ str(now)[:19]+"\n")
                sl.write("________________________________________________________________________________________________________\n")

                for (status) in statuses:
                        if status[2][1]==1:
                               #    print("Service:",status[1],"| Status: Paused")
                                f.write("Service:"+status[1]+"| Status: Paused\n")
                                sl.write("Service:"+status[1]+"| Status: Paused\n")
        
                        elif status[2][1]==4:
                               # print("Service:",status[1],"| Status: Running")
                                f.write("Service:"+status[1]+"| Status: Running\n") 
                                sl.write("Service:"+status[1]+"| Status: Running\n") 

                        else:
                                print ("Service:"+status[1]+"| Status: "+str(status[2][1])+"\n")        
                f.close()
                sl.close()



class lnxServices:
    
    def listServices():
        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

        for pid in pids:
            try:
                cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                if cmd.find('smtpd') != -1:
                    print "PID: %s; Command: %s" % (pid, cmd)
            # process has already terminated
            except IOError:
                continue
    

