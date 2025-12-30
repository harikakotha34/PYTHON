#mini AI chatbot

import datetime
import time

name=input("welcome,enter your name :")
presentHour=datetime.datetime.now().hour

if 5<=presentHour<=11:
    print("Good morning. ",name)
elif 11<=presentHour<=17:
    print("Good afternoon, ",name)
elif 17<=presentHour<=20:
    print("Good evening, ",name)
else:
    print("good night, ",name)
time.sleep(1)


print("welcome to your  chatbot")
print("you can ask me basic question! type 'bye' to exit from the bot ")

#chatbot memory Creation [ dictionary of responses ]

responses={
    "hello":"Hi,welcome.How can I help you? ",
    "how are you":"Iam fine.Thank You",
    "who are you":"Iam smart AI chatbot",
    "motivate me":"keep going.Small steps every day lead to big results.",
    "happy":"Great to hear that",
    "what is python":"Python is a high-level, interpreted programming language,easy to read,write,and learn",
    "is python useful?":"Useful for Data Analyst roles,Helps in ML & Automation,Easy to use for ECE projects."

}
#Function to get response of Chatbot
def getResponseOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "Iam not able to tell that yet."

#take user input

while True: 
    userInput=input("Please ask your question:")
    reply=getResponseOfBot(userInput)
    print("Bot Response :",reply)

    if "bye" in userInput.lower():
        break