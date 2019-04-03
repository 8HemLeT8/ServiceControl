import difflib
import time
import datetime
        
class fileHandler:
        def detectChanges(file1,file2,tosave):
                now = datetime.datetime.now()
                with open(file1) as a, open(file2) as b:
                        
                        alines = a.readlines()
                        blines = b.readlines()
                        d = difflib.Differ()

                        if tosave:
                                sl=open("Status_Log.txt","a")        
                                sl.write("________________________________________________________________________________________________________\n")
                                sl.write("Check time: "+ str(now)[:19]+"\n")
                                sl.write("________________________________________________________________________________________________________\n")
                                
                                diff = d.compare(blines, alines)
                                print("Changes Occured:")
                                print(''.join(x for x in diff if (x[0] is not ' ' and x[0] is not '?')), file=sl) 
                                diff = d.compare(blines, alines)
                                print (''.join(x for x in diff if (x[0] is not ' ' and x[0] is not '?')))
                                sl.close()

                        else:
                                diff = d.compare(blines, alines)
                                print ('Changes Occured:')
                                print(''.join(x for x in diff if (x[0] is not ' ' and x[0] is not '?'))) 
                        
                
        def clear(file):
                f=open(file,"w")
                f.write("")
                print("The file: "+f.name+" cleared.")
