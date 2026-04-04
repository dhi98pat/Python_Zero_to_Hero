from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
## Creating a Flask application instance
app = Flask(__name__)
@app.route("/createJIRA", methods=["POST"])
def createJIRA():
    return "Creating a JIRA issue!"
    url = "https://devops.atlassian.net/rest/api/3/issue"

    API_TOKEN = ""
    auth = HTTPBasicAuth("email@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first Jira !!",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10004"
        },
        "project": {
        "key": "SCRUM"
        },
        "summary": "My First Jira Ticket",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=5000)