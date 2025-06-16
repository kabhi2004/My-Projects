import os
import pandas as pd
from docx import Document
import fitz  
from PIL import Image
import pytesseract

def get_file_extension(file_path):
    return os.path.splitext(file_path)[-1].lower()

def load_file(file_path):
    ext = get_file_extension(file_path)
    
    if ext == '.csv':
        df = pd.read_csv(file_path)
        return df
    
    elif ext in ['.xlsx', '.xls']:
        df = pd.read_excel(file_path)
        return df
    
    elif ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return text

    elif ext == '.pdf':
        text = ''
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        return text

    elif ext == '.docx':
        doc = Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text

    elif ext in ['.png', '.jpg', '.jpeg']:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
    
    else:
        return "Unsupported file type."
    
import together
import os
os.environ["TOGETHER_API_KEY"] = "eb5c67bac544bbe54e9734d222f4d910a3a2ad55856b984d9d99cca224403799"

def ask_llama(question, context=""):
    prompt = f"""You are a helpful data analyst AI. Use the context below to answer the question accurately.

Context:
{context}

Question: {question}
Answer:"""

    response = together.Complete.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        prompt=prompt,
        max_tokens=512,
        temperature=0.7,
        top_p=0.9,
    )
    return response['choices'][0]['text'].strip()

# from google.colab import files
# uploaded = files.upload()
file_path = "C:\\Users\\DELL\\Downloads\\sales_data.xlsx"
content = load_file(file_path)
print(content)

content = load_file(file_path)

if isinstance(content, pd.DataFrame):
    context = content.head(10).to_string() 
else:
    context = content[:2000] 
question = "What are the top 3 countries with the highest sales?"
answer = ask_llama(question, context)
print(" Answer:", answer)
