# This code is to learn about the Azure AI Language Service Translator Service.
# create a resource on Azure portal for Translator Service before running this code.
# Make sure to install the required package: pip install azure-ai-translation-text==1.0.0b1
# note we need also specify the region when creating the client.
# also not TranslatorCredential is used instead of AzureKeyCredential for this service, which uses both key and region.
from azure.ai.translation.text import TextTranslationClient,TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

endpoint = "https://api.cognitive.microsofttranslator.com/"
region = "eastus"
key = "api-key-goes-here"

credential=TranslatorCredential(key,region)

client = TextTranslationClient(endpoint=endpoint, credential=credential)

source_language = "en"
target_language = ["it"]

input_text = "I like to learn new languages, like Italian."

documents = [InputTextItem(text=input_text)]

response = client.translate(content=documents, to=target_language, from_parameter=source_language)

print(f"Translated Text : {response[0].translations}")

# Expected output:
# Translated Text : [{'text': "Mi piace imparare nuove lingue, come l'italiano.", 'to': 'it'}]