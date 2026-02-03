# This is understand  about Azure AI Content Understanding service as metioned on https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview
# Azure Content Understanding in Foundry Tools is an Foundry Tool that's available as part of the Microsoft Foundry Resource in the Azure portal. It uses generative AI 
# to process and ingest many types of content, including documents, images, videos, and audio, into a user-defined output format. Content Understanding offers a
#  streamlined process to reason over large amounts of unstructured data, accelerating time-to-value by generating an output that you can integrate into automation 
# and analytical workflows.Content Understanding is now a generally available (GA) service with the release of the 2025-11-01 API version. It's now available in a 
# broader range of regions.
# Content Understanding in Foundry Tools is built on Azure AI services, including Azure Cognitive Services and Azure OpenAI Service. It leverages large language
#  models (LLMs). So , we have to create a Azure AI Foundry resource to use this service.
# I created aifoundryContentUnderstanding-tej-swedencentral as my Azure AI Foundry resource name in East US region to explore this service.
# from all resources , click on the new created foundry project and launch the Foundry Tools studio to explore the Content Understanding service on the left menu
# Content understanding preview version is only available in australiaeast, swedencentral and westus regions as of 02/02/2026
# CLick on Content Understanding  from the left menu , scroll down and click on try it out.
# Tried out Invoice Data Extraction sample by uploading a sample Sample_Invoice.pdf invoice document and an Analysis and verified fields it was able to extract from the document.
# Tried out Post Call Analysis, by using a already available on the studio and verified fields it was able to extract from the document.

# Creating Custom Task, in this case a Analyzer using Content Understanding service - check video 158 on Udemy course for steps
# Create a storage account and a container in it to store the documents to be analyzed on Azure portal
# Upload documents to be analyzed to the created container
# navigate to the storage account and click on Access Control (IAM) and assign "Storage Blob Data Contributor" role to the AI Foundry resource created earlier 
# under Add role assignment and give yourself under select members
# Now navigate to Foundry Tools studio and click on Content Understanding from the left menu
# Click on Custom Tasks tab and click on Create new task button
# if storage account does not show up in the list, go to manage connections and add a new connection to the storage account you created earlier
# Give a name to the task and select Analyzer as task type
# use sample filled survey document you had created earlier and create a sample schema for it by clicking on Create sample schema button by selecting Document
#  Analysis template
# Now you can add more fields to be extracted from the document by clicking on Add field button and selecting the field type and click on save button
# Now you can run analysis , you can see it was able to extract name, date from the document







