'''The Voice by Ananya Pal'''

import os
import wikipedia
import pyttsx3
engine = pyttsx3.init()


""" RATE"""
r= int(input("\nEnter Rate: "))
rate = engine.getProperty('rate')   # getting details of current speaking rate
print ('Current Rate of speaking: ', rate)   #printing current voice rate
engine.setProperty('rate', r)     # setting up new voice rate
print ('New Rate of speaking: ', r)  #printing new voice rate


"""VOLUME"""
v= float(input("\nEnter Volume: "))
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print ('Current Volume of speaking: ',volume)   #printing current volume level
engine.setProperty('volume',v)    # setting up volume level  between 0 and 1
print ('New Volume of speaking: ', v)  #printing current volume rate


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
c=int(input("\nEnter 0 for Male Voice and 1 for Female Voice: "))
if c==0:
    engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
elif c==1:
    engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female
else:
    print("Sorry! No appropriate value entered.")
    

cmd= input('\nEnter your Query: ')

s= int(input("\nEnter number of sentences: "))

result= wikipedia.summary(cmd, s)
print(result)

engine.say(result)

c=input("\nDo you want to save the results (Y/N)? ")

if(c=='Y' or c=='y'):

    type=input("Enter 'A/a' for Audio, 'T/t' for Text file and 'B/b' for Both: ")
    if((type=='A' or type=='a')):
        print("Okay! Audio saved.\n")
        #a='E:/'+cmd+'.mp3'
        a='E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/COMPLETES/'+cmd+'.mp3'
        engine.save_to_file(result, a)

    elif ((type=='T' or type=='t')):
        print("Okay! Text File saved.\n")
        a='E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/COMPLETES/'+cmd+'.txt'
        myfile=open(a, 'w')
        myfile.write(result)
        myfile.close()
        #engine.save_to_file(result, a)

    elif ((type=='B' or type=='b')):
        print("Okay! Both Audio and Text Files saved.\n")
        a1='E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/COMPLETES/'+cmd+'.txt'
        a2='E:/0.0. Visual Studio Code/AnanyaPal_Python/PROJECTS/COMPLETES/'+cmd+'.mp3'

        #engine.save_to_file(result, a1)
        myfile=open(a1, 'w')
        myfile.write(result)
        myfile.close()
        engine.save_to_file(result, a2) #saving as audio file

    else:
        print("Sorry! Wrong choice entered.\n")

elif (c=='N' or c=='n'):
    print("Okay! Results NOT saved.\n")
else:
    print("Sorry! Wrong choice entered.\n")

engine.runAndWait()