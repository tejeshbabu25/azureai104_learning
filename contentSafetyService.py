#only delealing with Azure AI services and not OpenAI services
# from terminal install the required package:pip install azure.ai.contentsafety
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeImageOptions,ImageData

#below values are from Azure portal and Content Safety resource -> keys and endpoint from Resource Management
endpoint = "https://contentsafety-r.cognitiveservices.azure.com/"
key = "endpoint key from Azure portal"

client=ContentSafetyClient(endpoint,AzureKeyCredential(key))
with open("content_safety_sample.jpg", "rb") as image_file:
    request = AnalyzeImageOptions(image=ImageData(content=image_file.read()))

response = client.analyze_image(request)

print(response)
# prints response as {'categoriesAnalysis': [{'category': 'Hate', 'severity': 0}, {'category': 'SelfHarm', 'severity': 2}, {'category': 'Sexual', 'severity': 0}, {'category': 'Violence', 'severity': 2}]}