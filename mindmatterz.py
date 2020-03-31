#!/usr/bin/python

import cgi

print 'Content-Type: text/html\r\n'   # content header
print '\r\n'   # finish headers with blank line

form = cgi.FieldStorage()   # FieldStorage object to
                            # hold the form data
contents = ['From: Web-Enquiry.com',
            'To:noel@mindmatterz.in',
            'Subject: Web Enquiry\n\n'
           ]
# check whether a field called "username" was used...
# it might be used multiple times (so sep w/ commas)
if form.has_key('name'):
  contents.append('Full Name: ' +  form["name"].value)
if form.has_key('email'):
  contents.append('Email Address: ' + form["email"].value)
if form.has_key('tel'):
  contents.append('Telephone: ' + form["tel"].value)
if form.has_key('message'):
  contents.append('Comments & Enquiries: ' + form["message"].value)
contents = '\n'.join(contents)

import smtplib
import urllib2
smtpserver = '162.243.128.118'
SENDER = 'web@enmail.com'
RECIPIENTS = ['noel@mindmatterz.in']
session = smtplib.SMTP(smtpserver)
session.sendmail(SENDER, RECIPIENTS, contents)

print '''
<html>
<head>
<meta http-equiv="refresh" content="2;url=http://www.mindmatterz.in/index.html" />
<title>www.mindmatterz.in</title>
</head>
<body>
<br>
<font color="grey" face="verdana" size="4"><b>Your Message has been sent. Thank you...</b></font>
</body>
</html>'''
