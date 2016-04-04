Message Waiting Indicator program for Raspberry Pi 2
Check for new e-mail on IMAP servers and notify by LED blinking

We have 3 states:
1) New email (LED blinking)
2) No news (LED down)
3) Out of service (LED up)

loading config yaml file:
    name:
      server: mail.com
      login: user
      pass: password
      
writing log to mwi.log file