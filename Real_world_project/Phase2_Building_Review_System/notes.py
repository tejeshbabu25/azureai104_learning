# On Azure portal, create a new resource of storage account of type Blob Storage
# create a new container as documents to store the reviews from customers
# upload the reviews.txt file to the container

# *** AI Search resource ***
# On Azure portal, create a new resource of AI Search service

# *** Add Data source ***
# Under AI Search resource -> Search Management -> Data source -> Add data source of type Azure Blob Storage

# *** Define an Index schema under Indexes ***
# To add an Index, click on Add under and paste the json from index.json file
# sentiment-index schema is created

# *** Build Indexer to populate the index from data source***
# Under Indexers , click on Add Indexer(JSON) and paste the json from indexer.json file, update the data source name
# once indexer is created, click on Run to populate the index
# under indexes -> sentiment-index -> Search explorer, you can run test queries to see the indexed data

# *** Create a skillset to enrich the data with AI capabilities ***
    # Document cracking skill to extract text from documents
    # field mapping to map the fields from data source to index
    # skillset execution to link the skillset to indexer
    # Output field mapping to map the enriched fields to index
    # Push into Indexer to run the indexer again to populate the index with enriched data
# For sentiment analysis we will need add a new resource of type Azure AI Service as sentiment analysis is not part of AI Search service by default
# On Azure portal, create a new resource of type Azure AI Service
# Under Search service -> Search Management -> Skillsets -> Add skillset (JSON) and paste the json from skill.json file
# on the "congnitiveServices" section, update the "key" value with the api key of Azure AI Service created above as this links the skillset to the AI service
# for the skills section, we have the documentation on https://learn.microsoft.com/en-us/azure/search/cognitive-search-predefined-skills to help with more skills
# for our example we are using skill of type "Microsoft.Skills.Text.V3.SentimentSkill" to analyze the sentiment of the reviews
# once skillset is created, go to indexes -> create a new index as sentiment-index01 and make sure the name of the sentimentScore field is set correctly as 
# it was mentioned as output field in the skillset
# Now go to indexers -> edit the existing indexer to update the target index to sentiment-index01, skillsetName as sentiment-indexer and add below section to the outputFieldMappings
#      {
#       "sourceFieldName": "/document/sentimentScore",
#       "targetFieldName": "sentimentScore",
#       "mappingFunction": null
#     }
# click on save, reset & Run to populate the new index with sentiment scores
# now going back to indexes -> sentiment-index01 -> Search explorer, you can run test queries to see the indexed data with sentiment scores as below

# {
#   "@odata.context": "https://reviewssearchservice.search.windows.net/indexes('sentiment-index01')/$metadata#docs(*)",
#   "@odata.count": 1,
#   "value": [
#     {
#       "@search.score": 1,
#       "id": "cmV2aWV3cy50eHQ1",
#       "content": "I absolutely loved the new restaurant the food was delicious and the staff were so friendly! The product stopped working after just two days, and I couldn't get any support. The meeting was scheduled for 3 PM and lasted about an hour. This book inspired me to\r\nchange the way I think about my career highly recommended! The flight was delayed for hours, and no explanation was given. The service was slow, but the waiter was very kind and the food was tasty. The report contains the quarterly financial data for all\r\ndepartments. I'm thrilled with how the project turned out we exceeded all our goals! The software keeps crashing and makes it hard to get any work done. While the design of the phone is beautiful, the battery life is really disappointing.\n",
#       "metadata_storage_name": "reviews.txt",
#       "metadata_storage_path": "https://datasourcetej.blob.core.windows.net/documents/reviews.txt",
#       "sentimentScore": "mixed"
#     }
#   ]
# }

# *** Text split skill ***
# update existing skillset to add a new skill of type "Microsoft.Skills.Text.V3.TextSplitSkill" to split the reviews into smaller chunks for better search experience
# add below section above the sentiment skill in the skills array
# {
#       "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
#       "name": "split-skill",
#       "description": "Split the document content into sentences",
#       "context": "/document",
#       "defaultlanguageCode": "en",
#       "textSplitMode": "sentences",
#       "maximumPageLength": 500,
#       "inputs": [
#         {
#           "name": "text",
#           "source": "/document/content",
#           "inputs": []
#         }
#       ],
#       "outputs": [
#         {
#           "name": "textItems",
#           "targetName": "sentences"
#         }
#       ]
#     },

# update the sentiment skill to use the splitted sentences as input
# "context": "/document/sentences/*",
# create a new index as sentiment-index02 with same schema as before and update the sentimentScore field to be of type Collection(Edm.String) as mentioned on splitskill_index.json
# update the indexer to use the new skillset and new target index sentiment-index02 and add below section to the outputFieldMappings as below, also on splitskill_indexer.json file

# {
#       "sourceFieldName": "/document/sentences/*",
#       "targetFieldName": "sentences",
#       "mappingFunction": null
# }
# update the exting "sourceFieldName": "/document/sentimentScore", to "sourceFieldName": "/document/sentences/*/sentimentScore" to map the sentiment scores for splitted each sentences

# save, reset & Run to populate the new index with sentiment scores for splitted sentences
# go back to indexes -> sentiment-index02 -> Search explorer, you can run test queries to see the indexed data with sentiment scores for each splitted sentences as below


# {
#   "@odata.context": "https://reviewssearchservice.search.windows.net/indexes('sentiment-index02')/$metadata#docs(*)",
#   "@odata.count": 1,
#   "value": [
#     {
#       "@search.score": 1,
#       "id": "cmV2aWV3cy50eHQ1",
#       "content": "I absolutely loved the new restaurant the food was delicious and the staff were so friendly! The product stopped working after just two days, and I couldn't get any support. The meeting was scheduled for 3 PM and lasted about an hour. This book inspired me to\r\nchange the way I think about my career highly recommended! The flight was delayed for hours, and no explanation was given. The service was slow, but the waiter was very kind and the food was tasty. The report contains the quarterly financial data for all\r\ndepartments. I'm thrilled with how the project turned out we exceeded all our goals! The software keeps crashing and makes it hard to get any work done. While the design of the phone is beautiful, the battery life is really disappointing.\n",
#       "metadata_storage_name": "reviews.txt",
#       "metadata_storage_path": "https://datasourcetej.blob.core.windows.net/documents/reviews.txt",
#       "sentences": [
#         "I absolutely loved the new restaurant the food was delicious and the staff were so friendly! ",
#         "The product stopped working after just two days, and I couldn't get any support. ",
#         "The meeting was scheduled for 3 PM and lasted about an hour. ",
#         "This book inspired me to\r\n",
#         "change the way I think about my career highly recommended! ",
#         "The flight was delayed for hours, and no explanation was given. ",
#         "The service was slow, but the waiter was very kind and the food was tasty. ",
#         "The report contains the quarterly financial data for all\r\n",
#         "departments. ",
#         "I'm thrilled with how the project turned out we exceeded all our goals! ",
#         "The software keeps crashing and makes it hard to get any work done. ",
#         "While the design of the phone is beautiful, the battery life is really disappointing.\n"
#       ],
#       "sentimentScore": "[\"positive\",\"negative\",\"neutral\",\"positive\",\"positive\",\"negative\",\"positive\",\"neutral\",\"neutral\",\"positive\",\"negative\",\"negative\"]"
#     }
#   ]
# }

# *** Defining Table projections ***
# Under Skillsets -> Add another skills known as shaper skill of type "Microsoft.Skills.Util.V3.ShaperSkill" to shape the output of the indexer to match the schema of the target index
# edit existing skillset below Shaperskill and table project under knowledgestore section as below

# {
#       "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
#       "name": "shape-sentence-row",
#       "description": "Turn each sentence into a row object for table projection",
#       "context": "/document/sentences/*",
#       "inputs": [
#         {
#           "name": "docName",
#           "source": "/document/metadata_storage_name"
#         },
#         {
#           "name": "sentence",
#           "source": "/document/sentences/*"
#         },
#         {
#           "name": "score",
#           "source": "/document/sentences/*/sentimentScore"
#         }
#       ],
#       "outputs": [
#         {
#           "name": "output",
#           "targetName": "row"
#         }
#       ]
#     }

#  "knowledgeStore": {
#     "storageConnectionString": "<take value from storage account -> access keys -> connection string>",
#     "projections": [
#       {
#         "tables": [
#           {
#             "tableName": "SentenceSentiment",
#             "generatedKeyName": "rowId",
#             "source": "/document/sentences/*/row",
#             "inputs": []
#           }
#         ],
#         "objects": [],
#         "files": []
#       }
#     ],
#     "parameters": {
#       "synthesizeGeneratedKeyName": true
#     }
#   }

# once saved reset sentiment-indexer and run it
# now we will have a new Table "SentenceSentiment" under "Data Storage -> Tables"
# also, Storage browser -> Tables - > click on newly created SentenceSentiment and we can
#  see the table created for each row from reviews.txt file in table format
# full json file can be found on tableProjections_skill.json