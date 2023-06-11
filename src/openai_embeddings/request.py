import requests
import json
import os
import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

def make_http_call_with_chunking(input_string, model, api_key):
    headers = ""
    # Define the URL to make the HTTP call
    url = "https://api.openai.com/v1/embeddings"

    # Define the chunk size
    chunk_size = 1000

    # Initialize an empty list to store the chunks
    chunks = []

    # Split the data into chunks
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        chunks.append(chunk)

    # Prepare the headers for the HTTP request
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    # Initialize an empty list to store the response chunks
    response_chunks = []

    # Send the chunked data in the HTTP request
    for chunk in chunks:
        # Construct the JSON payload with the two fields
        payload = {
            "input": input_string,
            "model": model
        }

        # Convert the payload to JSON
        json_payload = json.dumps(payload)

        # Send the HTTP request with the chunked data
        response = requests.post(url, data=json_payload, headers=headers)
        response_chunks.append(response.text)

    # Concatenate the response chunks
    response_data = ''.join(response_chunks)

    # Save the response as JSON
    return json.loads(response_data)

key = os.environ.get('EMBDEDDINGS_OPENAI_API_KEY')
data = "This is a large string..."
response = make_http_call_with_chunking(data, "text-embedding-ada-002", key)
collection.add(
    response.data
)
results = collection.query(
    query_texts=["large"],
    n_results=2
)


print("DATA: " + results)
