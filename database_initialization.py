"""
Populate the database with data.

Usage:
    python database_initialization.py --data ./data/ml-arxiv-embeddings.json
"""

import argparse

from database import populate_database

# setup command line arguments
parser = argparse.ArgumentParser(description='Populate the database with data.')
parser.add_argument(
    '--data',
    type=str,
    default='./data/ml-arxiv-embeddings.json',
    help='Path to the data file.'
)
args = parser.parse_args()

if __name__ == '__main__':
    populate_database.main(args.data)
