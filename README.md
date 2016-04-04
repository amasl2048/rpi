#Message Waiting Indicator program for Raspberry Pi 2

Check for new e-mail on IMAP servers and notify by LED blinking

We have 3 states:
1. New email (LED blinking)
2. No news (LED down)
3. Out of service (LED up)

Script is loading config yaml file (mwi.yml):
'''
    name:
      server: mail.com
      login: user
      pass: password
'''

and writing a log to file (mwi.log).