import json
# import src.openai_embeddings.request
import os
def handler(event, context):

    body = event['body']

    key = os.environ.get('EMBDEDDINGS_OPENAI_API_KEY')
    data = "This is a large string..."
    # src.openai_embeddings.request.make_http_call_with_chunking(data, "text-embedding-ada-002", key)
    response = {
        "statusCode": 200,
        "body": json.dumps(data)
    }

    return response

