import time
import threading
import random
import math
import decimal
from functools import partial

class Sensor(threading.Thread):
    def __init__(self, callbackFunc, running):
        threading.Thread.__init__(self) # Initialize the threading superclass
        self.val = 0 # Set default sensor data to be zero
        self.running = running # Store the current state of the Flag
        self.callbackFunc = callbackFunc # Store the callback function



def gen(self):
    res = 0.0
    while True:
        yield float(res)
        res += 0.1
          

    def run(self):
        while self.running.is_set(): # Continue grabbing data from sensor while Flag is set
            time.sleep(0.2)  # Time to sleep in seconds, emulating some sensor process taking time
            #self.val = self.gen()
            self.val = random.randint(0, 10) # Generate random integers to emulate data from sensor
            #self.val = math.sin(self.val * 3.14 /180)
            self.callbackFunc.doc.add_next_tick_callback(partial(self.callbackFunc.update, self.val)) # Call Bokeh webVisual to inform that new data is available
        print("Sensor thread killed") # Print to indicate that the thread has ended