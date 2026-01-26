# This feature allows you to build a conversation layer on top of your data
# using Azure Language Studio
# also ensure you have created Azure Search Service resource
# linking search to language AI service
    #  open your Azure language service
    # Featues - enable "Custom question answering"
            # - select your Azure AI search service

# once done, reload https://language.cognitive.azure.com/home
# select "Custom question answering"
# Create a Custom Question Answering project
# now edit knowledge base  by adding question answer pairs like below
    # question : How do i make a hotel reservation?
    # answer : You can make a reservation directly on our website by selecting your destination, travel dates , and number of rooms and guests.
# using manage sources you can use chitchat feature to add chitchat kind of knowledge
# now deploy the knowledge base by clicking on "Deploy Knowledge base"
# once done, this will also give a prediction URL

# to test the Url, use below command on Windows powershell to test the endpoint
# Invoke-WebRequest -Uri "https://langser-tej.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=knowledgebase&api-version=2021-10-01&deploymentName=production" `
# -Method POST `
# -Headers @{
# 			"Ocp-Apim-Subscription-Key"="api-key-goes-here";
# 			"Content-Type"="application/json"
# }`
# -Body '{"question":"I need to make a hotel reservation"}'

# Expected Response
# StatusCode        : 200
# StatusDescription : OK
# Content           : {
#                       "answers": [
#                         {
#                           "questions": [
#                             "How do i make a hotel reservation?"
#                           ],
#                           "answer": "You can make a reservation directly on our website by selecting your destination,
#                     tra...
# RawContent        : HTTP/1.1 200 OK
#                     csp-billing-usage: CognitiveServices.TextAnalytics.QuestionAnsweringTextRecords=1
#                     x-envoy-upstream-service-time: 1073
#                     apim-request-id: bea784ee-6f5a-42fb-87ab-d50fb5bd745b
#                     Strict-T...
# Forms             : {}
# Headers           : {[csp-billing-usage, CognitiveServices.TextAnalytics.QuestionAnsweringTextRecords=1],
#                     [x-envoy-upstream-service-time, 1073], [apim-request-id, bea784ee-6f5a-42fb-87ab-d50fb5bd745b],
#                     [Strict-Transport-Security, max-age=31536000; includeSubDomains; preload]...}
# Images            : {}
# InputFields       : {}
# Links             : {}
# ParsedHtml        : mshtml.HTMLDocumentClass
# RawContentLength  : 509




# We can now create bot by clicking on language studio after it was deployed
# Note : This bot is deployed as a Azure WebApp
# Once done you can test it out by going to all resources, selected azure bot service that you created, then go to Settings->test in web chat and asking questions
