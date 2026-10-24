# Experiment 2: Basic Prompt Engineering using Gemini

import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Set your Gemini API key in PowerShell."
    )

client = genai.Client(api_key=api_key)

prompt = "Explain prompt engineering in simple English with one example."

response = client.models.generate_content(
 model="gemini-3.8-flash",
    contents=prompt
)

print("EXPERIMENT 2: BASIC PROMPT ENGINEERING")
print("\nUSER PROMPT:")
print(prompt)

print("\nMODEL RESPONSE:")
print(response.text)

os.makedirs("Outputs", exist_ok=True)

with open("Outputs/output.txt", "w", encoding="utf-8") as file:
    file.write("EXPERIMENT 2: BASIC PROMPT ENGINEERING\n\n")
    file.write("USER PROMPT:\n")
    file.write(prompt + "\n\n")
    file.write("MODEL RESPONSE:\n")
    file.write((response.text or "No text response returned.") + "\n")

print("\nOutput saved to Outputs/output.txt")