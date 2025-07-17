import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import pandas as pd
import EventLibrary as el


folder=r"C:\Users\NAVANSHU\Downloads"

event=el.FileEventHandler()
obs=Observer()
obs.schedule(event,path=folder,recursive=False)
obs.start()
try:
    print("Observer has Started")
    while obs.is_alive():
            
        time.sleep(1)  # Keeps the main thread alive, checks if observer is still running
except KeyboardInterrupt:
    obs.stop
    obs.join
    print("Terminated")