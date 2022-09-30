import speech_recognition as sr
import pyttsx3
import datetime
import time
import webbrowser
import wikipedia
import os

import command as oo



#initialization of sapi
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


print("Running.....")
#output voice 
def Speak(text):
    
	engine.say(text)
	
	engine.runAndWait()

#wishing
def Greet():
    
	a=int(datetime.datetime.now().hour)
	
	if a>=0 and a<12:
		Speak("good morning.!!!!")
	elif a>=12 and a<18:
		Speak("good after noon!!!!! ")
	else:
		Speak("good evening")

Speak("Engine Starting")
time.sleep(0.3)
Greet()

Speak("I'm your Personal Assistant")
Speak("You can give me commands like")
Speak("Open Youtube, Open Facebook or Open Download etc")
Speak("I can send an email, I can search on web.")
Speak("If you want to know more you can always use command 'help'")
Speak("quit or exit for exit")
print("Commands must be like")
print("Open youtube ")
print("Search food ")
print("what is food? ")
print("Who is Sachin tenduulkar?")
print("Open downloads")
print("open music")
print("send Email")
print("remenber my name is ....")
print("what is my name?")
print("what is my phone number?")
print("what text - for asking what you said to remeber about text")

print("quit or exit for exit")

#input the audio and recoginize text and return to function
def input():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Say Something...")
		
		try:
			audio=r.listen(source)
			request=r.recognize_google(audio)
		except :
			print("system error")
			return "error" 
			
	try :
		print("You said\t  "+request)
	except sr.UnknownValueError:
		print("can u please repeat")
		request=None
	except sr.RequestError:
		print("Check Internet Connectivity, and Try Again...")
	
	return request.lower()
request=input()

#creating object of oopscommands class  and initalizing the command string to
#class commands
c=oo.commands(request)
response=c.command() #running the command for the void command by object calling to function



#for continous working of voice take input and working on commands untill user says quit
while response != "quit" :
        request=input()
        c=oo.commands(request)
        response=c.command()
        time.sleep(0.8)

print("exit")

if 1==1:
	print(2)
else:
	print(2)







































































































