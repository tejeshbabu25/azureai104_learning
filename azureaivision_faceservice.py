# learning face service using azure ai face service
# first install azure ai vision face package
# pip install azure-ai-vision-face


from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import *
import json

endpoint = "https://faceservice-tej.cognitiveservices.azure.com/"
key = "api_key_here"

client = FaceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

features_to_client =[
    FaceAttributeTypeDetection01.HEAD_POSE,
    FaceAttributeTypeDetection01.OCCLUSION,
    FaceAttributeTypeDetection01.ACCESSORIES
]

with open("sample_face.jpg","rb") as image_data:
    response = client.detect(
        image_content=image_data.read(),
        detection_model=FaceDetectionModel.DETECTION01,
        recognition_model=FaceRecognitionModel.RECOGNITION01,
        return_face_id=False,
        return_face_attributes=features_to_client
    )

print(json.dumps(response[0].as_dict(), indent=4))

# Results is printed in json format as below
# PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureaivision_faceservice.py
# {
#     "faceRectangle": {
#         "top": 157,
#         "left": 221,
#         "width": 244,
#         "height": 244
#     },
#     "faceAttributes": {
#         "headPose": {
#             "pitch": -0.9,
#             "roll": -7.7,
#             "yaw": -9.7
#         },
#         "accessories": [],
#         "occlusion": {
#             "foreheadOccluded": false,
#             "eyeOccluded": false,
#             "mouthOccluded": false
#         }
#     }
# }