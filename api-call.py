import os
import openai
from dotenv import load_dotenv

load_dotenv()
prompt_path = "prompt.txt"
with open(prompt_path, "r") as f:
  prompt = f.read()
print(prompt)

openai.api_key = os.environ.get("OPENAI_API_KEY")
response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=0,
  max_tokens=188,
  top_p=1,
  frequency_penalty=0.29,
  presence_penalty=0
)

print(100*'#')
print(response)
