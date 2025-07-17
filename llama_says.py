import requests
import pandas as pd
df=pd.read_excel("output.xlsx")
foldernames="\n".join(df.iloc[:,0].values)
prompt=prompt = f"""
I am organising my university folders. Here is the list:

{foldernames}

Please analyse and tell me ONLY:

{{
    "folder_path": "The exact folder path that is most relevant for storing Software Requirement Specification format files.",
    "confidence": "A confidence score out of 1.0 indicating how sure you are."
}}

Respond ONLY in this JSON format.
"""


response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2", 
        "prompt": prompt ,
        "stream": False}
)
data=response.json()
print('Generated Text: \n' ,data['response'])

