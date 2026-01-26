# This is using the Read Model for hand written text to verify it is handwritten invoice
# I uploaded the "Sample_HandWrittenText_Azure_Document_Intelligence.png" on Document Intelligence Studio 
# under OCR/Read model to understand the run analysis and responses

# Python code to extract the text from sample handwritten image

# first install this package "pip install azure-ai-documentintelligence==1.0.0b4"
# Note : "prebuilt-read" is the model id for Read prebuilt model which we are using here

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult

endpoint = "https://documentintel-tej.cognitiveservices.azure.com/"
key = "api-key-goes-here"
documentUrl = "https://storageaccounttej.blob.core.windows.net/docintelstorage/Sample_HandWrittenText_Azure_Document_Intelligence.png"

client = DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response = client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=documentUrl))

result: AnalyzeResult = response.result()

# style is used to verify if the document is handwritten or not
for style in result.styles:
    if style.is_handwritten == True:
        print(f"Handwritten text, Confidence : {style.confidence}")

for index,para in enumerate(result.paragraphs):
    print(f"Paragraph {index+1}:{para.content}")


#Expected Output for only printing paragraphs
# Handwritten text, Confidence : 0.95
# Handwritten text, Confidence : 1
# Handwritten text, Confidence : 0.6
# Handwritten text, Confidence : 0.7
# Handwritten text, Confidence : 0.8
# Handwritten text, Confidence : 0.9
# Paragraph 1:Corner Store
# Paragraph 2:123 Market St. Austin, TX 78701 Ph: (512) 555- 1234
# Paragraph 3:Receipt # 89765
# Paragraph 4:Date: 04/15/2024
# Paragraph 5:Time: 2:45 PM
# Paragraph 6:Item
# Paragraph 7:Qty
# Paragraph 8:Price
# Paragraph 9:Total
# Paragraph 10:Coffee
# Paragraph 11:1
# Paragraph 12:$2.50
# Paragraph 13:$2.50
# Paragraph 14:Sandwich
# Paragraph 15:1
# Paragraph 16:$5.75
# Paragraph 17:$5.75
# Paragraph 18:Chips
# Paragraph 19:2
# Paragraph 20:$1.00
# Paragraph 21:$2.00
# Paragraph 22:Subtotal:
# Paragraph 23:$ 10.25
# Paragraph 24:Tax :
# Paragraph 25:$ 0.82
# Paragraph 26:Total :
# Paragraph 27:$ 11.07
# Paragraph 28:Paid with: Visa
# Paragraph 29:Auth #: A12345678
# Paragraph 30:Thank you!