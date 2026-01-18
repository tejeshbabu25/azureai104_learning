# this uses openai streaming responses so you can watch as the response is generated
# this is to learn from openai responses
# below values are from ai.azure.com , Models+endpoints section for gpt-5.2-chat
# for below response api version is 2025-03-01-preview
# update response type to output_text from choices[0].message.content as per new openai sdk
# use input instead of messages as per new openai sdk
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2025-03-01-preview",
    azure_endpoint="https://tejes-mkiz7hea-eastus2.cognitiveservices.azure.com/openai/responses?api-version=2025-04-01-preview",
    api_key="endpoint key here"
)

response = client.responses.create(
    input=[
        {
            "role": "system",
            "content": "You are a travel planner",
        },
        {
            "role": "user",
            "content": "I am going to USA, what should I see?",
        }
    ],
    max_output_tokens =10000,
    model="gpt-5.2-chat",
    stream=True
)

for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.output_text.done":
        print("\n[Done]")