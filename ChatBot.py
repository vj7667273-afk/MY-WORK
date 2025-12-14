import time 
import random

name = input("Hello,what is your name?")

time.sleep(2)
print("Hello"+name)

feeling = input("how are you today?")

time.sleep(2)
if "good"in feeling:
    print("i am feeling good too!")
else :
    print("i am sorry to hear that!")

time.sleep(2)
favcolor = input("what is your favourite color")

colors=["red","green","blue"]

time.sleep(2)
print("my favourite color is"+random.choice(colors))