📊 AI-Powered Document Analyzer with LLaMA-4
This project demonstrates a multi-format document loader and analyzer powered by Meta's LLaMA-4 Maverick language model via Together.ai. It supports a wide variety of document types including .csv, .xlsx, .txt, .pdf, .docx, and image files, enabling users to ask intelligent questions based on the extracted content.

🚀 Features
📁 Load and parse data from:

CSV, Excel (XLSX/XLS)

Text Files (TXT)

PDFs and DOCX

Image Files (JPG, PNG) using OCR

🧠 Ask intelligent questions about the content using LLaMA-4 Maverick (via Together.ai API)

📈 Designed for data analysts, researchers, and developers

🧾 File Types Supported
File Type	Description
.csv	Loads into a DataFrame
.xlsx	Loads into a DataFrame
.txt	Reads plain text
.pdf	Extracts text from pages
.docx	Extracts text from paragraphs
.jpg, .png	OCR to extract text from image

🧰 Requirements
Python 3.8+

Libraries:

pandas

pytesseract

Pillow

fitz (from PyMuPDF)

python-docx

together (for API interaction)

Install dependencies:

bash
Copy code
pip install pandas pytesseract pillow PyMuPDF python-docx together
Make sure Tesseract OCR is installed and configured correctly.
Windows users can download it here.

🔐 Setup
Set your Together.ai API key:

python
Copy code
os.environ["TOGETHER_API_KEY"] = "your_api_key_here"
🧪 Example Usage
python
Copy code
file_path = "path_to_file/sales_data.xlsx"
content = load_file(file_path)

if isinstance(content, pd.DataFrame):
    context = content.head(10).to_string()
else:
    context = content[:2000]  # Limit context for long texts

question = "What are the top 3 countries with the highest sales?"
answer = ask_llama(question, context)
print("Answer:", answer)
📦 Project Structure
bash
Copy code
.
├── analyzer.py           # Main script
├── README.md             # Project documentation
└── requirements.txt      # (Optional) List of dependencies
🧠 Powered By
Meta LLaMA-4 Maverick

Together.ai API

Tesseract OCR

📄 License
This project is for educational and non-commercial use only.
Please check individual library licenses for further restrictions.
