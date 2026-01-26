# Create a resource on Azure portal for Document Intelligence (form recognizer) 
# For this example , we will be making use of Invoice Pre-built model as mentioned 
# on https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/invoice?view=doc-intel-4.0.0
# log into https://contentunderstanding.ai.azure.com/documentintelligence/studio and sign in with same Azure credentials
# lets start with Invoice model and click on it
# select the Subscription,RG and Document intelligence service you created on portal and click on continue & finish
# You can upload a document or use already uploaded document and click on Run Analysis and see how service uses document 
# intelligence to extract information and Result tab you would be able to see data in JSON format

# Below code is using python code to do the same
 # for our code, we will be uploading a Invoice onto Azure storage account service under a container
 # create a storage account service on Azure Portal
 # Once resource is created , navigate to resource and click on Data storage
 # Click on container and create a new container
 # upload a sample Invoice , once uploaded, click on the file name and it will provide you a url of the file, which can only be accessed
 # by a key. However, if you wanted to allow public account to this file, go to Settings->Configuration on storage account resource and click on 
 # configuration and enable "Allow Blob anonymous access" and then go to the container in which you uploaded a document 
 # and click on "Change access level" and select
 # "Blob (anonymous read access for blobs only)" to enable access to this python program as it is public

# program
# first install this package "pip install azure-ai-documentintelligence==1.0.0b4"
# Note : "prebuilt-invoice" is the model id for Read prebuilt model which we are using here

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

endpoint = "https://documentintel-tej.cognitiveservices.azure.com/"
key = "api-key-goes-here"
documentUrl = "https://storageaccounttej.blob.core.windows.net/docintelstorage/Sample_Invoice_Azure_Document_Intelligence.pdf"

client = DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response = client.begin_analyze_document("prebuilt-invoice",AnalyzeDocumentRequest(url_source=documentUrl))

result = response.result()

for index,invoice in enumerate(result.documents):
    print(f"Customer Name : {invoice.fields.get("CustomerName").get("valueString")}")
    print(f"Invoice Id : {invoice.fields.get("InvoiceId").get("valueString")}")
    print(f"SubTotal : {invoice.fields.get("SubTotal").get("content")}")
    

# Expected output for invoice.fields.get("CustomerName")
# Customer Name {'type': 'string', 'valueString': 'Fabrikam Solutions LLC', 'content': 'Fabrikam Solutions LLC', 'boundingRegions': [{'pageNumber': 1, 'polygon': [1.0802, 3.2688, 2.5732, 3.2675, 2.5733, 3.4155, 1.0803, 3.4168]}], 'confidence': 0.928, 'spans': [{'offset': 194, 'length': 22}]}

# Expected out for above code
# Customer Name : Fabrikam Solutions LLC
# Invoice Id : INV-2026-001
# SubTotal : $1,400

