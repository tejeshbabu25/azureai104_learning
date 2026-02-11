from openai import AzureOpenAI
from typing import Dict, Any, List
import os
from fastapi import FastAPI, Body
from pydantic import BaseModel,Field

GPT5_ENDPOINT = os.getenv("AZURE_GPT5_ENDPOINT")
GPT5_KEY = os.getenv("AZURE_GPT5_KEY")
GPT5_DEPLOYMENT = os.getenv("AZURE_GPT5_DEPLOYMENT")
GPT5_API_VERSION=os.getenv("AZURE_GPT5_VERSION")

GPT4_ENDPOINT = os.getenv("AZURE_GPT4_ENDPOINT")
GPT4_KEY = os.getenv("AZURE_GPT4_KEY")
GPT4_DEPLOYMENT = os.getenv("AZURE_GPT4_DEPLOYMENT")
GPT4_API_VERSION=os.getenv("AZURE_GPT4_VERSION")

MAX_TOKENS=5000

client_gpt5 = AzureOpenAI(
    api_key=GPT5_KEY,
    api_version=GPT5_API_VERSION,
    azure_endpoint=GPT5_ENDPOINT
)

client_gpt4 = AzureOpenAI(
    api_key=GPT4_KEY,
    api_version=GPT4_API_VERSION,
    azure_endpoint=GPT4_ENDPOINT
)

app = FastAPI(title="Chat API")

class ChatRequest(BaseModel):
    user_prompt: str
    system_prompt: str = "You are a helpful assistant"
    history: List[Dict[str, str]] = Field(default_factory=list)

@app.post("/ask")
def ask_models(req: ChatRequest)-> Dict[str, Any]:
    history = req.history or []

    results = {}

    response5 = client_gpt5.chat.completions.create(
        model=GPT5_DEPLOYMENT,
        messages=[
            {"role": "system", "content": req.system_prompt},
            *history,
            {"role": "user", "content": req.user_prompt}
        ],
        max_completion_tokens=MAX_TOKENS
    )

    results["gpt-5"] = {
        "response": response5.choices[0].message.content,
        "prompt_tokens": response5.usage.prompt_tokens,
        "completion_tokens": response5.usage.completion_tokens,
        "total_tokens": response5.usage.total_tokens
    }

    response4 = client_gpt4.chat.completions.create(
        model=GPT4_DEPLOYMENT,
        messages=[
            {"role": "system", "content": req.system_prompt},
            *history,
            {"role": "user", "content": req.user_prompt}
        ],
        max_completion_tokens=MAX_TOKENS
    )

    results["gpt-4"] = {
        "response": response4.choices[0].message.content,
        "prompt_tokens": response4.usage.prompt_tokens,
        "completion_tokens": response4.usage.completion_tokens,
        "total_tokens": response4.usage.total_tokens
    }

    return results
# Expected Output