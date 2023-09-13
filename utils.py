import numpy as np
from numpy import dot
from numpy.linalg import norm
import openai 
from openai.embeddings_utils import cosine_similarity

def open_ai_embeddings(input_str:str, api_token:str):
    # use the api token
    openai.api_key = api_token
    
    # convert text to embedding
    model_id = "text-embedding-ada-002"
    embedding = openai.Embedding.create(input=input_str, model=model_id)['data'][0]['embedding']
    return embedding

def top_n_similarity_index(n:int, main_vector:np.array, vector_list:np.array):
    similarity_list = [cosine_similarity(main_vector, v) for v in vector_list]
    similarity_list = np.argsort(similarity_list)[-n:]
    return similarity_list

def get_embedding_similarity_index(n:int, input_str:str, embedding_list:list, api_token:str):
    embedded_text = open_ai_embeddings(input_str, api_token=api_token)
    top_index = top_n_similarity_index(n=n, main_vector=embedded_text, vector_list=embedding_list)
    return top_index