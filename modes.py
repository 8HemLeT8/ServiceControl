from getServices import *
import time
from fileHandler import *
import os

class monitor:
    def monitorState(x):
        if(os.name=='nt'):
                while 1:
                        WinServices.ListServices("new.txt","w")
                        fileHandler.detectChanges("new.txt","old.txt",True)
                        time.sleep(x)
                        WinServices.ListServices("old.txt","w")
                        fileHandler.detectChanges("old.txt","new.txt",True)
        if(os.name=='posix'):
            print("Linuxxx")
                

class manual:
    def manualState(datetime1,datetime2):
        try:
                datetime.datetime.strptime(datetime1,'%m-%d-%y %H:%M:%S')
                datetime.datetime.strptime(datetime2,'%m-%d-%y %H:%M:%S')
        except:
                print("Make sure the DateTime is of the format: MM-DD-YY HH:MM:SS")
                exit()
        
        sl=open("serviceList.txt","r")
        data=sl.read()
        arr=data.split("Check time:")
        flag1=False
        flag2=False
        for i in range(len(arr)):
                if arr[i].__contains__(datetime1):
                        print(arr[i],file=open("file1.txt","w"))
                        flag1=True
                if arr[i].__contains__(datetime2):
                        print(arr[i],file=open("file2.txt","w"))
                        flag2=True
        if flag1==False:
                print("No data for the first DateTime!")
                exit()
        
        if flag2==False:
                print("No data for the second DateTime!")
                exit() 
        fileDiff.detectChanges("file1.txt","file2.txt",False)
        sl.close()
        file.close()