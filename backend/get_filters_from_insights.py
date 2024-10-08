from utils.process_outfit import parse_text
from gpt_bot import fetch_openai_response,build_assistant_prompt
# from prompt_insights import get_prompt
from user_purchase_insights import get_user_purchase_insight
from utils.uniqueValues import brand_name_array, color_array, article_type_array,occasion_array,text_description_array
unique_array_dict = {"brand_name": brand_name_array, "color": color_array,
                     "article_type": article_type_array, "occasion": occasion_array,'text_description':text_description_array}
def categorize_filters(insights, unique_array_dict):
    # Create dictionaries for hard and soft filters
    hard_filters = {"topwear": {}, "bottomwear": {}, "footwear": {}, "accessories": {}}
    soft_filters = {"topwear": {}, "bottomwear": {}, "footwear": {}, "accessories": {}}

    # Go through all 4 dictionaries
    for cat_insights in insights:
        category = cat_insights["category"]
        # Add the 'category' key to the hard & soft filters insights
        hard_filters[category]['category'] = category
        soft_filters[category]['category'] = category
        soft_filters[category]['text_description'] = cat_insights.get('text_description','none')

        for key in ['color', 'article_type', 'brand_name', 'occasion']:
            # Check if value exists in the corresponding unique array. If yes, it's a hard filter else a soft filter
            if cat_insights.get(key, None) and cat_insights[key] in unique_array_dict[key]:
                hard_filters[category][key] = cat_insights[f'{key}']
                soft_filters[category][key] = 'none'
            elif cat_insights.get(f'{category}_{key}', None):
                soft_filters[category][key] = cat_insights[f'{key}']
                hard_filters[category][key] = 'none'
    return hard_filters, soft_filters

# Unique values from PineconeLocal for 'brandName', 'baseColour', 'articleType', 'Occasion'

def analyse_user_purchase_insights_simple(user_purchase_csv):
    user_purchase_insights = get_user_purchase_insight(user_purchase_csv)
    categories = ["topwear", "bottomwear", "footwear", "accessories"]
    # pinecone_queries = []
    pinecone_queries={}

    for i, category in enumerate(categories, start=0):
        category_data = user_purchase_insights[i]
        pinecone_query = ""
        pinecone_queries[category]={}
        for key, value in category_data.items():
            if key != 'category' and value != 'none':
                if pinecone_query:
                    pinecone_query += ' '
                pinecone_query += value
                pinecone_queries[category][key]=value

        # pinecone_queries.append(pinecone_query)

    return pinecone_queries

def analyse_user_prompt_insights(user_prompt):
    keys = ['category', 'color', 'article_type', 'brand_name', 'occasion', 'text_description']
    base_prompt = build_assistant_prompt(keys, user_prompt=user_prompt)
    # base_response = fetch_gpt_response(SYSTEM_PROMPT + "\n" + base_prompt)
    #base_response = fetch_paid_openai_response(base_prompt)
    # base_response = get_gpt_response(SYSTEM_PROMPT + "\n" + base_prompt,paid=False)
    base_response = fetch_openai_response(base_prompt)

    if base_response is None:
        print("Sever is down")
        return

    print(base_response)
    top_wear, bottom_wear, foot_wear, accessories = parse_text(base_response, keys)
    print("Top Wear:", top_wear)
    print("Bottom Wear:", bottom_wear)
    print("Foot Wear:", foot_wear)
    print("Accessories:", accessories)
    user_prompt_insights = [top_wear, bottom_wear, foot_wear, accessories]
    # print("user_prompt_insights:", user_prompt_insights)

    hard_filters_prompt, soft_filters_prompt = categorize_filters(user_prompt_insights, unique_array_dict)
    # print("soft_filters_prompt:", soft_filters_prompt)
    # print("hard_filters_prompt:", hard_filters_prompt)
    print("hard filters prompt : ",hard_filters_prompt)
    print("soft filters prompt : ",soft_filters_prompt)
    return hard_filters_prompt, soft_filters_prompt
