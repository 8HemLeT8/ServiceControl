from __future__ import print_function
import datetime
import time
import fileHandler
import os
from threads import *

#PROBLEM IS LINUX CANT WORK WITH IMPORT WIN32 FIX IT!!!
         

class manual:
    def manualState(self,datetime1,datetime2):
        a=fileHandler.actions()    
        try:
                datetime.datetime.strptime(datetime1,'%y-%m-%d %H:%M:%S')
                datetime.datetime.strptime(datetime2,'%y-%m-%d %H:%M:%S')
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
                        print(arr[i], file=open("file1.txt","w"))
                        flag1=True
                if arr[i].__contains__(datetime2):
                        print(arr[i], file=open("file2.txt","w"))
                        flag2=True
        if flag1==False:
                print("No data for the first DateTime!")
                exit()
        
        if flag2==False:
                print("No data for the second DateTime!")
                exit() 
        a.detectChanges("file1.txt","file2.txt",False)
        sl.close()
