import os
from sentence_transformers import SentenceTransformer
import pandas as pd
start_path = r"D:\fourth_semester"  
folder_list=[]
for root, dirs, files in os.walk(start_path):
    for directory in dirs:
        """ print(os.path.join(root,directory)) """
        folder_list.append(os.path.join(root,directory))
        
""" print("Folders scanned:", len(folder_list)) """

df=pd.DataFrame(folder_list)
print(df) 

model=SentenceTransformer('all-MiniLM-L6-v2')   
embeddings = model.encode(df[0].tolist(), show_progress_bar=True)
embeddings_df = pd.DataFrame(embeddings, index=df.index)
df_embedded = pd.concat([df, embeddings_df], axis=1)


