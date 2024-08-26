import pdfplumber
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

pdf_text = extract_text_from_pdf('Politica_de_Privacidade.pdf')
print(pdf_text)

llm = OpenAI(api_key=openai_api_key)

prompt_template = PromptTemplate(template="Por favor, processe o seguinte texto: {text}")
formatted_prompt = prompt_template.format(text=pdf_text)

response = llm(formatted_prompt)
processed_text = response.get('choices', [{}])[0].get('text', '')
print(processed_text)

client = chromadb.Client()
collection = client.create_collection(name="policy_text")

collection.add(documents=[{"text": processed_text}])
