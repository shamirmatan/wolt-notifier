import sys
from datatypes import Restaurant
from time import localtime, strftime, sleep
import os

rest = str(sys.argv[1])
while True:
    status = Restaurant(rest).is_online()
    time = strftime("%H:%M:%S", localtime())
    if not status:
        print(f"[{time}] '{rest}' is closed")
    else:
        print(f"[{time}] '{rest}' is open")
        if os.uname().sysname == 'Darwin':
            os.system(f'say "{rest} is open"')
        break
    sleep(10)
