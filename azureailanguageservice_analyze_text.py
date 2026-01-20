# install pip install azure.ai.textanalytics package before running this code
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://langser-tej.cognitiveservices.azure.com/"
key="api-key-goes-here"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

mydocuments = [
    "I love programming in Python! It's such a versatile language",
    "Me gusta aprender nuevos idiomas y explorar diferentes culturas."
]

response =client.detect_language(documents=mydocuments)

print(response)
