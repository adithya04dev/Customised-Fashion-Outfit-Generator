import os
import pinecone
from pinecone_text.sparse import BM25Encoder
from sentence_transformers import SentenceTransformer
import torch
import time
from dotenv import find_dotenv, load_dotenv
from pinecone import ServerlessSpec, PodSpec
# Load environment variables from the root .env file
root_env_path = find_dotenv()
load_dotenv(root_env_path)

import os
from pinecone import Pinecone

def initialize_pinecone():
    try:
        # initialize connection to pinecone (get API key at app.pinecone.io)
        api_key = os.getenv("PINECONE_API_KEY")
        env = os.getenv("PINECONE_ENVIRONMENT")
        # init connection to pinecone
        pinecone = Pinecone(api_key=api_key, environment=env)
        return pinecone
    except Exception as e:
        print(f"Error initializing Pinecone: {e}")
def get_clip_and_bm25_model():
    try:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model = SentenceTransformer('sentence-transformers/clip-ViT-B-32', device=device)
        bm25 = BM25Encoder()
        return model, bm25
    except Exception as e:
        print(f"Error getting CLIP and BM25 model: {e}")
def retreive_index(pinecone, index_name):
    env = os.getenv("PINECONE_ENVIRONMENT")
    spec = PodSpec(environment=env)
    try:
        if index_name not in pinecone.list_indexes().names():
            # create the index
            pinecone.create_index(
                index_name,
                dimension=512,
                metric="cosine",
                spec=spec
            )
        obj=pinecone.Index(index_name)
        if not  obj:
            print(" index is none ")
        return obj
    except Exception as e:
        print(f"Error creating index: {e}")

def setup_pinecone():
    start_time = time.time()

    try:
        # print('Initializing Pinecone...')
        pinecone = initialize_pinecone()
        print('Pine cone Initialization completed.')


        # print('Getting CLIP and BM25 model...')
        model, bm25 = get_clip_and_bm25_model()
        print('Models obtained:')
        # print('---- Model:', model)
        # print('---- BM25:', bm25)

        # print('Retieveing index.')
        index_name = "complete-database"
        pinecone_index = retreive_index(pinecone, index_name)
        print('Index Retievied:', pinecone_index)
        # print('Setup completed.')
        end_time = time.time()
        print(f'Time taken: {end_time - start_time} seconds')
        return pinecone_index, model, bm25

    except Exception as e:
        print(f"Error setting up Pinecone: {e}")

def build_hard_filters( occasion=None, article_type=None, color=None, brand_name=None,
                       gender=None, is_jewellery=None, master_category=None,
                       product_display_name=None, season=None, style_image=None,
                       sub_category=None):
    hard_filters = {}

    if occasion is not None: hard_filters["occasion"] = {"$eq": occasion}
    if article_type is not None: hard_filters["article_type"] = {"$eq": article_type}
    if color is not None: hard_filters["color"] = {"$eq": color}
    if brand_name is not None: hard_filters["brand_name"] = {"$eq": brand_name}
    if gender is not None: hard_filters["gender"] = {"$eq": gender}
    if is_jewellery is not None: hard_filters["is_jewellery"] = {"$eq": is_jewellery}
    if master_category is not None: hard_filters["master_category"] = {"$eq": master_category}
    if product_display_name is not None: hard_filters["product_display_name"] = {"$eq": product_display_name}
    if season is not None: hard_filters["season"] = {"$eq": season}
    if style_image is not None: hard_filters["style_image"] = {"$eq": style_image}
    if sub_category is not None: hard_filters["sub_category"] = {"$eq": sub_category}

    # if curr_category == 'topwear':
    #     hard_filters["sub_category"] = {"$eq": "topwear"}
    # if curr_category == 'bottomwear':
    #     hard_filters["sub_category"] = {"$eq": "bottomwear"}
    # if curr_category == 'footwear':
    #     hard_filters["master_category"] = {"$eq": "footwear"}
    # if curr_category == 'accessories':
    #     hard_filters["master_category"] = {"$eq": "accessories"}

    return hard_filters





