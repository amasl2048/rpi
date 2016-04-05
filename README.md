##Message Waiting Indicator (MWI) program for Raspberry Pi 2

Check for new e-mail on IMAP servers and notify by LED blinking

We have 3 states:
1. New email (LED blinking);
2. No news (LED down) - or short blink in order to show activity;
3. Out of service (LED up).

Script loads config yaml file (mwi.yml):
'''
    name:
      server: mail.com
      login: user
      pass: password
'''

and writes a log to file (mwi.log).