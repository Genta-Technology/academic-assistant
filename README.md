# Academic-Assistant
Genta Academic Assistant, an AI powered assistant to help you on your academic research

## Setup Database

### Setup virtual environment

Setup a virtual environment using venv

```bash
python -m venv venv
```

### Activate virtual environment

Activate the virtual environment

```bash
# in linux
source venv/bin/activate

# in windows
venv\Scripts\activate
```

### Install dependencies

install the dependencies using pip from the requirements.txt file

```bash
pip install -r requirements.txt
```

### Setup .env file

Copy the .env.example file to .env, then edit the .env file to match your database configuration

```bash
cp .env.example .env
```

### Download the database embedding data from kaggle: https://www.kaggle.com/datasets/awester/arxiv-embeddings

Download the data and extract it to a folder named 'data' inside the repository folder

### Run the database setup script

Run the database setup script to initialize the database

```bash
python database_initialization.py --data_path <path to the downloaded data>
```
