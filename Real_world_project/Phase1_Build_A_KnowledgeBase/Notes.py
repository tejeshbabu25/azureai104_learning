# Project Phase - Building a KnowledgeBase
  # Build a resource based on Azure AI Language Service - Make sure to enable custom question and answers
  # For the source of questions, we will umport an existing set of questions - This is in the .tsv format(Tab-separated format)
  # We will add a follow-up prompt to showcase how this works
  # We then save and deploy our knowledgebase. This knowledgebase is accessible via an API endpoint
  # We then develop a simple Python program that would interact with this knowledge base and get answers to questions
  
# On Azure portal, create a new Azure AI Language resource with Custom Question and Answering enabled, this also 
# creates a Azure AI Search service resource in the background,not select a standard tier for search resource due to free tier limitations
# naviage to language studio from the Azure AI Language resource created - https://language.cognitive.azure.com/home
# We will be importing the question and answers available in course_support_qna.tsv file
# if you unable to log into language studio with same azure subscription account, copy the tenantId from Microsoft Entra ID and use it to login 
# to language studio using the URL - https://language.cognitive.azure.com/home?tenantId=<tenantId-goes-here>
# navigate to "Understand questions and conversations language" section and click on Custom question and answering
# Create a new project by clicking on New project button
# Give a name to the project, select the Azure AI Language resource created earlier and click on Create button
# Once the project is created, click on Files from Add source button and select the course_support_qna.tsv file to import the questions and answers
# Now "Edit Knowledge base" button will be enabled, click on it to view the imported questions and answers

# ****** follow-up prompt *******
# Follow-up prompts can be added to any of the questions by clicking on the question and then clicking on Add follow-up prompt button
# Add a follow-up prompt text and the answer to it and click on Save button to link them
# Once all the follow-up prompts are added, click on Save button on the top right corner to save the knowledge base
# for this example i added a new question as "Can you provide details on corporate pricing options?" and added it as a follow-up prompt 
# to "Do you offer corporate training packages"

# ****** Deploying the knowledge base ********
# Once the knowledge base is saved, click on Deploy button to deploy the knowledge base
# Once done, click on "Get prediction Url" and we can make use of curl cmd or python code to interact with the knowledge base
# My prediction endpoint URL is as below - https://langservice-tej13.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=mycustomQA&api-version=2021-10-01&deploymentName=production


# Sample Python code to interact with the knowledge base is on file cloudxeus_support_bot.py in this folder

# ****** Azure Functions *******
# Now our python code is only running locally, we can also deploy this code as an Azure Function and make it available as a web service
# On Azure portal , create a new "Function App" resource
# Select "App Service" plan type as "Consumption (Serverless)"

# ****** Installing Azure functions python package ******
# pip install azure-functions

# ****** function_app.py ******
# this is the code for the Azure Function that will interact with the knowledge base









