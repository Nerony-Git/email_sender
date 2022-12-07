import smtplib

#Get the recipient's email account 
receiver = input("Enter the recipient's email: \n")

#Get the message to be sent
msg = input("Type your message: \n")


def sendEmail(receiver, msg):
    #Using gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","password_of_email")
    server.sendmail("youremail@gmail.com",receiver,msg,)
    server.close()

sendEmail(receiver, msg)