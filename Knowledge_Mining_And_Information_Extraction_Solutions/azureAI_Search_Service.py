# Azure AI Search service is a cloud service that provides search capabilities across your expansive data sources.
# Allows you to add search capabilities to your applications
# You have the ability to index documents and data from a variety of data sources

# Create a Azure AI Search service resource on Azure portal
# Go to Azure portal -> Create a resource -> Search for Azure AI Search service and create a new resource

# Search Index 
    # The Azure search service searches for data within the search index
    # You can perform a full-text search, a vector search, or a hybrid search that combines both full-text and vector search capabilities.
    # The search index is likened to a table. It has a defined schema.
    # The search index then contains documents like rows in a table.
    # if we add more than one field attributes to the index schema, then the storage size increases and the cost increases as well.
    # Internally an Index is distributed across partitions
    # An index is always available and can't be paused or taken offline

# Field attributes - This definies how the field can be used
    # Searchable - full text/vector search on the field
    # Filterable - filter results based on field value/queries
    # Sortable - sort results based on a score,but sorted based on fields within the document
    # Facetable - categorize results based on field value
    # Retrievable - include field in search results
    # Key - uniquely identifies each document in the index

# Indexers - Indexers are used to automate the process of populating a search index with data from an external data source
    # This is the crawler that extracts the data from the data source and loads it into the search index
    # It does a field to field mapping between the data source and the search index
    # The indexer can run on demand or based on a schedule
    # There is support for different data sources that include Azure blob storage, Azure SQL database, SQL Server on Axure VMs
    # If you need multiple inderxer jobs to run concurrently, you need to increase the replica count of the search service
    # When an inderxer job runs for the first time, it reads all the data in the source and then populates the indexer
    # Subsequent runs of the indexer are incremental, meaning that only the data that has changed since the last run is read and updated in the index

# create a new storage account and a container in it to store documents to be indexed
# Upload sample documents to the created container

# navigate to the created Azure AI Search service resource on Azure portal
# click on Overview -> import data -> select Azure Blob storage as data source -> provide connection details to the storage account and container where documents are stored
# note this automatically creates indexes,inderxer and data source for you based on the documents in the container
# During import data wizard, you can select "Azure blob storage" as data source type, provide connection details to the storage account and container where documents are stored
# You can modify the index schema and field attributes before creating the index - leaving default settings is fine for now
# Once the index is created, you can run the indexer to populate the index with data
# On the AI search service resource, Click on Search Management -> Data sources , you can see the created data source
# Click on Indexes, you can see the created index - this is another table pointing to the data source
# Click on Indexers, you can see the created indexer
# under indexes tab, click on the created index and then click on Search explorer
# In search explorer, you can run search queries against the index to retrieve documents

# Creating a skillset and using cognitive skills to enrich the data during indexing
# Skillsets are used to define a series of cognitive skills that are applied to the data during the indexing process to extract additional information and insights from the data
# Nabigate to the storage account and upload more documents
# Navigate to the Azure AI Search service resource on Azure portal, Click on Import Data -> select the same data source as earlier - > click on Add cognitive skills
# click on Add enrichments , enable OCR, scroll down and under Text cognitive skils , select applicable skills like Language detection, key phrase extraction,
#  entity recognition, Organization names , location names
# click on next and create a new  index - you can modify the index schema and field attributes before creating the index - leaving default settings is fine for now
# Navigate to the newly created index and click on Search explorer
# In search explorer, you can run search queries against the index to retrieve documents along with enriched data extracted using cognitive skills

# Knowledge store - Is the secondary storage for AI-enriched content that is created by a skillset in Azure AI Search service
# Documentation : https://learn.microsoft.com/en-us/azure/search/knowledge-store-concept-intro?tabs=portal
# It allows you to store and manage the enriched data separately from the search index within AI search resource, enabling advanced analytics and reporting scenarios
# A knowledge store is defined inside a skillset definition and it has two components
    # 1. A connection string to Azure storage
    # 2. Projections - defines how the enriched data is mapped to the knowledge store, whether its a table,objects or files, projection element is an array.

# "knowledgeStore": {
#     "storageConnectionString":"<YOUR-AZURE-STORAGE-ACCOUNT-CONNECTION-STRING>",
#     "projections":[
#        {
#           "tables":[ ],
#           "objects":[ ],
#           "files":[ ]
#        }
#     ]
# }

# we are exploring the table projection here - which stores non structured data in tabular format in Azure Table storage, or NoSQL data
# explored partition key and entity key while creating table projections

# Create a new container for images and Upload a image on the storage account container to test the knowledge store functionality
# navigate to the Azure AI search service resource on Azure portal, Click on Import Data -> select the same data source as earlier - > click on Add cognitive skills
# CLick on Add enrinchments , enable OCR , scroll down and under Text cognitive skils , select applicable skills like Language detection, key phrase extraction,
# under Image cognitive skills , select Generate tags from images, generate captions from images
# Now under "Save enrichments to a knowledge store", select Image projection, select the existing connection to the storage account and images container created earlier
# Also select Key phrases,Entities and image details under Azure table projections and click on Customize target index
# Create a new index and note you now have additional fields like imagetags,imagecaptions etc
# Create the index and run the indexer to populate the index
# Once this is fully created, navigate to the storage account and click on Tables under Table storage
# You can see a new table created with the name of the index like azureblobSkillset3Entities,azureblobSkillset3Images,& azureblobSkillset3KeyPhrases
# click on the storage browser and navigate to Tables -> click on azureblobSkillset3Images table , you can see the table containing partition key, 
# row key( unique identifier for each image document), imagesid,description,tags etc
# also when you go to the images container, you can see "azureblob-skillset3-image-projection", you can see the predictions
