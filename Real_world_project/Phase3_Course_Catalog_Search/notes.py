# using search service again to search across all types of storage
# we will use multiple data storages - > cosmos db , storage accounts 
# On Azure Portal , create below service on phase 3 resource group
   # Search service under free tier
   # Cosmos DB for learning workload type and free tier
   # both under same region

# navigate to the cosmos db service -> Data Explorer -> Add New container of type database
# name as catalog
# create container under it and select existing database and add courses as container id,partution key as /courseId
# container throwput as manual and click on OK
# Once created , navigate to the catalog->courses->items and add each item from the items.json file individually

# On Azure portal create another storage account in the same region as above
# once created , create a new container named such as data
# upload all the folders available on "storagecontainer files" folder

# navigate to your search service created earlier and click on "import data" with existing data type and select Azure cosmos db
# give it a datasource name and in "Customize target Index", select the options(retrievable,filterable,sortable,facetable,searchable) for each field like courseid ,name 
# , description,price and category
# click on create a indexer and submit
# this wizard would have created "cosmosdb-index" index and you can go into it to test the index by clicking on search
# above the search button, we can select "JSON View" to define what columns you want to return from the search for example

# {
#   "search": "AI",
#   "count": true,
#   "select": "name,description,price,category"
# }

# returns only below

# {
#   "@odata.context": "https://coursesearchcatalog.search.windows.net/indexes('cosmosdb-index')/$metadata#docs(*)",
#   "@odata.count": 2,
#   "value": [
#     {
#       "@search.score": 1.9739704,
#       "name": "AI-900: Microsoft Azure AI Fundamentals",
#       "description": "Gain knowledge of fundamental AI and machine learning concepts and explore Azure AI services.",
#       "price": 99,
#       "category": "AI Fundamentals"
#     },
#     {
#       "@search.score": 1.839325,
#       "name": "AI-102: Designing and Implementing an Azure AI Solution",
#       "description": "Develop skills to build, manage, and deploy AI solutions using Azure Cognitive Services, Azure Cognitive Search, and Azure Bot Services.",
#       "price": 149,
#       "category": "AI Engineer"
#     }
#   ]
# }

# Since price column was set as filterable, updating search query as below returns only 1 course 

# {
#   "search": "AI",
#   "count": true,
#   "select": "name,description,price,category",
#   "filter": "price lt 100"
# }

#response
# {
#   "@odata.context": "https://coursesearchcatalog.search.windows.net/indexes('cosmosdb-index')/$metadata#docs(*)",
#   "@odata.count": 1,
#   "value": [
#     {
#       "@search.score": 1.9739704,
#       "name": "AI-900: Microsoft Azure AI Fundamentals",
#       "description": "Gain knowledge of fundamental AI and machine learning concepts and explore Azure AI services.",
#       "price": 99,
#       "category": "AI Fundamentals"
#     }
#   ]
# }

# *** creating another Index "azureblob-index" for storage account data ****

# assuming we have a App, when searching for AI-102 course , the search should search in cosmo db first and once it has the course name,
# then i goes into each folder on storage account which has document/images/transcipts and return all data relevant to this course
# so for that first we go into each file on documents folder add metadata by adding courceId as key and value as AI-102 for example
# repeat this for all files in Images and Transcipts folders
# creating a Axire Search Index for azure storage for creating the new index
# go to the search index and click on Import Data
# select Data source as "Azure Blob Storage" and name it
# Under ConnectionString click on Choose an existing connection and select your storageaccount->data , which has all your documents,images and transcripts
# click on add cognitive skills
# Add enrichments
# select "Enable OCR and merge all text into merged_content field", select "Enable OCR and merge all text into merged_content field" and
# "Generate captions from images" under "Image Cognitive Skills"
# select translate text and detect language under "Text cognitive skills" 
# Click customize "Target Index"
# you can notice courseId as one of the option as we added metadata for in above steps
# for courseId select retreivable,filerable
# click on Create an Indexer and submit
# now under Indexes, we have a new "azureblob-index" created
# click on it and click on seach to verify the results









