# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:30:22 2026

@author: Shahan
"""

# main.py

import time

from injec_detector import injection_score
from presidio_engine import analyze_pii
from policy_eng import policy_decision


def security_gateway(user_input):

    start_time = time.time()

    # Step 1: Injection detection
    score = injection_score(user_input)

    # Step 2: PII detection using Presidio
    pii_results = analyze_pii(user_input)

    # Step 3: Policy decision
    decision, output = policy_decision(score, pii_results, user_input)

    end_time = time.time()
    latency = end_time - start_time

    print("\n--- SECURITY GATEWAY RESULT ---")
    print("Injection Score:", score)
    print("PII Detected:", len(pii_results))
    print("Decision:", decision)
    print("Output:", output)
    print("Latency:", latency, "seconds")


if __name__ == "__main__":

    user_input = input("Enter your prompt: ")

    security_gateway(user_input)