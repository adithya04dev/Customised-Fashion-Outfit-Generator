from pydantic import BaseModel


class UserPromptInput(BaseModel):
    user_prompt: str


from pre_process_hard_filters import get_outfit_from_prompt, pre_process_filters
from fastapi import APIRouter
from gpt_bot import llm_with_message_history,config,initialize_chat
endpoint_router = APIRouter()
GET_OUTFIT_ENDPOINT_COUNT = 0

OUTFIT_HISTORY = []

user_purchase_csv = 'dataset/user_history_data/gwen_2.csv'

@endpoint_router.get("/reset_chat")
def reset_chat():
    global llm_with_message_history,config
    llm_with_message_history,config=initialize_chat()
    global GET_OUTFIT_ENDPOINT_COUNT, OUTFIT_HISTORY
    GET_OUTFIT_ENDPOINT_COUNT = 0
    OUTFIT_HISTORY.clear()


    print("Chat Reset")
    return {"message": "Chat reset was successful"}


OCCASSION = None




from fastapi import HTTPException

@endpoint_router.post("/get_outfit")
def get_outfit(user_prompt_object: UserPromptInput):
    global GET_OUTFIT_ENDPOINT_COUNT, OUTFIT_HISTORY, user_purchase_csv
    user_prompt = user_prompt_object.user_prompt
    GET_OUTFIT_ENDPOINT_COUNT += 1

    try:
        print(GET_OUTFIT_ENDPOINT_COUNT, " time get_outfit is running ")
        response = None
        outfit = None
        if GET_OUTFIT_ENDPOINT_COUNT == 1:
            outfit = get_outfit_from_prompt(user_prompt, user_purchase_csv)
        else:
            prev_outfit_index = GET_OUTFIT_ENDPOINT_COUNT - 2
            from handle_change_prompt import handle_change_prompt, handle_next_prompt
            handle_change_prompt(OUTFIT_HISTORY[prev_outfit_index])  # handle 2nd prompt onwards
            outfit = handle_next_prompt(user_prompt, prev_outfit_index)

        if outfit is None:
            raise HTTPException(status_code=500, detail=error_message)
        response = {"outfit": outfit}
        OUTFIT_HISTORY.append(response)
        return response
    except Exception as e:
        # Handle the exception and return a 500 status code
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        error_response = {"error": error_message, "status": 500}
        # return error_response  # Return the error response with 500 status code
        raise HTTPException(status_code=500, detail=error_message)






