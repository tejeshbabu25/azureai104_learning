# To learn about Azure AI Language Service - Analyze Text API for Sentiment Analysis, please refer to the documentation at
# https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview
# This code sample demonstrates how to use Azure AI Language Service to perform sentiment analysis on given text

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://langser-tej.cognitiveservices.azure.com/"
key="api-key-goes-here"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

mydocuments = [
    "I love programming in Python! It's such a versatile language",
    "I do not like working while coffee is getting cold.",
    "The report had 20 points, out of which 15 were excellent, 3 were average, and 2 needed improvement.",
    "This is a 200 points"
]

# response =client.analyze_sentiment(documents=mydocuments)

# print(response)

# Expected output:
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureailanguageservice_analyzeText_to_SentimentAnalysis.py
# [AnalyzeSentimentResult(id=0, sentiment=positive, warnings=[], statistics=None, confidence_scores=SentimentConfidenceScores(positive=0.83, neutral=0.17, negative=0.0), sentences=[SentenceSentiment(text=I love programming in Python! , sentiment=positive, confidence_scores=SentimentConfidenceScores(positive=1.0, neutral=0.0, negative=0.0), length=30, offset=0, mined_opinions=[]), SentenceSentiment(text=It's such a versatile language, sentiment=positive, confidence_scores=SentimentConfidenceScores(positive=0.65, neutral=0.34, negative=0.01), length=30, offset=30, mined_opinions=[])], is_error=False, kind=SentimentAnalysis), AnalyzeSentimentResult(id=1, sentiment=negative, warnings=[], statistics=None, confidence_scores=SentimentConfidenceScores(positive=0.0, neutral=0.01, negative=0.99), sentences=[SentenceSentiment(text=I do not like working while coffee is getting cold., sentiment=negative, confidence_scores=SentimentConfidenceScores(positive=0.0, neutral=0.01, negative=0.99), length=51, offset=0, mined_opinions=[])], is_error=False, kind=SentimentAnalysis), AnalyzeSentimentResult(id=2, sentiment=neutral, warnings=[], statistics=None, confidence_scores=SentimentConfidenceScores(positive=0.01, neutral=0.99, negative=0.0), sentences=[SentenceSentiment(text=The report had 20 points, out of which 15 were excellent, 3 were average, and 2 needed improvement., sentiment=neutral, confidence_scores=SentimentConfidenceScores(positive=0.01, neutral=0.99, negative=0.0), length=99, offset=0, mined_opinions=[])], is_error=False, kind=SentimentAnalysis), AnalyzeSentimentResult(id=3, sentiment=neutral, warnings=[], statistics=None, confidence_scores=SentimentConfidenceScores(positive=0.02, neutral=0.97, negative=0.01), sentences=[SentenceSentiment(text=This is a 200 points, sentiment=neutral, confidence_scores=SentimentConfidenceScores(positive=0.02, neutral=0.97, negative=0.01), length=20, offset=0, mined_opinions=[])], is_error=False, kind=SentimentAnalysis)]

# to extract only sentiments from each document individually
response =client.analyze_sentiment(documents=mydocuments)

for result in response:
    print(f"Sentiment: {result.sentences[0].sentiment} - Sentence : {result.sentences[0].text}")

# Expected output:
#  PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureailanguageservice_analyzeText_to_SentimentAnalysis.py
# Sentiment: positive - Sentence : I love programming in Python! 
# Sentiment: negative - Sentence : I do not like working while coffee is getting cold.
# Sentiment: neutral - Sentence : The report had 20 points, out of which 15 were excellent, 3 were average, and 2 needed improvement.
# Sentiment: neutral - Sentence : This is a 200 points