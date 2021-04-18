# GPT-3 Makeathon
## Installation
Requirements: python >= 3.6, tested with 3.6.9. on linux.
```sh
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Secrets
Create a file called `.env` in the main directory and add your API key with the parentheses to the file like:
`OPENAI_API_KEY = "your_secret_numbers"`

## Run
```sh
streamlit run app.py
```