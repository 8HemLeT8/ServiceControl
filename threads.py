import threading

class inputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            userInput=str(input("to stop type STOP\n"))
            if (userInput=="STOP"):
                self.is_alive=False
                return



#def fileStatus():