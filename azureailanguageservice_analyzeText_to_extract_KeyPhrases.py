# this code sample demonstrates how to use Azure AI Language Service to extract key phrases of given text documents.
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

#response =client.extract_key_phrases(documents=mydocuments)

# print(response)

# Expected output:
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureailanguageservice_analyzeText_to_extract_KeyPhrases.py
# [ExtractKeyPhrasesResult(id=0, key_phrases=['versatile language', 'programming', 'Python'], warnings=[], statistics=None, is_error=False, kind=KeyPhraseExtraction), ExtractKeyPhrasesResult(id=1, key_phrases=['nuevos idiomas', 'diferentes culturas'], warnings=[], statistics=None, is_error=False, kind=KeyPhraseExtraction)]

# to extract key phrases from each document individually
response =client.extract_key_phrases(documents=mydocuments)[0]

for key_phrase in response.key_phrases:
    print(key_phrase)

# Expected output:
# (.venv) PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureailanguageservice_analyzeText_to_extract_KeyPhrases.py
# versatile language
# programming
# Python