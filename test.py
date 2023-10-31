import os
import openai
import streamlit as st
from dotenv import load_dotenv


load_dotenv()
openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_key  = os.environ['OPENAI_API_KEY']
openai.api_base = os.getenv("OPENAI_API_BASE")

response = openai.ChatCompletion.create(
    engine="gpt-4",
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Where are the headquarters of Just Eat Takeaway.com?"}
    ]
)

st.title('Hackathon 2023')
st.write(response['choices'][0]['message']['content'])
# print(response['choices'][0]['message']['content'])
