import manualMode,fileHandler,os

class main:
    a=fileHandler.actions()
    mm=manualMode.manual()
    if os.name=='nt':
        import winServices
        
        winServices.winMonitor.winMonitorState(600)
        #a.clear("serviceList.txt")
        #mm.manualState("19-04-05 17:01:23","19-04-03 18:16:31")


    elif os.name=='posix':
        import lnxServices
        m=lnxServices.lnxMonitor()
        #m.lnxMonitorState(600)
        #a.clear("serviceList.txt")
        mm.manualState("19-04-05 17:01:23","19-04-03 18:16:31")






