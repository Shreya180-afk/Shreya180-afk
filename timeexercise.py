name=input("enter your name= ")
import time
timestamp = time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
if(hour>=0 and hour<12):
    print("good morning",name)
elif(hour>=12 and hour<15):
    print("good noon",name)
elif(hour>=15 and hour<18):
    print("good evening ",name)
elif(hour>=18 and hour<=24):
    print("good night",name)
    