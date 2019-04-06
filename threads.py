import threading

class inputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            userInput=raw_input("To stop type STOP && To exit type EXIT\n")
            if (userInput=="STOP"):
                self.is_alive=False
                return
            if userInput=="EXIT":
                exit()



#def fileStatus():