# This sample demonstrates how to Optical Character Recognition (OCR) in an image using Azure AI Vision Image Analysis SDK.
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
with open("sample_OCR.png", "rb") as image_file:
    image_details=image_file.read()

response = client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.READ]
)

#print(json.dumps(response.as_dict(), indent=4)) # this prints the response in json format which inccludes boundingbox and text

for line in response.read.blocks[0].lines:
    print(f"{line.text}")
# Prints the texts from the image using OCR from the uploaded image as below
#  PS C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning> & C:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/.venv/Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/azureaivision_OCR.py
# CLIENTS
# AUTHENTICATION & AUTHORIZATION
# MONITORING & LOGGING
# OAuth
# JWT
# API Keys
# Metrics
# Error Tracking
# Web Browser Mobile App. Desktop App. IQT Device.
# Audit Logs
# HTTP Requests
# API GATEWAY
# (GET, POST, PUT, DELETE)
# · Routing
# CACHE
# . Authentication
# · Rate Limiting
# EXTERNAL SERVICES
# Redis / Memcached
# · Logging
# · 3rd Party APis
# · Payment Gateway
# MESSAGE QUEUE
# REST API SERVICE
# · Email Service
# W RabbitMQ
# B› Kafka
# Request
# Business
# Data
# Handler
# Logic
# Processing
# LOAD BALANCER
# H
# H
# SECURITY
# · Traffic Distribution
# · SSL/TLS Encryption
# · Failover
# · DDOS Protection
# · Firewall Rules
