# this code sample demonstrates how to use Azure AI Language Service to extract named entities of given text documents.
# install pip install azure.ai.textanalytics package before running this code
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://langser-tej.cognitiveservices.azure.com/"
key="api-key-goes-here"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

mydocuments = [
    "Satya Nadella announced at Microsoft Build that Python is a first-class language in Azure Functions.",
    "Companies revenue has increased by 25%"
]

# response =client.recognize_entities(documents=mydocuments)

# print(response)

# Expected output:
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureailanguageservice_analyzeText_to_extract_namedEntities.py
# [RecognizeEntitiesResult(id=0, entities=[CategorizedEntity(text=Satya Nadella, category=Person, subcategory=None, length=13, offset=0, confidence_score=1.0), CategorizedEntity(text=Microsoft Build, category=Event, subcategory=None, length=15, offset=27, confidence_score=0.8), CategorizedEntity(text=Python, category=Skill, subcategory=None, length=6, offset=48, confidence_score=1.0), CategorizedEntity(text=first, category=Quantity, subcategory=Ordinal, length=5, offset=60, confidence_score=0.98), CategorizedEntity(text=language, category=Skill, subcategory=None, length=8, offset=72, confidence_score=0.92), CategorizedEntity(text=Azure Functions, category=Product, subcategory=ComputingProduct, length=15, offset=84, confidence_score=0.8)], warnings=[], statistics=None, is_error=False, kind=EntityRecognition), RecognizeEntitiesResult(id=1, entities=[CategorizedEntity(text=25%, category=Quantity, subcategory=Percentage, length=3, offset=35, confidence_score=1.0)], warnings=[], statistics=None, is_error=False, kind=EntityRecognition)]
# Satya Nadella
# Microsoft Build
# first-class language
# Azure Functions
# Python
# to extract entities from each document individually
response =client.recognize_entities(documents=mydocuments)[0]

for entity in response.entities:
    print(f"Entity Text: {entity.text} , Category: {entity.category} ")

# Expected output:
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureailanguageservice_analyzeText_to_extract_namedEntities.py
# Entity Text: Satya Nadella , Category: Person 
# Entity Text: Microsoft Build , Category: Event 
# Entity Text: Python , Category: Skill 
# Entity Text: first , Category: Quantity 
# Entity Text: language , Category: Skill 
# Entity Text: Azure Functions , Category: Product 