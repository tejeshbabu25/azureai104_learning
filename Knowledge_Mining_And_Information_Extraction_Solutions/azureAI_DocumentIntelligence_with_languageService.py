# This is to combine document intelligence service with language service
# We wil using the language service and storage service already created on Azure Portal
# upload Sample_Sentiment_Analysis_Text.pdf file onto storage account->container on portal
# Note , below code only worked when you have just bullet points on it without any other text around it

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = "https://documentintel-tej.cognitiveservices.azure.com/"
key = "api-key-goes-here"
documentUrl = "https://storageaccounttej.blob.core.windows.net/docintelstorage/Sample_Sentiment_Numbered_Only.pdf"

lang_endpoint = "https://langser-tej.cognitiveservices.azure.com/"
lang_key = "api-key-goes-here"

client = DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))
lang_client = TextAnalyticsClient(endpoint=lang_endpoint,credential=AzureKeyCredential(lang_key))

response = client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=documentUrl))

result:AnalyzeResult = response.result()

# for each_page in result.pages:
#     for index,line in enumerate(each_page.lines):
#         print(line.content)

# # Expected output
# Sample Text for Sentiment Analysis
# The following bullet points contain a mix of positive, negative, and neutral sentiments. They are
# designed to help you test sentiment analysis using Azure AI Language services.
# · I absolutely love how fast and responsive this application is.
# The user interface looks outdated and feels confusing to navigate.
# •
# · Customer support resolved my issue within minutes and was very polite.
# · The product works as expected, but there is nothing particularly impressive about it.
# . I am extremely disappointed with the frequent crashes and data loss.
# •
# The onboarding experience was smooth and easy to follow.
# · Pricing seems reasonable compared to other tools in the market.
# •
# The latest update introduced several bugs that made things worse.
# · Overall, the service meets basic requirements without any major issues.
# . I would highly recommend this solution to teams looking for reliability and performance.

documents = []
for each_page in result.pages:
    for index,line in enumerate(each_page.lines):
        documents.append(line.content)

lang_response = lang_client.analyze_sentiment(documents=documents)

for result in lang_response:
    print(f"Sentiment:{result.sentences[0].sentiment} - Sentence: {result.sentences[0].text}") 

# Expected output
# Sentiment:positive - Sentence: 1. I absolutely love how fast and responsive this application is.
# Sentiment:negative - Sentence: 2. The user interface looks outdated and feels confusing to navigate.
# Sentiment:positive - Sentence: 3. Customer support resolved my issue within minutes and was very polite.
# Sentiment:neutral - Sentence: 4. The product works as expected, but there is nothing particularly impressive about it.
# Sentiment:negative - Sentence: 5. I am extremely disappointed with the frequent crashes and data loss.
# Sentiment:neutral - Sentence: 6. The onboarding experience was smooth and easy to follow.
# Sentiment:positive - Sentence: 7. Pricing seems reasonable compared to other tools in the market.
# Sentiment:negative - Sentence: 8. The latest update introduced several bugs that made things worse.
# Sentiment:neutral - Sentence: 9. Overall, the service meets basic requirements without any major issues.
# Sentiment:positive - Sentence: 10. I would highly recommend this solution to teams looking for reliability and performance.