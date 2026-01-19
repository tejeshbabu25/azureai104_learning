# This sample demonstrates how to extract common tags from an image using Azure AI Vision Image Analysis SDK.
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
    visual_features=[VisualFeatures.TAGS]
)

print(json.dumps(response.as_dict(), indent=4))

# Prints common tags found in the image as below
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureaivisionforExtractingCommonTags.py
# {
#     "modelVersion": "2023-10-01",
#     "metadata": {
#         "width": 573,
#         "height": 847
#     },
#     "tagsResult": {
#         "values": [
#             {
#                 "name": "clothing",
#                 "confidence": 0.984424889087677
#             },
#             {
#                 "name": "pressure suit",
#                 "confidence": 0.9618092775344849
#             },
#             {
#                 "name": "astronaut",
#                 "confidence": 0.934812068939209
#             },
#             {
#                 "name": "outdoor",
#                 "confidence": 0.9297432899475098
#             },
#             {
#                 "name": "helmet",
#                 "confidence": 0.9194680452346802
#             },
#             {
#                 "name": "personal protective equipment",
#                 "confidence": 0.8479580283164978
#             },
#             {
#                 "name": "person",
#                 "confidence": 0.6970574855804443
#             },
#             {
#                 "name": "ground",
#                 "confidence": 0.6386427879333496
#             },
#             {
#                 "name": "protective garment",
#                 "confidence": 0.5343671441078186
#             }
#         ]
#     }
# }

