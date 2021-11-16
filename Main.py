from time import sleep
import serial
import pyttsx3
import smtplib
from email.message import EmailMessage

ser=serial.Serial("/dev/ttyACM0",9600)

def SpeakAudio(Text):
    engine=pyttsx3.init()
    engine.setProperty("rate",130)
    engine.say(Text)
    engine.runAndWait()

def SendEmail():
    Sender_Email = "radfs@gmail.com"
    Reciever_Email = "Rec4@gmail.com"
    Password = "deePasswrd"

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Emergency Message From Mukesh" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Please help me, I Am in emergency.')
                           
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
        

# main Code Initiated

ser.flush()
while True:
    Out=''
    text=''
    if ser.in_waiting>0:
        Out=(ser.readline().decode("ascii").rstrip())
        ser.flush()
    if Out=="A":
        text="Hello, How Are You"
    elif Out=="B":
        text=("What is Your Name")
    elif Out=="C":
        text=("Where is the washroom")
    elif Out=="D":
        text=("Give me some water")
    elif Out=="E":
        text=("I am hungry give me some food")
    elif Out=="F":
        text=("i am sorry")
    elif Out=="Z":
        #SendEmail()
        text=("Email Sent For help")               
                       
    print(text)    
    if len(text)>1:
        SpeakAudio(text)
    


    
    

