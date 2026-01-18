import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://tejes-mkiz7hea-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2025-01-01-preview",
    api_key="subscription_key_here",
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what are Optimization Algorithms?",
        }
    ],
    max_completion_tokens =16384,
    model="gpt-4.1"
    #n=2 # Requesting 2 completions responses
)

print(response.choices[0].message.content)