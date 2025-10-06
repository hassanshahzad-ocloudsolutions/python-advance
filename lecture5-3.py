#Daemon Threads

'''A daemon thread is a background thread that runs 
continuously to perform helper or maintenance tasks — but it does not block the program from exiting.'''

'''A daemon thread is like a background assistant — it keeps working quietly,
but if the main program ends, it is stopped immediately without cleanup.'''

'''Can be used for constantly reading the information from a file, constantly fetching data from 3rd party API
 and when the main program finishes they all will also be terminated'''

import threading
import time

path = "text.txt"
text = ""

#Runs this function with daemon thread.
def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

#Runs this function with simple thread
def printLoop():
    for x in range(5):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()

'''Real world use of Daemon Threads.

AutoSave, Auto-save helps during runtime; if the app closes, no need to keep saving.

Background Data Fetching, Fetches live data (news, weather, etc.) for display — not vital after exit.

Logging, Logs run continuously but are not critical when the program ends.


We use daemon threads for continuous, background, non-critical tasks that should not delay program termination.
'''


