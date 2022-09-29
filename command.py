#improting  required lib

import speech_recognition as sr
import pyttsx3
import datetime
import time
import webbrowser
import wikipedia
import os
import subprocess
import smtplib, ssl
import getpass
import sql


#initialization of sapi
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def Speak(text):
	engine.say(text)
	engine.runAndWait()


#command class for utlization of tasks
class commands:
    xyz=""
    chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    

    #constructor 
    def __init__(self,xyz):
       self.xyz=xyz.lower()

    #for wikipedia search like what is food etc questions
    def wiki(self,xyz):

        try:
            terms=""
            terms=terms.join(xyz[2:])
            Speak("wait")
            request=terms
            output=wikipedia.summary(request,sentences=3)
            Speak(output)
        except:
            print("Cant find the approprate information. Try Again ")

    #for opneing website by saying open website_name or open webiste_name.com            
    def open_website(self,request):
        if 'open' in request:
            Speak("wait")
            
            request=request.replace("open","")
            
            if ".com"   in request:
                webbrowser.get(commands.chrome).open(request)
            else:
                a=""
                a=a.join(request+".com")
                webbrowser.get(commands.chrome).open(a)

    #for searching some ting on google by saying search something 
    def google_search(self,xyz):
        ss=""
        if "search" in xyz:
            Speak("wait")
            xyz=xyz.replace("search","?")
            webbrowser.get(commands.chrome).open(xyz)

    #for open an app or a application on the pc 
    def open_app(self,request):
        request=request.replace("open","")
        try:
        #download folder
            if "download"  in request or "downloads" in request:
                Speak("wait")

                path=os.path.join('C:\\','Users',os.getlogin(),"downloads")
                path = os.path.realpath(path)
                subprocess.run(['explorer', os.path.realpath(path)])
        #music           
            elif "music" in request or "songs" in request:
                Speak("wait")
                path=os.path.join("C:\Program Files\Windows Media Player\wmplayer.exe")
                path = os.path.realpath(path)
                os.startfile(path)
        #cmd            
            elif "cmd" in request or "powershell" in request:
                Speak("wait")
                os.system("start cmd /k ")
        #libraries
            elif "libaries" in request or "coumputer" in request:
                Speak("wait")
                os.system("start explorer ")
        #microsoft apps,store
            elif "microsoft" in request:
                if "store" in request:
                    Speak("wait")
                    os.system("start ms-windows-store:")
        #documnets
            elif"documents"in request:
                Speak("wait")
                path=os.path.join('C:\\','Users',os.getlogin())
                path = os.path.realpath(path)
                subprocess.run(['explorer', os.path.realpath(path)])
        #photos
            elif "photos" in request or "Pictures" in request:
                Speak("wait")
                path=os.path.join('C:\\','Users',os.getlogin(),"OneDrive\Pictures")
                path = os.path.realpath(path)
                subprocess.run(['explorer', os.path.realpath(path)])
        #calculator            
            elif "calculator" in request:
                Speak("wait")
                os.system("start calculator:")
            
            
        #will search on web
            else:
            
                return "web"

        except :
                return "web"

    #function for email
    def send_email(self):
        Speak("please be sure your sending accounts is alowing less secure app ")
        port = 465  
        smtp_server = "smtp.gmail.com"
        Speak("PLease type your E-Mail ID : ")
        sender_email = input("E-mail : ")

        Speak("To Whom do you wanna Send?")
        Speak("Enter Recipient E-mail : ")
        receiver_email = input("To :: ")
        Speak("Please type your Password : ")
        

        password = getpass.getpass("enter your password and press enter")
        
        Speak("What is the Message? please speak \n > ")

        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Message is : ")
            audio=r.listen(source)
            try:
                message=r.recognize_google(audio)
            except :
                print("system error")
                
        try :
            print("You said\t  "+message)
        except sr.UnknownValueError:
            print("can u please repeat")
            message=None
        except sr.RequestError:
            print("System error")

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        except:
            
            Speak("Cant send email as error occured")
            print("Cant send email as error occured")

    #remembering some thing like name // store in database
    def remember(self):
        self.xyz=self.xyz.replace("remember ","")
        sql.store(self.xyz)
        
    #to get information from data base
    def get_info(self):
        
        ans=sql.get_info(self.xyz)

        if ans=="false":

            return "false"
        else:
            print(ans)
            Speak(ans)
            
            return "true"

    #the main command which calssify about to open website search or wiki or send mail or open any appliction
    #or to quit the application
    def command(self):
        

        if "remember " in self.xyz:
            commands.remember(self)

        elif "open "in self.xyz:
            
            web=commands.open_app(self,self.xyz)    #open application if specified
            if web=="web":
               commands.open_website(self.xyz,self.xyz) #open web site

        elif "how are you" in self.xyz:
             Speak("Good how can i help you!!")

        elif "help" in self.xyz or "help me" in self.xyz:
            print("Commands must be like")
            print("Open youtube ")
            print("Search food ")
            print("what is food? ")
            print("Who is Sachin tendulkar?")
            print("Open downloads")
            print("open music")
            print("send Email")
            print("remenber my name is ....")
            print("what is my name?")
            print("what is my phone number?")
            print("what text - for asking what you said to remeber about text")
            print("which user")
            print("get user")

            print("quit or exit for exit")

        elif"send mail" in self.xyz or "send email" in self.xyz:    #send mail
            commands.send_email(self)


        elif "what" in self.xyz or "who" in self.xyz:   #information
                ans=commands.get_info(self)
                if ans=="false":
                    if "time" in self.xyz:
                        Speak(datetime.datetime.now())
                    else:
                        commands.wiki(self.xyz,self.xyz) 
                        
        elif "search" in self.xyz:  #search google
            commands.google_search(self.xyz,self.xyz)
        elif "which" in self.xyz or "get" in self.xyz:
        	if "user" in self.xyz :
        		print(os.login());Speak(os.login())
	    elif "quit"  in self.xyz or "exit" in self.xyz : #quit
            Speak("quiting the application ")
            return "quit"

        else :
            Speak(" Could not found the command !!")





        


    
