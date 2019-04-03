import os
import psutil

class lnxServices:
    """
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
    """            
print os.system("ps -u 0")

print(psutil.pids())