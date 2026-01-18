# below code is to learn about Azure Content Safety service for Text content moderation from REST service
# details can be found at https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Cwindows&pivots=programming-language-rest
# we will be using be command on powershell to call the REST service for content moderation from windows terminal
#take endpoint,key from Azure portal and open content safety resource -> go to Resource Management and click on Keys and endpoint
# copy paste below code into poweshell on windows or install Powershell extension on VS code and run the code after opening the file
Invoke-WebRequest -Uri "https://contentsafety-r.cognitiveservices.azure.com/contentsafety/text:analyze?api-version=2024-09-01" `
-Method POST `
-Headers @{
			"Ocp-Apim-Subscription-Key"="key from Azure portal";
			"Content-Type"="application/json"
}`
-Body '{"text":"Thinking to inducing drugs into the person","categories":["Hate","SelfHarm","Violence"]}'


# The response will be similar to below
# StatusCode        : 200
# StatusDescription : OK
# Content           : {"blocklistsMatch":[],"categoriesAnalysis":[{"category":"Hate","severity":0},{"category":"SelfHarm","severity":0},{"categor 
#                     y":"Violence","severity":4}]}
# RawContent        : HTTP/1.1 200 OK
#                     Transfer-Encoding: chunked
#                     apim-request-id: f31c68ca-c3b4-4d53-acde-6af7f7164cc5
#                     csp-billing-usage: CognitiveServices.ContentSafety.Text:Analyze=1
#                     api-supported-versions: 2023-04-3…
# Headers           : {[Transfer-Encoding, System.String[]], [apim-request-id, System.String[]], [csp-billing-usage, System.String[]],
#                     [api-supported-versions, System.String[]]…}
# Images            : {}
# InputFields       : {}
# Links             : {}
# RawContentLength  : 152
# RelationLink      : {}


