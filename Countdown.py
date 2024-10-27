import time
from playsound import playsound

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
        playsound('src/beeb.mp3')
    
    print('Timer Completed!')

t = input('Enter The time in second: ')

countdown(int(t))

