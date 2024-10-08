def parse_text(input_string, keys):
    # print("Debug: Starting parse_text function")
    # print(f"Debug: Input keys: {keys}")
    
    # Initialize dictionaries
    article_dict = {'topwear': {}, 'bottomwear': {}, 'footwear': {}, 'accessories': {}}
    # print(f"Debug: Initialized article_dict: {article_dict}")

    # Loop through each line in the input string
    for line in input_string.split('\n'):
        # print(f"\nDebug: Processing line: {line}")

        # Skip empty lines
        if not line.strip():
            # print("Debug: Skipping empty line")
            continue

        parts = line.split(': ')
        # print(f"Debug: Line parts: {parts}")
        if len(parts) < 2:
            continue
        # Find out which article the current line pertains to
        for article in article_dict:

            if article in parts[0]:
                # print(f"Debug: Matched article: {article}")
                current_category = article
                article_dict[article]['category'] = current_category
                # print(f"Debug: Set category for {article}: {current_category}")

                if 'to_change' in parts[0]:
                    to_change_value = parts[1].strip().lower() == 'true'
                    if current_category:
                        article_dict[current_category]['to_change'] = to_change_value
                        # print(f"Debug: Set to_change for {current_category}: {to_change_value}")

                # For the identified article, see if the key is in our defined keys
                for key in keys:
                    if key in parts[0]:
                        article_dict[article][key] = parts[1]
                        # print(f"Debug: Set {key} for {article}: {parts[1]}")
                        # break


    # print("Debug: Returning results")
    return article_dict['topwear'], article_dict['bottomwear'], article_dict['footwear'], article_dict['accessories']
def extract_category_info(data):
    categories = {
        "topwear": {},
        "bottomwear": {},
        "footwear": {},
        "accessories": {}
    }
    categories_array = ["topwear", "bottomwear", "footwear", "accessories"]

    for i, item in enumerate(data["outfit"]):
        category = categories_array[i]  # Get category based on index
        info = {
            "product_display_name": item["product_display_name"],
            "brand_name": item["brand_name"],
            "color": item["color"],
            "article_type": item["article_type"],
            "master_category": item["master_category"]
        }
        categories[category] = info

    return categories