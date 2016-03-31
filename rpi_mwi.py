import RPi.GPIO as GPIO
import imaplib
import sys
import yaml
import time

'''
Message Waiting Indicator program for Raspberry Pi 2
Check for new e-mail on IMAP servers and notify by LED blinking

We have 3 states:
1) New email (LED blinking)
2) No news (LED down)
3) Out of service (LED up)

'''

try:
    cred = yaml.load(open('mwi.yml')) # load config file
except:
    print sys.exc_info()[1]
    sys.exit(1)
    
timeout = 900 # time between email check

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# LED connected between GPIO and Ground over 470 Ohm
chan = 3 # using GPIO3
GPIO.setup(chan, GPIO.OUT)

def check_mail(): #TODO: check several servers
    mails = False # do we have new emails?
    service = True # does email server available?
    for serv in cred.keys():
        
        M = imaplib.IMAP4_SSL(cred[serv]["server"])

        try:
            M.login(cred[serv]["login"], cred[serv]["pass"])
        except:
            print "No connection"
            service = False
            return service, mails

        M.select(readonly=1)
        ret, data = M.search(None, '(UNSEEN)')
        if ret == 'OK':
            #print data
            if data[0] != '':
                print 'You have %s new e-mails!' % (len(data[0].split(' ')))
                mails = True
            else:
                print 'No news'
                mails = False
        else:
            print "No service"
            service = False
            return service, mails

        M.close()
        M.logout()
    return service, mails

def led_blink():
    for t in range(int(timeout/2)):
        # LED up for 0.5s
        GPIO.output(chan, 1)
        time.sleep(0.5)
        # LED down for 1.5s
        GPIO.output(chan, 0)
        time.sleep(1.5)

def led_down():
    GPIO.output(chan, 0)
    time.sleep(timeout)
    
def led_up():
    GPIO.output(chan, 1)
    time.sleep(timeout)

while True:
    service, mails = check_mail() 
    if mails: # We have new email
        print "LED blink!"
        led_blink()
    elif service: # Server available, but no e-mails
        print "LED down"
        led_down()
    else:
        print "LED up" # Out of service
        led_up()

#GPIO.cleanup()