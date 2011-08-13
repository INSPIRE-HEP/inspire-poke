#!/usr/bin/python

import cgi
from email.MIMEText import MIMEText
import simplejson as json
import smtplib

FEEDBACK = 'feedback@inspirebeta.net'
CRAZYSPIRESMACHINE = 'spires-autofeedback@slac.stanford.edu'

def mail_feedback(search, yes_no, message):
    """ take the info, send it to INSPIRE feedback """
    if yes_no == 'true':
        yes_no = 'yes'
    elif yes_no == 'false':
        yes_no = 'no'
    message = """
    Dear INSPIRE feedback folks,
        A SPIRES user interacted with your box in SPIRES!

        They were trying the search
            %(search)s

        What they said was
            Did INSPIRE give results you expected? %(yes_no)s
            Comments: %(message)s

    """ % { 'search' : search,
            'message' : message,
            'yes_no' : yes_no }

    msg = MIMEText(message)
    msg['Subject'] = 'INSPIRE feedback originating from SPIRES:' + yes_no
    msg['To'] = FEEDBACK
    msg['From'] = CRAZYSPIRESMACHINE

    s = smtplib.SMTP('cernmx.cern.ch')
    s.sendmail(CRAZYSPIRESMACHINE, [FEEDBACK], msg.as_string())
    s.quit()

    return True

if __name__ == '__main__':
    print "Content-type: application/json"
    print

    fs = cgi.FieldStorage()
    message = ''
    yes_no = False
    search = ''
    if fs.has_key('search'):
        search = fs.getvalue('search')
    if fs.has_key('message'):
        message = fs.getvalue('message')
    if fs.has_key('yesNo'):
        yes_no = fs.getvalue('yesNo')
    print json.dumps(mail_feedback(search, yes_no, message))
