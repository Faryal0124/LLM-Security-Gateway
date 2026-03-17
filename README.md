
# LLM Security Mini Gateway

This project is a simple security layer for Large Language Models (LLMs).  
It checks user input before sending it to the model to make sure it is safe from attacks such as jailbreak, prompt injection detection etc

---

## What it does

- Detects prompt injection (malicious instructions)
- Detects personal data (PII) like phone numbers and emails
- Masks sensitive data
- Blocks harmful prompts
- Allows safe prompts

---

## How it works

1. The system checks the input for injection attacks and calculates a score  
2. It also checks the input for PII (phone numbers, emails, API keys)  
3. Both results are sent to the policy decision engine  
4. If injection score ≥ threshold → BLOCK  
5. If PII is detected → MASK  
6. Otherwise → ALLOW

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
