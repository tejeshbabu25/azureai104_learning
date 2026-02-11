# Company is exploring different GPT Models

# We will build side-by-side model comparision chat interface powered by Azure AI foundry
    # Step 1 : Deploy multiple GPT models - using Multi-Model deployments
        #   # -  create two deployments in Azure AI foundry each for GPT-4 and GPT-5
    # Step 2 : Deploy a Python Backed service using Azure OpenAI SDK
        # Implement a python module that"
            # - Sends user/system prompts to both models
            # - Returns responses with token usage details
            # - Integrates Azure Content Safety checks for every request.
            # - Package this service in a Docker container and deploy it to an Azure virtual machine
    # Step 3 : create a Chat-like frontend
            # - Develop a Reach.js web interface with two side-by-side panels: one each for GPT 4 and 5
            # - Deploy the front end as a static web app on azure storage
    # Step 4 : Provide Insights on Model Behavior
            # - Students will directly compare model outputs
            # - Track token usage to understand cost tradeoffs
            # - learn how content safety fileters integrate into real solutions


# *****   Step 1 - Deploy the models on Azure AI foundry *****
# On Azure Portal - create a "Azure AI Foundry"
# Once created navigate Foundry portal
    # On it, go to Model Catalog - click on gpt-5.2-chat and create a project and deploy the model with default options
    # Go to Model Catalog - click on gpt-4.1 and create a project and deploy the model with default options
    # under Models+endpoints we now have 2 endpoints
# *** python code to send request and verify responses ***
# now we write a simple python module to interface with these 2 LLMs on "1_chat_models_input_from_commandLine.py" file which takes input from command line  
# now we write a simple python module to interface with these 2 LLMs on "1_chat_models_input_from_docker_and_VMs.py" which is used deploy our code to docker, by installing
# docker on a Azure VM
# Use Azure Function to call the endpoint

# Build a VM on Azure VM Service
# On Azure portal, search for Virtual machine
# select auth type as password and create a user and pwd - - save them for later
# once resource is created,navigate to resources

# Docker installation on our VM we just created
# navigate to the Virtual Machine resourse that got created "mydocketVM"
# go to Help->Serial console and login with user and pwd created ealier
# for command to setup docker go to https://docs.docker.com/engine/install/ubuntu/
# execute below command to "Setup Docker;s apt repository" and press enter to install

# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update

# Once done, install the Docer packages by running below command
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# now we updated the 1_chat_models_input_from_docker_and_VMs.py file and also created a requirement.txt file to let docker know to install all the dependencies it needs
# .env files has all the keys for a respective environment
# To build a docket image, we now create a Dockerfile

# Building a dockerimage and running a container
# on portal->dockerVM->network settings -> click on create port rule-> add "inbound port rule" to allow connections from anywhere to any port number
# by setting "Destination port ranges" as *
# name it as "AllowAnyCustomAnyInbound" and click on Add
# now we need to copy files from local machine
# on we code, open a new terminal a below command , note IP address below is on docker VM resource overview page

scp .env dockerUsr@20.40.249.155:/home/dockerUsr

# do the same to add other files 
    # 1_chat_models_input_from_docker_and_VMs.py - scp 1_chat_models_input_from_docker_and_VMs.py dockerUsr@20.40.249.155:/home/dockerUsr
    # Dockerfile - scp Dockerfile dockerUsr@20.40.249.155:/home/dockerUsr
    # requirements.txt - scp requirements.txt dockerUsr@20.40.249.155:/home/dockerUsr
# verify files are uploaded by checking under help->Serial console and typing command as ls
# now we build the docker image by using below command on Serial console , model-chat below is a tag- it can be anything
sudo docker build -t model-chat .

# once done, you can verify the image created using 
sudo docker images command

# to Run this docker image
sudo docker run --env-file .env -p 8000:8000 model-chat

# once it is running - use below curl command to hit the endpoint and verify the response from VSCode terminal/cmd prompt

curl -X POST "http://20.40.249.155:8000/ask" -H "Content-Type:application/json" -d "{\"user_prompt\":\"Explain supervised vs unsupervised learning\",\"system_prompt\":\"You are a helpful AI teacher.\",\"history\":[]}

# Expected Response
# {"gpt-5":{"response":"**Supervised vs. Unsupervised Learning** are two main categories of machine learning, distinguished by whether labeled data is used.\n\n---\n\n## ✅ Supervised Learning\n\n**Definition:**  \nSupervised learning uses **labeled data**, meaning each training example includes both:\n- **Input (features)**  \n- **Correct output (label)**\n\nThe model learns a mapping from inputs to outputs.\n\n### Common Tasks\n- **Classification** → Predict a category  \n  - Example: Spam vs. not spam\n- **Regression** → Predict a numeric value  \n  - Example: House price prediction\n\n### Examples\n| Task | Input | Output |\n|----|----|----|\n| Email filtering | Email text | Spam / Not Spam |\n| Medical diagnosis | Patient data | Disease type |\n| Price prediction | House features | Price |\n\n### Common Algorithms\n- Linear Regression\n- Logistic Regression\n- Decision Trees\n- Random Forests\n- Support Vector Machines (SVM)\n- Neural Networks\n\n### Pros & Cons\n✅ Clear objective and measurable accuracy  \n❌ Requires labeled data, which can be expensive or time-consuming\n\n---\n\n## 🔍 Unsupervised Learning\n\n**Definition:**  \nUnsupervised learning uses **unlabeled data**. The model tries to discover hidden patterns or structures on its own.\n\n### Common Tasks\n- **Clustering** → Group similar data points  \n- **Dimensionality Reduction** → Reduce features while preserving structure\n- **Association Rule Learning** → Find relationships between variables\n\n### Examples\n| Task | Input | Output |\n|----|----|----|\n| Customer segmentation | Purchase history | Customer groups |\n| Topic modeling | Documents | Topics |\n| Anomaly detection | Network traffic | Unusual patterns |\n\n### Common Algorithms\n- K-Means\n- Hierarchical Clustering\n- DBSCAN\n- Principal Component Analysis (PCA)\n- Autoencoders\n- Apriori Algorithm\n\n### Pros & Cons\n✅ No labeled data required  \n❌ Results may be harder to interpret or evaluate\n\n---\n\n## 🔑 Key Differences\n\n| Aspect | Supervised Learning | Unsupervised Learning |\n|----|----|----|\n| Data | Labeled | Unlabeled |\n| Goal | Predict outcomes | Discover patterns |\n| Evaluation | Accuracy, RMSE, etc. | Harder, often qualitative |\n| Examples | Classification, Regression | Clustering, Dimensionality Reduction |\n\n---\n\n## 🧠 Simple Analogy\n- **Supervised Learning**: Learning with a teacher who provides correct answers.\n- **Unsupervised Learning**: Learning by exploring patterns without guidance.\n\nIf you’d like, I can also explain this with diagrams, code examples, or real-world case studies.","prompt_tokens":24,"completion_tokens":554,"total_tokens":578},"gpt-4":{"response":"Absolutely! Here’s a clear explanation:\n\n**Supervised Learning:**\n- In supervised learning, you train a model using a **labeled dataset**—that is, each input comes with the correct output.\n- The model learns to map inputs to the known outputs.\n- Examples:  \n  - **Classification:** Identifying if an email is spam or not (emails are labeled as \"spam\" or \"not spam\").\n  - **Regression:** Predicting house prices given information about the house (house price is the label).\n\n**Unsupervised Learning:**\n- In unsupervised learning, your data does **not have labels**. The model tries to find structure or patterns within the data on its own.\n- The objective is to discover hidden relationships or groupings.\n- Examples:  \n  - **Clustering:** Grouping customers with similar behaviors together.\n  - **Dimensionality Reduction:** Reducing data features while preserving important information (like compressing images).\n\n**Key Differences:**\n- Supervised: Uses labeled data, learns a mapping from inputs to outputs, mainly for prediction or classification.\n- Unsupervised: Uses unlabeled data, finds structure/patterns, mainly for grouping or data simplification.\n\n**Analogy:**  \nImagine a teacher:\n- **Supervised learning:** The teacher gives students questions *and* the correct answers to study from.\n- **Unsupervised learning:** Students get only the questions and must figure out how to group or organize them (e.g., by topic) themselves.","prompt_tokens":25,"completion_tokens":309,"total_tokens":334}}

# **** Azure AI content safety ****
# create a AI Content safety resource


