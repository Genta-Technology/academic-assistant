import weaviate
import json

from tqdm import tqdm

from modules import utilities

# Create a client
client = weaviate.Client(
    url=utilities.env.get('WEAVIATE_CLIENT_ENDPOINT'),
    additional_headers={
        'X-OpenAI-Api-Key': utilities.env('OPENAI_API_KEY')
    }
)

try:
    # Create schema
    client.schema.create(
        {
            'classes': [
                {
                    'class': 'Paper',
                    'description': 'A research paper',
                    "vectorizer": "text2vec-openai",
                    'properties': [
                        {
                            'name': 'DOI',
                            'description': 'ID of the paper',
                            'dataType': ['string'],
                        },
                        {
                            'name': 'title',
                            'description': 'Title of the paper',
                            'dataType': ['string']
                        },
                        {
                            'name': 'authors',
                            'description': 'Authors of the paper',
                            'dataType': ['string']
                        },
                        {
                            'name': 'abstract',
                            'description': 'Abstract of the paper',
                            'dataType': ['string']
                        },
                        {
                            'name': 'date',
                            'description': 'Date of the paper',
                            'dataType': ['string']
                        },
                    ]
                }
            ]
        }
    )
except:
    pass

def main(data_path: str = './data/ml-arxiv-embeddings.json'):
    # read data json file from ./data/ml-arxiv-embeddings.json
    with open(data_path) as f:
        data = json.load(f)

    client.batch.configure(100)
    with client.batch as batch:
        for i, d in enumerate(tqdm(data)):
            batch.add_data_object(
                data_object={
                    'DOI': d['id'],
                    'title': d['title'],
                    'authors': d['authors'],
                    'abstract': d['abstract'],
                    'date': d['update_date'],
                },
                class_name='Paper',
                vector=d['embedding']
            )