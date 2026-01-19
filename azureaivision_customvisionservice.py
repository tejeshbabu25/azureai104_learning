# In Azure AI Vision Custom Vision Service, this module provides functionalities to interact with the Custom Vision API.
# Create a custo vision service on Azure portal to get the endpoint and key.
# then log into https://www.customvision.ai/ and login with your Azure credentials.
# here we create a project of type as classification project type & multiclass "classification type" project
# once done, on this page you will be able to upload images with tags and train the model.
# ensure you upload at least 5 images per tag for better accuracy.


# Below is a sample code to interact with the Custom Vision Service using Python SDK.
# Publish the above trained model to an endpoint after training.
# before starting code ensure to install customvision package using below command
# pip install azure-cognitiveservices-vision-customvision

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json

# Below values are for customvision prediction endpoint and key

endpoint = "https://customvvisiontej2000-prediction.cognitiveservices.azure.com/"
key = "api_key_here"

credentials = ApiKeyCredentials(in_headers={"Prediction-Key": key})
prediction_client = CustomVisionPredictionClient(endpoint=endpoint, credentials=credentials)

image_data = open("classify_dog_test_file.jpg", "rb").read()
project_id = "97f540c7-e5a0-4de3-b5e4-81e4cbb087ed"
model_name="PetsModels"

response = prediction_client.classify_image(project_id, model_name, image_data)

for prediction in response.predictions:
    print(json.dumps(prediction.__dict__, indent=4))

# Below results will be printed on the console
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureaivision_customvisionservice.py
# {
#     "additional_properties": {},
#     "probability": 0.9981061,
#     "tag_id": "d2fc330a-19e3-43e2-9421-1d53ee004c7a",
#     "tag_name": "dogs",
#     "bounding_box": null,
#     "tag_type": "Regular"
# }
# {
#     "additional_properties": {},
#     "probability": 0.0018938313,
#     "tag_id": "3651ed09-b835-4e38-b7d7-3701a113aee1",
#     "tag_name": "cats",
#     "bounding_box": null,
#     "tag_type": "Regular"
# }