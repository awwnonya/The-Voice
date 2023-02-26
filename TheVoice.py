'''The Voice by Ananya Pal'''

import wikipedia
import pyttsx3
engine = pyttsx3.init()

""" RATE"""
r= int(input("\nEnter Rate: "))
rate = engine.getProperty('rate')   # getting details of current speaking rate
print ('Current Rate of speaking: ', rate)                        #printing current voice rate
engine.setProperty('rate', r)     # setting up new voice rate
print ('New Rate of speaking: ', r)                        #printing new voice rate


"""VOLUME"""
v= float(input("\nEnter Volume: "))
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print ('Current Volume of speaking: ',volume)                          #printing current volume level
engine.setProperty('volume',v)    # setting up volume level  between 0 and 1
print ('New Volume of speaking: ', v)                        #printing current volume rate


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
c=int(input("\nEnter 0 for Male Voice and 1 for Female Voice: "))
if c==0:
    engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
elif c==1:
    engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female
else:
    print("Sorry! No appropriate value entered.")
    

cmd= input('Enter your Query: ',)

s= int(input("\nEnter number of sentences: "))

result= wikipedia.summary(cmd, s)
print(result)

engine.say(result)
engine.runAndWait()