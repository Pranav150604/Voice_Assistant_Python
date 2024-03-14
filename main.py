

#                             >>   VOICE ASSISTANT    <<
#                                >>    Nⱥno多oτ    <<



'''Dear Sir, Google Colab does not run the below code, due to Driver Issues, It throws a 
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.9/dist-packages/pyttsx3/__init__.py in init(driverName, debug)
     19     try:
---> 20         eng = _activeEngines[driverName]
     21     except KeyError:

Looks Like It has something to do with the Loaded Drivers on Google's Colab Server, Hence the error Thrown
I'd Recommend executing the code Locally onto your own bare metal.
'''
# this is a voice assistant program which can wish you according to the time
#this can open youtube ,google,stackoverflow, spotify ,whatsapp,visual code
#it can tell you the present time and can send mail


import pyttsx3
'''
to install this library :pip install pyttsx3
this is a text to speech conversion library in python
it basically has two voices :1)DAVID(male).......2)ZIRA(female)
you can change speed rate here.200 is the default speed rate 

'''



import datetime
#this is a built-in datetime library and is used to manipulate date and time
#here it is used to tell the current time


import speech_recognition as sr
#this library has a ability to listen to spoken words and identify them


import wikipedia
#it is a python library that has access to wikipedia and collects information,data,links,images etc


import webbrowser
#it is a built-in library and can browse the input


import os
#it provides the facility to establish the interaction between the user and the operating system


import smtplib
#it is a client session object that is used to send mail to any internet machine

engine=pyttsx3.init('sapi5')
'''
sapi5 VOID modular system . Sapi ie speech API is a technology for voice reognition 
and synthetis provided by microsoft
the above line means that engine gets a reference to engine instance that uses the given driver

'''
voices=engine.getProperty('voices')
#gets the voices from engine
#print(voices[1].id){this line is optional}
engine.setProperty('voice',voices[1].id)
#voices[1] is for female and voices[0] is for male

def speak(audio):
# in this function,  audio string is spoken by engine
    engine.say(audio)
    engine.runAndWait()

def wishMe():
# for the function to work,we import "datetime" library
#according to the time ,the bot wishes the user


    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<16:
        speak("good afternoon")
    elif hour>=16 and hour<20:
        speak("good evening")
    else:
        speak("good night")
    speak("i am your nanobot please tell me how can i help you")
    #speak("nanobot at your service, how may I help you?")
def takeCommand():
#it takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        #the above line is the min time that it waits before it gives the output
        #if no input is heard by it more than 1 sec it gives the output
        audio=r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')#en-in is a language code that compiler understands
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e) {optional}
        print("say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your_password')
    server.sendmail('youremailgmail.com',to,content)
    server.close
'''
the above function is for sending email
when the server listens for the TCP connections from a client ,it initiates a connection on port 587
here your email_id and password need to be given



for sending email , there are some changes needed to be done in settings.
In google,browse "less secured apps in gmail"
then go the first website available,
then scroll down,u will find a option called "console",
click there then go to "security" then "basic settings"
then under "less secure apps" select "go to settings for less secure apps"
in the subwindow , select the enforce access to less secure apps for all radio button


'''


if __name__=="__main__":
    wishMe()
    while True:#this is a infinite loop
    #if 1:#this can be used if finite loop needed
        query=takeCommand().lower()
        if 'wikipedia' in query:
        #when you give input , if it contains the word "wikipedia" then this runs
        # to search anything you need to speak wikipedia with the content which you wanted to search
            query=query.replace('wikipedia',"")
            result =wikipedia.summary(query,sentences=2)#you can change the number of lines to be printed
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        #this opens youtube if your input contains the words"open youtube"
        

        elif 'open google' in query:
            webbrowser.open("google.com")
        #this opens google if your input contains the words"open google"
        

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        

        elif 'play songs'in query:
            #codePath = ""
            os.startfile("spotify")  
            #webbrowser.open("spotify.com")
        #opens spotify(song)


        elif 'whatsapp' in query:
           #codePath = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2301.4.0_x64__cv1g1gvanyjgm"
            os.startfile("C:\\Users\\windows10\\Desktop\\startWA.bat") 
            #webbrowser.open("whatsapp.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strTime}")
        # speaks out the current time with seconds


        elif 'open code' in query:
            codePath="C:\\Users\\windows10\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        #opens visual code


        elif 'send email' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to='receiver_email@gamil.com'
                sendEmail(to,content)
                speak('email has been sent!')
        #send a email when receiver email is given
            
            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to send this email")

        elif 'quit' in query:
            exit()
        #if "quit" is given as input ,it ends the execution



          
 
