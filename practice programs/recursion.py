'''def display(s,ind):
    if ind==len(s):
        return           
    print(s[ind],ind)
    display(s,ind+1)

s='Python Programming'
display(s,0)'''



'''def display(s,ind):
    if ind<0:
        return
    print(s[ind],ind)
    display(s,ind-1)

s='Python Programming'
display(s,17)'''



'''s='abcdefgh'
c=1
rep=len(s)
while c<rep:
    rep-=1
    for i in range(0,c):
        print(s,c)
        c+=1'''

'''def display(s,c):
    if c==len(s)+1:
        return
    print(s[:c])
    display(s,c+1)

    s='abcdefgh'
    display(s,1)'''


'''def display(s,ind):
    if ind==len(s)-sub+1:
        return
    print(s[ind:ind+sub],ind)
    display(s,ind+1)                   abc 0
                                       bcd 1
s='abcdefgh'                           cde 2
sub=3
display(s,0)'''



'''def display(l,ind):
    if ind==len(l):
        return
    print(l[ind])
    display(l,ind+1)

l=[1,2,3,4,5,6,7,8,9,10]
display(1,9)'''





'''def display(l,ind):
    if ind<0:
        return
    print(l[ind])
    display(l,ind-1)

l=[1,2,3,4,5,6,7,8,9,10,45,23,45,65,85,75,89]
display(l,len(l)-1)'''


'''def robo():
    print("Hi")
    robo()

     print("Hello")
 robo()'''


'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


fact(7) '''

#pip install pyttsx3 SpeechRecognition pyaudio
import speech_recognition as sr #used as voice to text
import pyttsx3 #text to voice
import datetime
import webbrowser
#Initialize the text-to-speech engine    
engine=pyttsx3.init()
# Function to make the assistance speak  
def speak(text): #text to voice
       voices=engine.getProperty('voices')
       engine.setProperty('voice',voices[1].id)
       engine.say(text)
       engine.runAndWait()
# Function to listen to user's voice   
def listen():
       recognizer=sr.Recognizer()
       with sr.Microphone() as source:
              print(" Listening.....")
              recognizer.pause_threshold=1


              audio = recognizer.listen(source)
              try:
                     command = recognizer.recognize_google(audio,language='en-in')
                     print("You said:",command)
                     return command.lower
             