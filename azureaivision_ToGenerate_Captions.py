# This sample demonstrates how to generate captions for an image using Azure AI Vision Image Analysis SDK.
# Below Computer Vision service was created in Azure portal for this code to work.
# Service Name: comvision-tej
# first install the pip install azure-ai-vision-imageanalysis
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json

endpoint = "https://comvision-tej.cognitiveservices.azure.com/"
key = "api_key_here"
client=ImageAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

# Submitting image files for analysis
with open("man_cat_space.jpg", "rb") as image_file:
    image_details=image_file.read()

response = client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.CAPTION]
)

print(json.dumps(response.as_dict(), indent=4))

# Prints generate caption for the uploaded image as below
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureaivision_ToGenerate_Captions.py   
# {
#     "modelVersion": "2023-10-01",
#     "captionResult": {
#         "text": "a man in space suit with a cat in space suit",
#         "confidence": 0.7356247901916504
#     },
#     "metadata": {
#         "width": 573,
#         "height": 847
#     }
# }