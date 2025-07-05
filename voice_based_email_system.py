import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unm="give your email id here"
pwd="give your password here"

r=sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str="speak now:"
        speak(str)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            # print("you said:{}".format(text))
            return text
        except:
            str="sorry could not recognize what you said"
            speak(str)

def sendmail():
    rec="give the receiver's email id here"
    str='please speak the body of your email'
    speak(str)
    msg=listen()
    str ="you have spoken the message"
    speak(str)
    speak(msg)
    
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(unm,pwd)
    server.sendmail(unm,rec,msg)
    server.quit()
    
    str='email has been sent'
    speak(str)
    
def readmail():
    server=e.connect("imap.gmail.com",unm,pwd)
    server.listids()
    
    # str="please say serial number of the email you wanna read"
    # speak(str)
    
    # a=listen()
    # if(a== "three"):
    #     a="3"
        
    for b in range(0,3):
        email = server.mail(server.listids()[b])
        str="the mail is from"
        speak(str)
        speak(email.from_addr)
        str="the subject of mail is"
        speak(str)
        speak(email.title)
        str="the body of mail is "
        # speak(str)
        # speak(email.body)
    
    

str="welcome"
speak(str)
while(1):
    str="what do you want to do"
    speak(str)
    str = "speak send to send mail      speak read to read inbox        speak exit to exit"
    speak(str)
    ch=listen()
    
    if (ch=='send'):
        sendmail()
    elif (ch=='read'):
        readmail()
    elif (ch=='exit'):
        str="you chosen to exit"
        speak(str)
        exit(1)
    else:
        str="sorry could not recognize what you said"
        speak(str)
        speak(ch)