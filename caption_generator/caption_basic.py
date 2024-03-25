import requests


API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer {Auth_Token}"}  # Authorization Token 

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Questions:which is the largest country in the world? Answer:",
})
generated_text = output[0]["generated_text"]
# Split the generated text by "Answer:" to get only the answer part
answer = generated_text.split("Answer:")[1].strip()

print("Answer:", answer)