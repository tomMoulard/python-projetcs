#made by tomMoulard 27/08/16

import random

def setres(n):
	if n <= 0:
		return ""
	else:
		return(chr(random.randint(33, 126))+setres(n - 1))

def sendemail(cnt):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	msg = MIMEMultipart()
	msg['From'] = "gipsyzilla@gmail.com"
	msg['To'] = "tomtomone247@gmail.com"
	msg['Subject'] = "Password"
	msg.attach(MIMEText(cnt))
	p_w_d = "azAZ&&11"
	server = smtplib.SMTP('smtp.gmail.com', 587)
	print ("[+] Connecting To Mail Server.")
	server.ehlo()
	server.starttls()
	server.ehlo()
	print ("[+] Logging Into Mail Server.")
	server.login('gipsyzilla', p_w_d)
	print ("[+] Sending Mail")
	server.sendmail(fromaddr, toaddr, msg.as_string())
	print ("[+] Mail Sent Successfully.")
	server.quit()

def main():
	res = "coucou"
	#get nb longueur
	n = int(input("quelle longueur ?\n"))
	#process
	res = setres(n)
	#print res
	print(res)
	#send email pour ne pas prendre le mdp
	#sendemail(res)
	print("email sent :)")

if __name__ == '__main__':
	main()