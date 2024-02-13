import pyautogui as pt
import time

print('Process has been started.')
print('Now open the app you need to send message through and Click on person to send message.')
time.sleep(10)
msg = input('Enter Your message :- ')
run = int(input('Enter How many times you want to message :- '))
counter = 1
print('Now open you want to send message through and Do Not change The screen.')
time.sleep(5)
print('Now Just Sit Back.')
for i in range(run):
    pt.write(msg)
    time.sleep(0.05)
    pt.press('Enter')
    counter += 1
    print(counter)

print('Messages sent.')
