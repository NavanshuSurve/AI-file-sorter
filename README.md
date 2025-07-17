# 📂 AI-based Automatic File Sorter

This project monitors your **Downloads folder** in real time and **automatically suggests or moves files** to the most relevant folder within your organised directory structure (e.g. "fourth_semester") using **semantic similarity via sentence embeddings**.

---

## 🚀 **Features**

✅ Monitors file creation, modification, and rename events  
✅ Extracts file names on download  
✅ Embeds file names and folder names using **MiniLM-L6-v2** embeddings  
✅ Compares embeddings to find the **most similar folder**  
✅ Suggests or automates the move to the suggested folder  
✅ Stores and loads embeddings efficiently using **pandas + Excel**

---

## 🔧 **Tech Stack**

- Python 3.10+
- [watchdog](https://pypi.org/project/watchdog/) for filesystem event monitoring  
- [sentence-transformers](https://www.sbert.net/) for semantic embeddings  
- [scikit-learn](https://scikit-learn.org/) for cosine similarity  
- pandas, openpyxl for Excel-based storage

---

## 🔧 **Requirements**

- Python 3.10+
- watchdog
- pandas
- sentence-transformers
- scikit-learn
- openpyxl
- llama-cpp-python (if using LLaMA local inference)
