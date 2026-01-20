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

# Expected output:
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureailanguageservice_analyze_text.py
# [DetectLanguageResult(id=0, primary_language=DetectedLanguage(name=English, iso6391_name=en, confidence_score=0.98), warnings=[], statistics=None, is_error=False, kind=LanguageDetection), DetectLanguageResult(id=1, primary_language=DetectedLanguage(name=Spanish, iso6391_name=es, confidence_score=1.0), warnings=[], statistics=None, is_error=False, kind=LanguageDetection)]