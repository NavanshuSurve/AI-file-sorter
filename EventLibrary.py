import time
from sentence_transformers import SentenceTransformer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity



model=SentenceTransformer('all-MiniLM-L6-v2') 
df=pd.read_excel('output.xlsx')

# Assuming first column is folder path
foldernames=df.iloc[:,0].values
# Remaining columns are embeddings
foldervectors=df.iloc[:,1:].to_numpy() 

best_score=''
best_folder=''
def embedding(filename):
    filename_embedding=model.encode(filename)
    # Reshape filename embedding to 2D
    filename_embedding=filename_embedding.reshape(1,-1)

    similarities=cosine_similarity(filename_embedding,foldervectors)

    similarities=similarities.flatten()

    index=np.argmax(similarities)#most similar index

    best_folder=foldernames[index]

    best_score=similarities[index]

    print("Most similar folder:", best_folder)
    print("Similarity score:", best_score)




def is_temporary_file(filename):
    temp_extensions = ('.crdownload', '.opdownload', '.part', '.tmp')
    return filename.endswith(temp_extensions)
    
class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.recent_events = {}  # file name -> timestamp

    def is_recent(self, path, event_type, threshold=2):
        now = time.time()
        key=(path,event_type)
        last_time = self.recent_events.get(key, 0)
        self.recent_events[key] = now
        return (now - last_time) < threshold

    def process_event(self, action, path):
        filename = os.path.basename(path)
        if is_temporary_file(filename):
            return

        if not self.is_recent(path,action):
            print(f"[{action}] {filename}")
            embedding(filename)
            

    """ def on_created(self, event):
        if not event.is_directory:
            self.process_event("Created", event.src_path) """

    def on_moved(self, event):
        if not event.is_directory:
            # Process destination file only
            self.process_event("Moved", event.dest_path)
            



    """ def on_modified(self, event):
        if not event.is_directory:
            self.process_event("Modified", event.src_path)
 """
        