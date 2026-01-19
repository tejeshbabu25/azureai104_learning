# this is to learn from openai to extract details as text by uploading a pdf
# i had to use pdfplumber instead of pypdf as Sample_Invoice.pdf had some issues being read due to font used on it
# below values are from ai.azure.com , Models+endpoints section for gpt-5.2-chat
# for below response api version is 2025-03-01-preview
# update response type to output_text from choices[0].message.content as per new openai sdk
# use input instead of messages as per new openai sdk
from csv import reader
from openai import AzureOpenAI
import pdfplumber

client = AzureOpenAI(
    api_version="2025-03-01-preview",
    azure_endpoint="https://tejes-mkiz7hea-eastus2.cognitiveservices.azure.com/",
    api_key="endpoint key here"
)

def extract_pdf_text(path:str) -> str:
    parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            parts.append(page.extract_text() or "")
    return "\n".join(parts)

pdf_path = r"C:\Tejesh_Development\Python\Dev_Learning\azureai104_learning\Sample_Invoice.pdf"
pdf_text = extract_pdf_text(pdf_path)

response = client.responses.create(
    input=[
        {
            "role": "user",
            "content": 
            [
                {
                    "type": "input_text",
                    "text": f"Extract all the details from the following invoice text and present them in a structured text format:\n\n{pdf_text}"
                }
            ],
        }
    ],
    max_output_tokens =10000,
    model="gpt-5.2-chat"
)

print(response.output_text)

# # Expected output is structured text with invoice details like invoice number, date, items, total amount, etc.
# Scripts/python.exe c:/Tejesh_Development/Python/Dev_Learning/azureai104_learning/openai_Extract_details_as_text.py
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
# Below is a structured extraction of all details from the provided invoice text.  
# I’ve normalized formatting, corrected spacing issues, and organized the data into clear sections.

# ---

# ## Invoice Details

# - **Invoice Title:** Sample Invoice
# - **Invoice Number:** INV-2025-001
# - **Invoice Date:** 2025-07-17
# - **Due Date:** 2025-07-31

# ---

# ## Bill To

# - **Company Name:** Greenfield Technologies
# - **Contact Name:** John Smith
# - **Address:** 123 Technology Ave, Suite 400
# - **City:** New York
# - **State:** NY
# - **ZIP Code:** 10001
# - **Email:** john.smith@greenfieldtech.com

# ---

# ## Line Items

# | Item # | Description              | Quantity | Unit Price | Line Total |
# |------:|--------------------------|---------:|-----------:|-----------:|
# | 1 | Cloud Storage (100GB) | 2 | $50.00 | $100.00 |
# | 2 | Data Analysis Service | 10 | $20.00 | $200.00 |
# | 3 | Custom Reporting | 1 | $150.00 | $150.00 |

# ---

# ## Financial Summary

# - **Subtotal:** $450.00
# - **Tax Rate:** 10%
# - **Tax Amount:** $45.00
# - **Total Due:** $495.00

# ---

# ## Notes

# - Payment is due within 14 days.
# - Please reference the invoice number when making payment.
# - For questions, contact **accounting@yourservice.com** or call **(555) 123-4567**.
# - Thank you for your business!

# ---

# If you’d like this converted into **JSON, XML, CSV, or a database-ready format**, just let me know.