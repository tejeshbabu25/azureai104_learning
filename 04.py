import os
from openai import AzureOpenAI
import requests

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://tejes-mkizzx37-swedencentral.cognitiveservices.azure.com/openai/deployments/dall-e-3/images/generations?api-version=2024-02-01",
    api_key="subscription_key_here",
)

response = client.images.generate(
    prompt="A beautiful sun image overlooking from the moon",
    model="dall-e-3",
    n=1,
    size="1024x1024",
    quality="standard"
)

image_url = response.data[0].url

import_data = requests.get(image_url).content
with open("sunset_from_moon.png", "wb") as handler:
    handler.write(import_data)

print("Finished generating the image")