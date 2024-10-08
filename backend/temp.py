import getpass
import os
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
os.environ["GOOGLE_API_KEY"] = 'AIzaSyCEBX0fTi-Tuvso5fNYVwkeKn3jeU0KkvA'
import random
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_google_genai import ChatGoogleGenerativeAI
store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# model = ChatOpenAI(model="gpt-4o-mini")
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002")
# model = ChatGroq(model="llama-3.1-70b-versatile")
llm_with_message_history = RunnableWithMessageHistory(model, get_session_history)
config = {"configurable": {"session_id": 'session_id:'+str(random.randint(1, 1000000))}}
response = llm_with_message_history.invoke(
    [HumanMessage(content="hello")],
    config=config,
    )
print(response.usage_metadata)