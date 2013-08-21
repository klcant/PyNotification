#!/usr/bin/python

#Sending an email through gmail using python
import smtplib
fromaddr = 'address@gmail.com'
toaddrs = 'address@gmail.com'
msg = 'Email message from python'

#provide gmail user name and password
username = 'youraccount@gmail.com'
password = 'app password'

# functions to send an email
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()


