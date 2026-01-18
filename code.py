import os
from openai import AzureOpenAI
import base64

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://tejes-mkiz7hea-eastus2.cognitiveservices.azure.com/",
    api_key="subsciption_key_here",
)

with open("cats image.jpeg", "rb") as image_file:
    image_details = base64.b64encode(image_file.read()).decode("utf-8")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant who helps to describe images.",
        },
        {
            "role": "user",
            "content": 
            [
                {
               "type": "text",
                "text": "Give me a description of the what the image is trying to explain",
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_details}"
                }
                }
            ]
        }
    ],
    max_completion_tokens =16384,
    model="gpt-5.2-chat"
)

print(response.choices[0].message.content)