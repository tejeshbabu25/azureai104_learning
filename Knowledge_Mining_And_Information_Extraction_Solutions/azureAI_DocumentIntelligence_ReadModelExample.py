# This is to about Azure AI Document Intelligence as documented on 
# https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0

# Document Analysis Service
 # Cloud-based Azure AI service
 # Document analysis (general extraction) models enable text extraction from forms and documents 
 # and return structured business-ready content for your organization's action, use, or development.
 
# Create a resource on Azure portal for Document Intelligence (form recognizer) 
# For this example , we will be making use of Read Pre-built model as mentioned 
# on https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/read?view=doc-intel-4.0.0&tabs=sample-code
# log into https://contentunderstanding.ai.azure.com/documentintelligence/studio and sign in with same Azure credentials
# lets start with OCR/Read model and click on it
# select the Subscription,RG and Document intelligence service you created on portal and click on continue & finish
# You can upload a document or use already uploaded document and click on Run Analysis and see how service uses document 
# intelligence to extract information and Result tab you would be able to see data in JSON format

# Below code is using python code to do the same
 # for our code, we will be uploading a document onto Azure storage account service under a container
 # create a storage account service on Azure Portal
 # Once resource is created , navigate to resource and click on Data storage
 # Click on container and create a new container
 # upload a sample document , once uploaded, click on the file name and it will provide you a url of the file, which can only be accessed
 # by a key. However, if you wanted to allow public account to this file, go to Settings->Configuration on storage account resource and click on 
 # configuration and enable "Allow Blob anonymous access" and then go to the container in which you uploaded a document 
 # and click on "Change access level" and select
 # "Blob (anonymous read access for blobs only)" to enable access to this python program as it is public

# program
# first install this package "pip install azure-ai-documentintelligence==1.0.0b4"
# Note : "prebuilt-read" is the model id for Read prebuilt model which we are using here

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult

endpoint = "https://documentintel-tej.cognitiveservices.azure.com/"
key = "api-key-goes-here"
documentUrl = "https://storageaccounttej.blob.core.windows.net/docintelstorage/sample_pdf_document_intelligence_testing.pdf"

client = DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response = client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=documentUrl))

result: AnalyzeResult = response.result()

for index,para in enumerate(result.paragraphs):
    print(f"Paragraph {index+1}:{para.content}")


#Expected Output for only printing paragraphs
# Paragraph 1:1/26/26, 12:03 PM
# Paragraph 2:Back up and recover your conversational language understanding models - Foundry Tools | Microsoft Learn
# Paragraph 3:Back up and recover your conversational language understanding models
# Paragraph 4:When you create a Language resource in the Azure portal, you specify a region for it to be created in. From then on, your resource and all of the operations related to it take place in the specified Azure server region. It's rare, but not impossible, to encounter a network issue that hits an entire region. If your solution needs to always be available, then you should design it to either fail-over into another region. This process requires two Azure Language in Foundry Tools resources in different regions and the ability to sync your CLU models across regions.
# Paragraph 5:If your app or business depends on the use of a CLU model, we recommend that you create a replica of your project into another supported region. So that if a regional outage occurs, you can then access your model in the other fail-over region where you replicated your project.
# Paragraph 6:Replicating a project means that you export your project metadata and assets and import them into a new project. This action only makes a copy of your project settings, intents, entities, and utterances. You still need to train and deploy the models to be available for use with runtime APIs .
# Paragraph 7:In this article, you learn to use the export and import APIs to replicate your project from one resource to another existing in different supported geographical regions. We also provide guidance for keeping your projects in sync and the changes needed to your runtime consumption.
# Paragraph 8:Prerequisites
# Paragraph 9:· Two Language resources in different Azure regions, each of them in a different region.
# Paragraph 10:Get your resource keys endpoint
# Paragraph 11:Use the following steps to get the keys and endpoint for your primary and secondary resources. Go to your resource overview page in the Azure portal . From the menu on the left side, select Keys and Endpoint. You use the endpoint and key for the API requests
# Paragraph 12:https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/how-to/fail-over
# Paragraph 13:1/21
# Paragraph 14:1/26/26, 12:03 PM
# Paragraph 15:Back up and recover your conversational language understanding models - Foundry Tools | Microsoft Learn
# Paragraph 16:Home > All resources > MyDemoResource
# Paragraph 17:MyDemoResource | Keys and Endpoint ...
# Paragraph 18:Cognitive Services
# Paragraph 19:Search (Ctrl+/)
# Paragraph 20:Overview
# Paragraph 21:Activity log
# Paragraph 22:Access control (IAM)
# Paragraph 23:Tags
# Paragraph 24:Diagnose and solve problems
# Paragraph 25:Resource Management
# Paragraph 26:Quick start
# Paragraph 27:..........
# Paragraph 28:KEY 2
# Paragraph 29:......
# Paragraph 30:Endpoint
# Paragraph 31:https://mydemoresource.cognitiveservices.azure.com/
# Paragraph 32:Billing By Subscription
# Paragraph 33:Properties
# Paragraph 34:Locks
# Paragraph 35:Monitoring
# Paragraph 36:? Tip
# Paragraph 37:Keep a note of keys and endpoints for both primary and secondary resources. Use these values to replace the following placeholders: {PRIMARY-ENDPOINT}, {PRIMARY-RESOURCE-KEY} , {SECONDARY-ENDPOINT} , and {SECONDARY-RESOURCE-KEY}. Also take note of your project name, your model name, and your deployment name. Use these values to replace the following placeholders: {PROJECT-NAME}, {MODEL-NAME}, and {DEPLOYMENT-NAME} .
# Paragraph 38:Export your primary project assets
# Paragraph 39:Start by exporting the project assets from the project in your primary resource.
# Paragraph 40:Submit export job
# Paragraph 41:Replace the placeholders in the following request with your {PRIMARY-ENDPOINT} and {PRIMARY- RESOURCE-KEY} that you obtained in the first step.
# Paragraph 42:Create a POST request by using the following URL, headers, and JSON body to export your project.
# Paragraph 43:Request URL
# Paragraph 44:https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/how-to/fail-over
# Paragraph 45:2/21
# Paragraph 46:»
# Paragraph 47:Regenerate Key1 Regenerate Key2
# Paragraph 48:.- These keys are used to access your Cognitive Service API. Do not share your keys. Store them securely- for example, using Azure Key Vault. We also recommend regenerating these keys regularly. Only one key is necessary to make an API call. When regenerating the first key, you can use the second key for continued access to the service.
# Paragraph 49:Show Keys
# Paragraph 50:KEY 1
# Paragraph 51:Keys and Endpoint
# Paragraph 52:Pricing tier
# Paragraph 53:Networking
# Paragraph 54:Identity
# Paragraph 55:Location @
# Paragraph 56:westus









