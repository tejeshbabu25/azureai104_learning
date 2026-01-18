import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://tejes-mkiz7hea-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2025-01-01-preview",
    api_key="subscription_key_here",
)

rag_params = {
    "data_sources":[
        {
            "type":"azure_search",
            "parameters":{
                "endpoint":"https://aisearch7897.search.windows.net",
                "index_name":"myindexongpt4",
                "authentication":{
                    "type":"api_key",
                    "key":"api_key_here",
                }
            }
        }
    ]
}

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what are Optimization Algorithms?",
        }
    ],
    max_tokens =16384,
    model="gpt-4.1",
    extra_body=rag_params
)

print(response.choices[0].message.content)

# when executed the output is: Optimization algorithms are methods designed to find the best solution or outcome for a given problem, often by maximizing or minimizing a particular objective function. Modern optimization algorithms focus on achieving faster convergence, utilizing adaptive learning rates, and employing black-box optimization techniques that leverage machine learning to improve perfor