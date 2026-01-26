# This is  to learn about the Azure AI Language Service Conversational Language Understanding (CLU) for analyzing conversational text.

# Key concepts:
  # Intent: The purpose or goal behind a user's input.
  # Entity: Specific pieces of information within the input that are relevant to the intent.
  # Utterance: A segment of text or speech that represents a single instance of communication.

# 1. Create a Language Resource
# 2. Create a project
# 3. Schema - Define Intents and Entities
# 4. Define Utterances
# 5. Train and deploy the model

# Sign in to https://language.cognitive.azure.com/ using the same as your Azure account.
# Select Resource Type as "Language"
# Once created , navigate to "Understand questions and conversational language"
# Click and create a project for Conversational Language Understanding
# assume your building hotal booking site
# Add Intents and Entities as per your requirement
    # Intent : BookHotel, CancelBooking, ModifyBooking, checkAvailability,greet
    # Entity : Location, Date, NumberOfGuests,RoomType
        # Click on each entities and define the entity type like Location as GeographyV2, Date as datetimeV2 etc.
    # Utterances: Sample phrases users might say for each intent.
        # for this perform Data Labeling
          # for example for Intent BookHotel add as "I want to book a hotel in New York for next weekend"
          # for Intent CancelBooking add as "I need to cancel my hotel reservation for tomorrow"
          # for Intent ModifyBooking add as "Can I change my hotel booking from single to double room?"
        # for each of the Utterances you need to label the entities present in the utterance. for example single room is RoomType entity.
# Add Utterances for training the model
# Training Set : Once you have added a sufficient number of labeled utterances, you can create a training set to train your model
# Testing Set : Add utterance to test the model by adding labels to entities
# Training Jobs :
    # Create a training job by selecting Standard training
    # in Model performance it shows how the Model is trained and details like F1 score,precision,recall,guidance,missingn intents in test set etc
# Now to use this Model, deploy it using "Deploying a Model"
# Go to "testing Deployments" and test your model

# Now using a python program to use this model
# install pip install azure-ai-language-conversations package
# Best practices can be found as https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/concepts/best-practices
    # choosing consistent schema
    # balancing training data
    # Clearly label utterances
    # Use None intent - when users give  out-of-content queries
# backup and recover - https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/how-to/fail-over
    # in case languague service is down as per documentation - make sure you have a lamguage service deployed on another region

from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://langser-tej.cognitiveservices.azure.com/"
key = "api-key-goes-here"

client = ConversationAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

utterance = "I need a double room for my family for the weekend"
project_name = "Trainingproject"
deployment_name = "myfirstModel"

response=client.analyze_conversation(
    task={
        "kind": "Conversation",
            "analysisInput":{
                "conversationItem":{
                    "participantId":"1",
                    "id":"1",
                    "modality":"text",
                    "language":"en",
                    "text":utterance
                },
                "isLoggingEnabled":False
            },
            "parameters":{
                "projectName":project_name,
                "deploymentName":deployment_name
            }
    }

)

print(response)

# Expected Response
# {'kind': 'ConversationResult', 'result': {'query': 'I need a double room for my family for the weekend', 'prediction': {'topIntent': 'BookHotel', 'projectKind': 'Conversation', 'intents': [{'category': 'BookHotel', 'confidenceScore': 0.62005097}, {'category': 'ModifyHotel', 'confidenceScore': 0.6076771}, {'category': 'CancelHotel', 'confidenceScore': 0.37151176}, {'category': 'checkAvailability', 'confidenceScore': 0}, {'category': 'greet', 'confidenceScore': 0}, {'category': 'None', 'confidenceScore': 0}], 'entities': [{'category': 'Date', 'text': 'the weekend', 'offset': 39, 'length': 11, 'confidenceScore': 1, 'resolutions': [{'resolutionKind': 'TemporalSpanResolution', 'timex': '2026-W05-WE', 'begin': '2026-01-31', 'end': '2026-02-02'}], 'extraInformation': [{'extraInformationKind': 'EntitySubtype', 'value': 'datetime.daterange'}]}]}}}






