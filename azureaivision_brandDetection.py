# This sample demonstrates how to detect brands in an image using Azure AI Vision Image Analysis SDK.
# notes latest ai services does not have brand detection feature , we are going to install older version of sdk to demonstrate brand detection
# using pip install azure.cognitiveservices.vision.computervision
# Below Computer Vision service was created in Azure portal for this code to work.
# Service Name: comvision-tej
# first install the pip install azure-ai-vision-imageanalysis
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

endpoint = "https://comvision-tej.cognitiveservices.azure.com/"
key = "api_key_here"
client=ComputerVisionClient(endpoint,credentials=CognitiveServicesCredentials(key))

features = [VisualFeatureTypes.brands]


with open("sample_brand.jpg", "rb") as image_file:
    response = client.analyze_image_in_stream(image_file, visual_features=features)

for brand in response.brands:
    print(f"Brand Name: {brand.name}, Confidence: {brand.confidence}, Bounding Box: {brand.rectangle}")

# Prints the detected brands from the image along with confidence score and bounding box as below
# Brand Name: Microsoft, Confidence: 0.871, Bounding Box: {'additional_properties': {}, 'x': 63, 'y': 271, 'w': 123, 'h': 108}