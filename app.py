import os
import openai
from dotenv import load_dotenv
import streamlit as st
#import logging
import time
import json

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
# logging.basicConfig(
#   filename="example.log", 
#   encoding="utf-8", 
#   level=logging.INFO, 
#   format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
#   datefmt="%Y/%m/%d %H:%M:%S"
# )

def main():
  """"Request a text from user, query it to API and display"""
  st.title("GPT3 Makeathon")
  st.header("HGF Challengers: Papent Applications")

  options = {
    "Summarize prior claims": "summary",
    "Create a problem description from the inventors problem description and a prior art example": "problem_description",
    "Create a solution description based on the inventors solution description and a prior art example": "solution_description"
    }
  choice = st.selectbox("What would you like to do?", tuple(options.keys()))
  with open("conf/conf.json") as f:
    conf = json.load(f)
  parameters = conf[options[choice]]

  # Create prompt from different inputs and commands
  if options[choice] == "summary":
    prompt = st.text_area("Enter your text")
    command = "\n\n\nOne-sentence summary:\n\n"
    prompt = f'{prompt}{command}'
  elif options[choice] == "problem_description":
    problem = st.text_area("Enter the problem")
    prior_art = st.text_area("Enter prior art")
    command = "\nDescribe the problem mentioned in the first text:\n"
    prompt = f'{problem}"""{prior_art}"""'
  elif options[choice] == "solution_description":
    solution = st.text_area("Enter the solution")
    prior_art = st.text_area("Enter prior art")
    command = "\nDescribe the solution proposed in text 1 like it was in text 2:\n"
    prompt = f'{solution}"""{prior_art}"""'

  # Generate response
  response = request(prompt, parameters)
  st.write(response.choices[0].text)

def request(prompt, param):
  """Request to Openais GPT3 API """
  #TODO: find out how to make stop work for empty stop sequences
  response = openai.Completion.create(
    engine=param["engine"],
    prompt=prompt,
    temperature=param["temperature"],
    max_tokens=param["max_tokens"],
    top_p=param["top_p"],
    frequency_penalty=param["frequency_penalty"],
    presence_penalty=param["presence_penalty"],
    stop=param["stop"]
  )
  return response

if __name__ == "__main__":
  main()
  