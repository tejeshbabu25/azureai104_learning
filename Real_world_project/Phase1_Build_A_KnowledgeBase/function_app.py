import azure.functions as func
import logging,os,json,requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="ask")
def ask(req: func.HttpRequest) -> func.HttpResponse:
    endpoint="https://langservice-tej13.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=mycustomQA&api-version=2021-10-01&deploymentName=production"
    api_key=os.environ["LANGUAGE_API_KEY"]
    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "application/json"
    }

    logging.info(api_key)
    logging.info(endpoint)

    req_body = req.get_json()
    question=req_body.get("question")
    data={
        "question": question,
        "top": 1
    }

    response = requests.post(endpoint, headers=headers, json=data)
    results=response.json()

    answers = results.get("answers", [])
    answers = answers[0]
    output = {"answer": answers}

    logging.info(output)
    return func.HttpResponse(json.dumps(output), mimetype="application/json")
