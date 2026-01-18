import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://tejes-mkiz7hea-eastus2.cognitiveservices.azure.com/",
    api_key="subscription_key_here",
)

with open("code.py", "r", encoding="utf-8") as code_file:
    code_content = code_file.read()

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant who teaches how to code.",
        },
        {
            "role": "user",
            "content": f"Explain clearly what the following Python code does:\n\n{code_content}"
        }
    ],
    max_completion_tokens =16384,
    model="gpt-5.2-chat"
)

print(response.choices[0].message.content)