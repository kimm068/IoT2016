import smtplib
import sys
# Import this 'sys'

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 

name = "Miyeon"
print name

# argument list
print 'Argument List:', str(sys.argv)


# classes = [iot,js,unity]
# print classes[1]

# if classes[i]=='unity':
# 	print "Robert Yang" 
 
 
fromaddr = "kimm068@newschool.edu"
toaddr = "miyeon2003@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hola"
 
body = sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]
msg.attach(MIMEText(body, 'plain')) 
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "****")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


