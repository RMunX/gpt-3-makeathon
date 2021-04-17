import os
import openai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

def main():
  """"Request a text from user, query it to API and display"""
  st.title("GPT3 Makeathon")
  st.header("HGF Challengers: Papent Applications")
  prompt = st.text_area("Enter your text")
  response = request(prompt)
  st.write(response.choices[0].text)

def request(prompt):
  """Request to Openais GPT3 API """
  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0,
    max_tokens=188,
    top_p=1,
    frequency_penalty=0.29,
    presence_penalty=0
  )
  return response

if __name__ == "__main__":
  main()
