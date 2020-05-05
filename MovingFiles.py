from watchdog.observers import Observer
import time
import os
import json
from watchdog.events import FileSystemEventHandler

class Myhandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_take_files_from):
            src = folder_to_take_files_from + "/" + filename
            newdestination = new_location +"/"+filename
            os.rename(src, newdestination)
            print("[INFO] File Moved.")


folder_to_take_files_from = '/Users/kalharaperera/Desktop/n1'
new_location = '/Users/kalharaperera/Desktop/n2'
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_take_files_from, recursive=True)
observer.start()

try:
    while (True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    
observer.join()