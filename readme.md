# GPT-3 Makeathon

## Installation
Requirements: python >= 3.6, tested with 3.6.9.
```sh
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Secrets
Add your API key to the .env file in the main directory with the parentheses like:
`OPENAI_API_KEY = "your_secret_numbers"`

## Run
```sh
streamlit run api-call.py
```