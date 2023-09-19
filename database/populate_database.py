"""
Populate the database with the data from the json file.
"""

import json
import weaviate

from tqdm import tqdm

from modules.utilities import EnvironmentVariables

# Load environment variables
env = EnvironmentVariables()

# Create a client
client = weaviate.Client(
    url=env.get('WEAVIATE_CLIENT_ENDPOINT'),
    additional_headers={
        'X-OpenAI-Api-Key': env('OPENAI_API_KEY')
    }
)

# Check if schema exists
if not client.schema.contains():
    # Create schema
    client.schema.create(
        {
            'classes': [
                {
                    'class': 'Paper',
                    'description': 'A research paper',
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

def main(data_path: str = './data/ml-arxiv-embeddings.json'):
    """
    Populate the database with data.

    Args:
        data_path (str): Path to the data file.
    """

    # read data json file from ./data/ml-arxiv-embeddings.json
    with open(data_path, encoding='utf-8') as file:
        json_data = []
        # read file as text
        data = file.read()
        # split text into lines
        data = data.split('\n')
        for item in enumerate(data):
            if item != '':
                # parse json
                try:
                    json_data.append(json.loads(item[1]))
                except json.decoder.JSONDecodeError:
                    continue

    client.batch.configure(100)
    with client.batch as batch:
        for sample in tqdm(data):
            batch.add_data_object(
                data_object={
                    'DOI': sample['root']['id'],
                    'title': sample['root']['title'],
                    'authors': sample['root']['authors'],
                    'abstract': sample['root']['abstract'],
                    'date': sample['root']['update_date'],
                },
                class_name='Paper',
                vector=sample["root"]['embedding']
            )
