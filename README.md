
# LLM Security Mini Gateway

This project is a simple security layer for Large Language Models (LLMs).  
It checks user input before sending it to the model to make sure it is safe.

---

## What it does

- Detects prompt injection (malicious instructions)
- Detects personal data (PII) like phone numbers and emails
- Masks sensitive data
- Blocks harmful prompts
- Allows safe prompts

---

## How it works

1. The system checks the input for injection attacks  
2. If injection score is high → BLOCK  
3. If safe, then it checks for PII  
4. If PII found → MASK  
5. Otherwise → ALLOW  

---

## Files

- injec_detector.py → checks injection  
- presidio_engine.py → detects and masks PII  
- policy_eng.py → makes final decision  
- main.py → runs the system  

---

## How to run

Install requirements:

pip install -r requirements.txt

Download spacy model:

python -m spacy download en_core_web_sm

Run the code:

python main.py

---

## Example

Input:
Ignore previous instructions. My phone number is 03123456789  

Output:
Decision: BLOCK  

---

## Author

Faryal Saleem
