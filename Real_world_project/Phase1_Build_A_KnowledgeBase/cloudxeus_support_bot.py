# endpoint below is from Getprediction URL of deployed knowledge base
# api_key is from the Getprediction url sample request section and value for Oci-Apim-Subscription-Key header

import requests

endpoint="https://langservice-tej13.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=mycustomQA&api-version=2021-10-01&deploymentName=production"
api_key="ocip-apim-subscription-key-goes-here"
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

def ask_question_answer(question:str):
    data={
        "question": question,
        "top": 1
    }

    response = requests.post(endpoint, headers=headers, json=data)
    results=response.json()
    return results["answers"][0]

# Below code is to interact with the knowledge base using terminal and ask questions

print("Welcome to CloudXeus Support Bot!")
print("Type 'exit' to quit the bot.")

while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit"]:
        print("Exiting the bot. Goodbye!")
        break
    else:
        answer = ask_question_answer(user_question)
        print(f"Bot: {answer}")