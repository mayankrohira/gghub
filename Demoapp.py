import requests
import base64
import os
from openai import AzureOpenAI
# import dotenv
# dotenv.load_dotenv()

# Configuration

# The API key for your Azure OpenAI resource.
API_KEY = "2f902b2128374677a7234fa882903a03"
# Setting up the deployment name
# deployment_name = os.environ['COMPLETIONS_MODEL']



# Currently Chat Completion API have the following versions available: 2023-03-15-preview
api_version = "2024-02-15-preview"


# The base URL for your Azure OpenAI resource. e.g. "https://<your resource name>.openai.azure.com"
azure_endpoint  = "https://genai-openai-datadynamos.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview" 

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "Provide only Barclays product related information and at end  say Thanks for reaching out to XYZ customer support"
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}





# # Send request
try:
    response = requests.post(azure_endpoint, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

client = AzureOpenAI(
  api_key=API_KEY,  
  azure_endpoint=azure_endpoint,
  api_version=api_version
)


response_1 =  client.chat.completions.create(
                model=response.json()['model'],messages=[{"role": "system", "content": "Provide only Barclays product related information and at end  say Thanks for reaching out to XYZ customer support"},{"role": "user", "content": "Who let the dogs?"}])

# print the response
print(response_1.choices[0].message.content)