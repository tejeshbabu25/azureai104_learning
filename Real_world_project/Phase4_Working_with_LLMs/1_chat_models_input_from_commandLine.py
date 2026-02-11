from openai import AzureOpenAI
from typing import Dict, Any, List

GPT5_ENDPOINT = "https://tejeshbabu519-3246-resource.cognitiveservices.azure.com/"
GPT5_KEY = "gpt-5.2-chat-key-goes-here"
GPT5_DEPLOYMENT = "gpt-5.2-chat"
GPT5_API_VERSION="2024-12-01-preview"

GPT4_ENDPOINT = "https://tejeshbabu519-3246-resource.cognitiveservices.azure.com/"
GPT4_KEY = "gpt-4.1-chat-key-goes-here"
GPT4_DEPLOYMENT = "gpt-4.1"
GPT4_API_VERSION="2024-12-01-preview"

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

def ask_models(user_prompt: str,system_prompt: str = "You are a helpful assistant.",history: List[Dict[str, str]] = None)-> Dict[str, Any]:
    if history is None:
        history = []

    results = {}

    response5 = client_gpt5.chat.completions.create(
        model=GPT5_DEPLOYMENT,
        messages=[
            {"role": "system", "content": system_prompt},
            *history,
            {"role": "user", "content": user_prompt}
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
            {"role": "system", "content": system_prompt},
            *history,
            {"role": "user", "content": user_prompt}
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
# below code is only request to test from command line, not needed when using from Docker

if __name__ == "__main__":
    history = []
    user_input = "Explain the difference between supervised and unsupervised learning with examples."
    result = ask_models(user_input, history=history)
    for model, output in result.items():
        print(f"\n=== {model} ===")
        print("Response:", output["response"])
        print(f"Tokens Used → Prompt: {output['prompt_tokens']} | Completion: {output['completion_tokens']} | Total: {output['total_tokens']}")


# Expected Output
# === gpt-5 ===
# Response: **Supervised learning** and **unsupervised learning** are two main categories of machine learning, and they differ mainly in the type of data they use and the goals they pursue.

# ---

# ## Supervised Learning

# **Definition:**  
# Supervised learning uses **labeled data**, meaning each training example comes with an input and a known correct output (label). The model learns to map inputs to outputs.

# **Goal:**  
# Predict the correct output for new, unseen data.

# **How it works:**  
# - The algorithm is trained on input–output pairs.
# - It learns patterns that relate inputs to known labels.
# - Performance is evaluated using metrics like accuracy or error rate.

# **Common tasks:**
# - **Classification** (predicting categories)
# - **Regression** (predicting continuous values)

# **Examples:**
# - **Email spam detection:** Emails are labeled as *spam* or *not spam*.
# - **House price prediction:** Inputs like size and location are labeled with actual house prices.
# - **Image recognition:** Images labeled as *cat*, *dog*, etc.

# **Typical algorithms:**
# - Linear Regression
# - Logistic Regression
# - Decision Trees
# - Support Vector Machines
# - Neural Networks

# ---

# ## Unsupervised Learning

# **Definition:**
# Unsupervised learning uses **unlabeled data**, meaning the data has no predefined outputs.

# **Goal:**
# Discover hidden patterns, structures, or relationships in the data.

# **How it works:**
# - The algorithm analyzes data without guidance on correct answers.
# - It groups or organizes data based on similarity or structure.

# **Common tasks:**
# - **Clustering**
# - **Dimensionality reduction**
# - **Association rule learning**

# **Examples:**
# - **Customer segmentation:** Grouping customers based on purchasing behavior without predefined categories.
# - **Market basket analysis:** Finding products that are often bought together.
# - **Anomaly detection:** Identifying unusual patterns in network traffic or transactions.

# **Typical algorithms:**
# - K-Means Clustering
# - Hierarchical Clustering
# - DBSCAN
# - Principal Component Analysis (PCA)
# - Apriori Algorithm

# ---

# ## Key Differences at a Glance

# | Aspect | Supervised Learning | Unsupervised Learning |
# |------|-------------------|----------------------|
# | Data | Labeled | Unlabeled |
# | Output | Known | Unknown |
# | Main goal | Prediction | Pattern discovery |
# | Evaluation | Accuracy, error metrics | Often qualitative or indirect |
# | Example | Spam classification | Customer clustering |

# ---

# **In summary:**
# Supervised learning learns from examples with known answers, while unsupervised learning explores data to find structure without predefined labels.
# Tokens Used → Prompt: 29 | Completion: 537 | Total: 566

# === gpt-4 ===
# Response: Certainly! Here’s an explanation of the difference between **supervised** and **unsupervised learning**, with examples for each:

# ---

# **Supervised Learning:**

# - **Definition:**
#   In supervised learning, the machine learning model is trained on a labeled dataset. This means that each training example includes both the input data and the correct output (label). The model learns to map inputs to outputs by finding patterns in the labeled data.

# - **Goal:**
#   To predict the correct output (label) for new, unseen inputs.

# - **Examples:**
#   - **Spam Detection:** Given emails labeled as "spam" or "not spam", the model learns to classify new emails.
#   - **House Price Prediction:** Given features about houses (size, location, etc.) and their known selling prices, the model predicts the price of a new house.
#   - **Image Classification:** Given images of animals labeled by species (cat, dog, etc.), the model identifies the species of new images.

# ---

# **Unsupervised Learning:**

# - **Definition:**
#   In unsupervised learning, the dataset is *not* labeled. The model receives only the input data, without any associated output labels. The aim is to find structure or patterns within the data.

# - **Goal:**
#   To discover hidden patterns, groupings, or representations in the input data.

# - **Examples:**
#   - **Customer Segmentation:** Given purchase data without any labels, the model groups customers into segments based on their buying behavior.
#   - **Clustering News Articles:** Automatically grouping news articles by topic without pre-existing topic labels.
#   - **Dimensionality Reduction:** Reducing the number of features in data (e.g., with PCA) to simplify visualization or further processing.

# ---

# **In summary:**

# - **Supervised learning** uses labeled data to predict known outputs.
# - **Unsupervised learning** uses unlabeled data to find structure or patterns within the data.

# Let me know if you want more details or examples!
# Tokens Used → Prompt: 30 | Completion: 410 | Total: 440