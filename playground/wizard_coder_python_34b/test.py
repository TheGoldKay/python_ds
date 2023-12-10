import requests, time

API_URL = "https://api-inference.huggingface.co/models/WizardLM/WizardCoder-3B-V1.0"
headers = {"Authorization": "Bearer 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"}
time.sleep(1)
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
    "inputs": "Give me an idea of how to cook an egg",
})
print(output)
