
from gpt_bot import build_pinecone_information_prompt,fetch_openai_response
from utils.uniqueValues import keys
from pre_process_hard_filters import get_outfit_selected
from main import OUTFIT_HISTORY, user_purchase_csv
from utils.process_outfit import parse_text
from utils.process_outfit import extract_category_info

def handle_change_prompt(outfit):
    try:            
        category_info = extract_category_info(outfit)
        # print("outfit",outfit)
        # print("category_info",category_info)
        pinecone_prompt = build_pinecone_information_prompt(category_info)


        response = fetch_openai_response(pinecone_prompt)
        print("get gpt response for handle change prompt completed")
        if response is None:
            print("Sever is down")
            return

        print(response)
    except Exception as e:
        print("exception in handle_change_prompt",e)

def handle_next_prompt(user_prompt: str, prev_outfit_index):


    next_response = fetch_openai_response(f"User prompt : {user_prompt}")
    print("get gpt response for handle next prompt completed")
    print(next_response)

    if next_response is None:
        print("Sever is down")
        return

    curr_categories = []
    category_dict_array = parse_text(next_response, keys=keys)

    print("\n category_dict_array:", category_dict_array)

    for category_dict in category_dict_array:
        category = category_dict['category']
        to_change = category_dict.get('to_change', False)
        if to_change:
            curr_categories.append(category)
        else:
            curr_categories.append('none')

    print(curr_categories)
    # each category is a dictionary that contain a key called to_change
    # add it to curr_categories, if not present add 'none'
    outfit = get_outfit_selected(user_prompt, user_purchase_csv, curr_categories, category_dict_array)

    # loading last articles from history.
    try:
        for i, article_dict in enumerate(outfit):
            if article_dict is None:
            # load from history
                length=len(OUTFIT_HISTORY[prev_outfit_index]['outfit'])

                article_dict = OUTFIT_HISTORY[prev_outfit_index]['outfit'][i]
                outfit[i] = article_dict
    except Exception as e:
        print(OUTFIT_HISTORY)
        # print(prev_outfit_index)
        print(outfit)
        # print(length)
        # print("outfit history in handle_next_prompt is:",OUTFIT_HISTORY[prev_outfit_index])
        # print("index being accessed",prev_outfit_index)
        print("exception in handle_next_prompt",e)

    return outfit

