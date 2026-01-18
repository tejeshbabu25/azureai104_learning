# this is to learn about Azure Content Safety service for Text content moderation
#only delealing with Azure AI services and not OpenAI services
# from terminal install the required package:pip install azure.ai.contentsafety
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeTextOptions

#below values are from Azure portal and Content Safety resource -> keys and endpoint from Resource Management
endpoint = "https://contentsafety-r.cognitiveservices.azure.com/"
key = "key from Azure portal"

client=ContentSafetyClient(endpoint,AzureKeyCredential(key))
txt="I want to hurt myself, I want to just inflict pain and suffering."
request = AnalyzeTextOptions(text=txt)

response = client.analyze_text(request)

print(response)
# prints response as {'blocklistsMatch': [], 'categoriesAnalysis': [{'category': 'Hate', 'severity': 0}, {'category': 'SelfHarm', 'severity': 4}, {'category': 'Sexual', 'severity': 0}, {'category': 'Violence', 'severity': 0}]}