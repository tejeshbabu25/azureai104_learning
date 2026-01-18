import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://tejes-mkiz7hea-eastus2.cognitiveservices.azure.com/",
    api_key="subscription_key_here",
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the tempature setting",
        }
    ],
    max_completion_tokens =16384,
    model="gpt-5.2-chat"
    #n=2 # Requesting 2 completions responses
)

print(response.choices[0].message.content)
#print(response.choices[1].message.content)
# printing responses in more readable json format import json library and use below statement
print(json.dumps(response.model_dump(), indent=2))