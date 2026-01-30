# Creating your own Custom Models from the 2 types available
  # 1. Custom neural - Here you have a base model that has been trainer on a large set of documents. 
            # You then fin-tune the model with your own data set
            # This model supports extracting key data fields fromstructured,semi-structured 
            # and unstructured documents
            # You can start using this model first to see if it fits your needs
  # 2. Custom Template - Here there is a dependency on the submitted template. Here there needs to be
            # a consistent visual structure for your documents.
            # When training this model, you need to ensure that layout of the document is static in nature
            # The custom template model supports key-value pairs,tables etc.

# To create a Custom Model go to # log into https://contentunderstanding.ai.azure.com/documentintelligence/studio and sign in with same Azure credentials
    # In this, you get to choose between 2 types - Custom extraction model and custom classification model
    # for this example we will be creating Custom extraction model
# On your storage account , create a new container called survey and upload the surver sample pdfs
# Now on document intelligence studio, map to your azure subsciption and container you just created and 
# and create the project
# At the end of project creating you get to label by choosing either Run layout or Auto label, we skip for now
# Now we Run layout for unanalyzed document, and extracts the layouts of the forms
# Now we label each field on each document by clicking on each field,
# for bullet points we can use draw region and choose as selection field
# Once all fields are lable - train the model by assiging a a Model name
# Once Model is trained , click on the model you created, upload Survey_Customer_Satisfaction_Filled.pdf 
# file, verify how well the model is trained
