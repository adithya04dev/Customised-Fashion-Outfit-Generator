import os

import openai
from fastapi import HTTPException
import google.generativeai as genai
import pandas as pd
import random
from dotenv import find_dotenv,load_dotenv

# from langchain_groq import ChatGroq

# Load environment variables from the root .env file
root_env_path = find_dotenv()
load_dotenv(root_env_path)
df=pd.read_csv(r'C:\Users\adith\Documents\Projects\python-projects\genai_hackathon\lookify\backend\dataset\main_dataset.csv')

categories = ['topwear','bottomwear','footwear','accessories']
l=df['article_type'].value_counts().head(80).index.tolist()
keys = ['category', 'color', 'article_type', 'brand_name', 'occasion','text_description']

SYSTEM_PROMPT = '''
You are E-Commerce GPT, a professional Analyst from the Fashion E-commerce industry with expertise
 in analyzing user needs based on User Prompt given to u by suggesting coordinated outfits.

As E-Commerce GPT, your task is to generate key-value pairs for all four categories: 
['topwear', 'bottomwear', 'footwear', 'accessories'] based on the user prompt.

The following are the correct values that could be assigned to 'article_type' category, grouped by main categories:

Topwear: ['tshirts', 'shirts', 'kurtas', 'tops', 'sweatshirts', 'sweaters', 'jackets', 'kurtis', 'innerwear_vests', 'tunics', 'dresses', 'bra', 'camisoles']

Bottomwear: ['jeans', 'trousers', 'shorts', 'track_pants', 'leggings', 'capris', 'skirts', 'lounge_pants', 'boxers', 'briefs', 'patiala', 'jeggings']

Footwear: ['casual_shoes', 'sports_shoes', 'heels', 'flip_flops', 'sandals', 'formal_shoes', 'flats', 'sports_sandals']

Accessories: ['watches', 'handbags', 'sunglasses', 'wallets', 'belts', 'backpacks', 'socks', 'perfume_and_body_mist', 'sarees', 'earrings', 'deodorant', 'nail_polish', 'lipstick', 'clutches', 'caps', 'ties', 'nightdress', 'pendant', 'necklace_and_chains', 'lip_gloss', 'night_suits', 'trunk', 'scarves', 'ring', 'dupatta', 'accessory_gift_set', 'cufflinks', 'kajal_and_eyeliner', 'stoles', 'kurta_sets', 'free_gifts', 'duffel_bag', 'bangle', 'laptop_bag', 'foundation_and_primer', 'bracelet', 'face_moisturisers', 'jewellery_set', 'fragrance_gift_set', 'highlighter_and_blush', 'compact', 'lip_liner', 'mobile_pouch', 'messenger_bag', 'eyeshadow', 'suspenders', 'mufflers']

Ensure that while generating key-value pairs for the outfit, the article_type for topwear, footwear, bottomwear, and accessories 
is well-coordinated.


Based on prompt understand and assign values based on the specific keys: ['category', 'color', 'article_type', 'brand_name', 'occasion', 'text_description'] .
You need to generate 4 sets of key pairs, key format {category}_{key_name}.
 eg: \n topwear_category: top_wear \n topwear_article_type: t-shirt \n Understand this as context.
 
 never  ever leave {category}_article_type,{category}_text_description as none.
'''

from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
def initialize_chat():
    store = {}
    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    model = ChatOpenAI(model="gpt-4o-mini",temperature=0.3)
    # model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002",temperature=0.6)
    # model = ChatGroq(model="llama-3.1-70b-versatile")

    llm_with_message_history = RunnableWithMessageHistory(model, get_session_history)
    config = {"configurable": {"session_id": 'session_id:'+str(random.randint(1, 1000000))}}
    response = llm_with_message_history.invoke(
        [HumanMessage(content=SYSTEM_PROMPT)],
        config=config,
        )

    return llm_with_message_history,config
llm_with_message_history,config=initialize_chat()

chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]






PINECONE_INFO_PROMPT = '''
This is for your context: These are the 4 Items Pinecone results have given us based on the search, now these are shown to user: \n
'''
format=''' 
Topwear

- topwear_category: 
- topwear_color: 
- topwear_article_type: 
- topwear_brand_name: 
- topwear_occasion: 
- topwear_text_description: 
- topwear_to_change: 

Bottomwear

- bottomwear_category: 
- bottomwear_color: 
- bottomwear_article_type: 
- bottomwear_brand_name: 
- bottomwear_occasion: 
- bottomwear_text_description: 
- bottomwear_to_change: 

Footwear

- footwear_category: 
- footwear_color: 
- footwear_article_type: 
- footwear_brand_name: 
- footwear_occasion: 
- footwear_text_description: 
- footwear_to_change: 

Accessories

- accessories_category: 
- accessories_color: 
- accessories_article_type: 
- accessories_brand_name: 
- accessories_occasion: 
- accessories_text_description: 
- accessories_to_change: 


'''

def build_pinecone_information_prompt(pinecone_output: str):
    keys.append('{category_name}_to_change: True or False')
    end_prompt = f'''
        now user will give you a new prompt, understand what user want's to change from these categories: {categories}
        based on that generate key-value pair like before, if user wants to change something include that as value for that key.
        Remember to assign valueto  article_type to only to values that i gave u before as context. 
        if user doesn't want any change values should be 'none', keys:{keys} \n, eg: accessories_to_change: True or False
        this is the format for it {format}
        For categories that don't need to be changed only return to_change key.Now again understand this as context.'''
    pinecone_information_prompt = f"{PINECONE_INFO_PROMPT} \n {pinecone_output} \n {end_prompt} "
    return pinecone_information_prompt



def fetch_openai_response(user_prompt: str):
    try:

        global llm_with_message_history,config 
        response = llm_with_message_history.invoke(
        [HumanMessage(content=user_prompt)],
            config=config,
        )  
        print(response.usage_metadata)
        reply=response.content
        with open("prompt.txt","w") as f:
            f.write(SYSTEM_PROMPT + "\n" + user_prompt)
        return reply.replace('**','').lower() 
    except Exception as e:
        print("Exception occurred while fetching response from openai", e)
        # Handle the exception and return a 500 status code
        error_message = f"An error occurred: {str(e)}"
        error_response = {"error": error_message, "status": 500}
        raise HTTPException(status_code=500, detail=error_message)

def build_assistant_prompt(keys, user_prompt):
    base_prompt = f"\nUser Prompt: {user_prompt}\n "
    # base_prompt +=f" if any festival is present in prompt, fill 'ethnic' in all 'occasion' keys, eg: Karwa Chauth or Diwali or Rakhi, topwear_occasion: ethnic "
    return base_prompt

